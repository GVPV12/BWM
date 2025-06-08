import os
import sys
import time
from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
import random
import json

# --- Configuración de codificación para la consola (opcional, para emojis si se intentan) ---
# Esta parte es para intentar que los emojis se vean, pero no está garantizado en todas las consolas.
# Para máxima compatibilidad, se quitarán los emojis en el código a continuación.
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
        sys.stderr = open(sys.stderr.fileno(), mode='w', encoding='utf-8', buffering=1)
    except Exception as e:
        # Fallback si no se puede reconfigurar stdout/stderr
        print(f"Advertencia: No se pudo configurar la consola para UTF-8: {e}")


# --- Archivo para guardar las marcas de agua ---
WATERMARKS_FILE = "watermarks.json"

def loading_animation():
    """Muestra una animación de carga en la consola."""
    animation_chars = [".  ", ".. ", "..."]
    print("Iniciando aplicacion. Por favor, espere...")
    for i in range(15):
        sys.stdout.write(f"\rCargando{animation_chars[i % len(animation_chars)]}")
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\r" + " " * 30 + "\r") # Limpia la línea al terminar
    sys.stdout.flush()


def load_watermarks():
    """Carga las marcas de agua guardadas desde el archivo JSON."""
    if os.path.exists(WATERMARKS_FILE):
        with open(WATERMARKS_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"Advertencia: El archivo '{WATERMARKS_FILE}' esta corrupto o vacio. Se iniciara con una lista vacia.")
                return []
    return []

def save_watermarks(watermarks):
    """Guarda la lista de marcas de agua en el archivo JSON."""
    with open(WATERMARKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(watermarks, f, indent=4, ensure_ascii=False)

def add_watermark_to_image(image_path, output_path, watermark_text, font_path=None, font_size=40,
                           font_color=(0, 0, 0, 128), stroke_width=0, stroke_fill=(0, 0, 0, 255),
                           position="bottom_left", custom_margin_x=20, custom_margin_y=20,
                           center_offset_x=0, center_offset_y=0):
    """
    Adds a text watermark to an individual image with an optional stroke.
    The output image will be saved as JPEG, converting from RGBA to RGB if necessary.
    """
    base_file_name = os.path.basename(image_path)

    try:
        with Image.open(image_path) as img:
            # --- Corrección de Orientación EXIF ---
            img = ImageOps.exif_transpose(img)

            # Crear una capa para el texto con transparencia.
            base_image = img.convert("RGBA")
            draw = ImageDraw.Draw(base_image)

            # --- Manejo de la fuente mejorado ---
            font = None
            # Primero intenta cargar la fuente Poppins descargada
            if font_path and os.path.exists(font_path):
                try:
                    font = ImageFont.truetype(font_path, font_size)
                except IOError:
                    print(f"Advertencia: No se pudo cargar la fuente '{font_path}'. Intentando con 'arial.ttf'.")
            
            # Si Poppins no se cargó o no existe, intenta Arial
            if font is None:
                try:
                    # En sistemas Windows, Arial.ttf suele estar disponible
                    font = ImageFont.truetype("arial.ttf", font_size)
                except IOError:
                    print("Advertencia: 'arial.ttf' no encontrada. Usando la fuente predeterminada de Pillow.")
                    # Si Arial tampoco está, usa la fuente por defecto de Pillow
                    font = ImageFont.load_default()

            # --- Verificar si se obtuvo una fuente válida ---
            if font is None:
                print(f"Error: No se pudo cargar ninguna fuente para la imagen '{base_file_name}'.")
                return False, base_file_name

            # --- Cálculo del tamaño del texto (bbox) ---
            if not watermark_text.strip():
                print(f"Advertencia: La marca de agua para '{base_file_name}' esta vacia. No se aplicara.")
                return False, base_file_name

            try:
                # Usa textbbox para obtener las coordenadas del bounding box del texto
                left, top, right, bottom = draw.textbbox((0, 0), watermark_text, font=font, stroke_width=stroke_width)
                text_width = right - left
                text_height = bottom - top
                
            except Exception as e:
                print(f"Error al calcular el tamano del texto para '{base_file_name}': {e}. Esto puede indicar un problema con la fuente o el texto.")
                return False, base_file_name

            img_width, img_height = base_image.size

            x, y = 0, 0

            # --- Posicionamiento de la marca de agua ---
            if position == "top_left":
                x = custom_margin_x
                y = custom_margin_y
            elif position == "top_right":
                x = img_width - text_width - custom_margin_x
                y = custom_margin_y
            elif position == "bottom_left":
                x = custom_margin_x
                y = img_height - text_height - custom_margin_y
            elif position == "bottom_right":
                x = img_width - text_width - custom_margin_x
                y = img_height - text_height - custom_margin_y
            elif position == "center":
                x = (img_width - text_width) / 2
                y = (img_height - text_height) / 2
            elif position == "center_offset_right":
                x = (img_width - text_width) / 2 + center_offset_x
                y = (img_height - text_height) / 2
            elif position == "center_offset_left":
                x = (img_width - text_width) / 2 - center_offset_x
                y = (img_height - text_height) / 2
            elif position == "center_offset_top":
                x = (img_width - text_width) / 2
                y = (img_height - text_height) / 2 - center_offset_y
            elif position == "center_offset_bottom":
                x = (img_width - text_width) / 2
                y = (img_height - text_height) / 2 + center_offset_y
            elif position == "random":
                max_x = img_width - text_width - custom_margin_x
                max_y = img_height - text_height - custom_margin_y

                if max_x <= custom_margin_x:
                    x = custom_margin_x
                else:
                    x = random.randint(custom_margin_x, max_x)

                if max_y <= custom_margin_y:
                    y = custom_margin_y
                else:
                    y = random.randint(custom_margin_y, max_y)

            x = int(max(0, min(x, img_width - text_width)))
            y = int(max(0, min(y, img_height - text_height)))

            # --- Dibujar el texto con trazo (stroke) si se especifica ---
            if stroke_width > 0:
                draw.text((x, y), watermark_text, font=font, fill=stroke_fill, stroke_width=stroke_width)

            # --- Dibujar el texto principal ---
            draw.text((x, y), watermark_text, font=font, fill=font_color)

            # --- Convertir a RGB si el formato de salida es JPEG y la imagen original es RGBA ---
            if output_path.lower().endswith(('.jpg', '.jpeg')):
                final_img = Image.new("RGB", base_image.size, (255, 255, 255)) # Crea una nueva imagen RGB con fondo blanco
                final_img.paste(base_image, (0, 0), base_image) # Pega la imagen RGBA sobre la nueva RGB, usando el canal alfa
            else:
                final_img = base_image

            final_img.save(output_path)
            return True, base_file_name
    except FileNotFoundError:
        print(f"Error: La imagen '{base_file_name}' no se encontro.")
        return False, base_file_name
    except Exception as e:
        print(f"Error general al procesar la imagen '{base_file_name}': {e}")
        return False, base_file_name

def watermark_multiple_images(input_folder, output_folder, watermark_text, font_path=None, font_size=40,
                               font_color=(0, 0, 0, 128), stroke_width=0, stroke_fill=(0, 0, 0, 255),
                               position="bottom_left", custom_margin_x=20, custom_margin_y=20,
                               center_offset_x=0, center_offset_y=0):
    """
    Applies a text watermark to all images in an input folder
    and saves them to an output folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    processed_files = []
    failed_files = []

    files_in_input_folder = [f for f in os.listdir(input_folder)]
    total_files = len(files_in_input_folder)

    print(f"Se intentara procesar todos los archivos encontrados ({total_files}).")
    print("El script dependera de la libreria Pillow para identificar si un archivo es una imagen compatible.")

    for filename in files_in_input_folder:
        image_path = os.path.join(input_folder, filename)

        name, ext = os.path.splitext(filename)
        output_filename = name + ".jpg" # Siempre guardar como JPG
        output_path = os.path.join(output_folder, output_filename)

        success, file_name = add_watermark_to_image(image_path, output_path, watermark_text, font_path, font_size,
                                                    font_color, stroke_width, stroke_fill, position,
                                                    custom_margin_x, custom_margin_y, center_offset_x, center_offset_y)
        if success:
            processed_files.append(file_name)
            print(f"Marca de agua anadida a: {file_name}")
        else:
            failed_files.append(file_name)

    processed_count = len(processed_files)
    error_count = len(failed_files)

    print("\n--- Resumen del Proceso ---")
    if total_files == 0:
        print(f"No se encontraron archivos en la carpeta '{input_folder}'.")
    elif error_count == total_files:
        print("¡Se produjo un error! Ningun archivo pudo ser procesado como imagen.")
        if failed_files:
            print(f"Archivos fallidos ({error_count}):")
            for f_name in failed_files:
                print(f"  - {f_name}")
    elif processed_count == total_files:
        print(f"Proceso completado. Se procesaron {processed_count} archivos exitosamente.")
    elif error_count > 0 and processed_count > 0:
        print(f"¡Atencion! Algunos archivos fueron procesados y otros no.")
        print(f"  - Imagenes procesadas con exito ({processed_count}):")
        for p_name in processed_files:
            print(f"    - {p_name}")
        print(f"  - Archivos no procesados como imagenes ({error_count}):")
        for f_name in failed_files:
            print(f"    - {f_name}")
    elif processed_count > 0 and error_count == 0:
        print(f"Proceso completado. Se procesaron {processed_count} archivos exitosamente.")
    elif processed_count == 0 and error_count > 0:
        print(f"No se pudieron procesar imagenes. Archivos fallidos ({error_count}):")
        for f_name in failed_files:
            print(f"  - {f_name}")

def download_font_if_not_exists(font_name, font_url, download_path="."):
    """
    Downloads a font file if it doesn't already exist.
    """
    font_full_path = os.path.join(download_path, font_name)
    if not os.path.exists(font_full_path):
        print(f"Descargando {font_name} de {font_url}...")
        try:
            response = requests.get(font_url, stream=True)
            response.raise_for_status()
            with open(font_full_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            # Mensaje de descarga exitosa eliminado para una experiencia más limpia
        except requests.exceptions.RequestException as e:
            print(f"Error al descargar la fuente: {e}")
            return None
    return font_full_path

def get_user_position_choice(margin_x, margin_y, offset_value):
    """Funcion para que el usuario elija la posicion de la marca de agua."""
    selected_position = ""
    center_offset_x = 0
    center_offset_y = 0

    while True:
        print("\n¿Quieres la marca de agua en una posicion ALEATORIA?")
        print("1. Si, aleatoria")
        print("2. No, quiero elegir una posicion especifica (centro o esquinas)")

        main_choice = input("Introduce el numero de tu eleccion: ")

        if main_choice == '1':
            selected_position = "random"
            break

        elif main_choice == '2':
            while True:
                print("\nElige la posicion de la marca de agua:")
                print("1. Centro (exacto o desplazado)")
                print("2. Arriba a la izquierda")
                print("3. Arriba a la derecha")
                print("4. Abajo a la izquierda")
                print("5. Abajo a la derecha")

                other_choice = input("Introduce el numero de tu eleccion: ")

                if other_choice == '1':
                    while True:
                        print("\nElige la sub-posicion central:")
                        print("1. Centro (exacto)")
                        print("2. Centro mas a la Derecha")
                        print("3. Centro mas a la Izquierda")
                        print("4. Centro mas Arriba")
                        print("5. Centro mas Abajo")

                        center_sub_choice = input("Introduce el numero de tu eleccion central: ")
                        if center_sub_choice == '1':
                            selected_position = "center"
                            break
                        elif center_sub_choice == '2':
                            selected_position = "center_offset_right"
                            center_offset_x = offset_value
                            break
                        elif center_sub_choice == '3':
                            selected_position = "center_offset_left"
                            center_offset_x = offset_value
                            break
                        elif center_sub_choice == '4':
                            selected_position = "center_offset_top"
                            center_offset_y = offset_value
                            break
                        elif center_sub_choice == '5':
                            selected_position = "center_offset_bottom"
                            center_offset_y = offset_value
                            break
                        else:
                            print("Opcion central no valida. Intentalo de nuevo.")
                    break

                elif other_choice == '2':
                    selected_position = "top_left"
                    break
                elif other_choice == '3':
                    selected_position = "top_right"
                    break
                elif other_choice == '4':
                    selected_position = "bottom_left"
                    break
                elif other_choice == '5':
                    selected_position = "bottom_right"
                    break
                else:
                    print("Opcion no valida. Por favor, introduce un numero del 1 al 5.")
            break
        else:
            print("Opcion principal no valida. Por favor, introduce '1' o '2'.")

    return selected_position, center_offset_x, center_offset_y

def manage_watermarks(watermarks):
    """Permite al usuario editar o borrar marcas de agua."""
    while True:
        print("\n--- Gestionar Marcas de Agua ---")
        if not watermarks:
            print("No hay marcas de agua guardadas.")
            input("Presiona Enter para continuar...")
            return

        for i, wm in enumerate(watermarks):
            print(f"{i + 1}. {wm}")

        print("\nOpciones:")
        print("A. Borrar una marca de agua")
        print("B. Volver al menu principal")

        choice = input("Introduce tu eleccion (numero para editar, A para borrar, B para volver): ").strip().lower()

        if choice == 'b':
            break
        elif choice == 'a':
            while True:
                try:
                    index_to_delete = int(input("Introduce el numero de la marca de agua a borrar: ")) - 1
                    if 0 <= index_to_delete < len(watermarks):
                        deleted_wm = watermarks.pop(index_to_delete)
                        print(f"'{deleted_wm}' ha sido borrada.")
                        save_watermarks(watermarks)
                        if not watermarks:
                            print("Todas las marcas de agua han sido borradas.")
                            break
                        print("\nMarcas de agua restantes:")
                        for i, wm in enumerate(watermarks):
                            print(f"{i + 1}. {wm}")
                        break
                    else:
                        print("Numero no valido. Intentalo de nuevo.")
                except ValueError:
                    print("Entrada no valida. Por favor, introduce un numero.")
        elif choice.isdigit():
            try:
                index_to_edit = int(choice) - 1
                if 0 <= index_to_edit < len(watermarks):
                    new_text = input(f"Introduce el nuevo texto para '{watermarks[index_to_edit]}': ")
                    if new_text.strip():
                        watermarks[index_to_edit] = new_text.strip()
                        print("Marca de agua actualizada.")
                        save_watermarks(watermarks)
                    else:
                        print("El texto no puede estar vacio.")
                    break
                else:
                    print("Numero no valido. Intentalo de nuevo.")
            except ValueError:
                print("Entrada no valida. Por favor, introduce un numero.")
        else:
            print("Opcion no valida. Intentalo de nuevo.")

def choose_directories():
    """Permite al usuario elegir las carpetas de entrada y salida."""
    user_home = os.path.expanduser('~')

    common_paths = {
        '1': os.path.join(user_home, 'Desktop'),
        '2': os.path.join(user_home, 'Downloads'),
        '3': os.path.join(user_home, 'Documents'),
        '4': os.path.join(user_home, 'Pictures')
    }

    while True:
        print("\n--- Elegir Carpetas de Entrada y Salida ---")
        print("Las imagenes de entrada estaran en 'input_images' y las de salida en 'output_images' dentro del directorio elegido.")
        print("Si no especificas un directorio, se usaran las carpetas 'input_images' y 'output_images' en el mismo lugar donde ejecutas el programa.")
        print("\nOpciones de Directorio Base:")
        print("1. Escritorio")
        print("2. Descargas")
        print("3. Documentos")
        print("4. Imagenes")
        print("5. Ingresar directorio manualmente")
        print("6. Usar directorio actual (por defecto)")

        choice = input("Introduce el numero de tu eleccion: ")

        base_dir = ""
        if choice in common_paths:
            base_dir = common_paths[choice]
            print(f"Directorio base seleccionado: {base_dir}")
        elif choice == '5':
            while True:
                print("\nEjemplo de ruta en Windows: C:\\Users\\TuUsuario\\MiCarpeta")
                print("Ejemplo de ruta en Linux/macOS: /home/tuusuario/MiCarpeta o /Users/tuusuario/MiCarpeta")
                manual_path = input("Introduce la ruta completa del directorio base: ").strip()
                if os.path.isdir(manual_path):
                    base_dir = manual_path
                    print(f"Directorio base seleccionado: {base_dir}")
                    break
                else:
                    print("Ruta no valida o no existe. Por favor, verifica la ruta y asegurate de que sea un directorio.")
        elif choice == '6':
            base_dir = os.getcwd()
            print(f"Usando directorio actual: {base_dir}")
        else:
            print("Opcion no valida. Intentalo de nuevo.")
            continue

        input_folder = os.path.join(base_dir, "input_images")
        output_folder = os.path.join(base_dir, "output_images")

        print(f"\nSe usaran:")
        print(f"Carpeta de Entrada: {input_folder}")
        print(f"Carpeta de Salida: {output_folder}")
        confirm = input("¿Es correcto? (s/n): ").strip().lower()
        if confirm == 's':
            return input_folder, output_folder
        else:
            print("Reiniciando seleccion de directorio...")


# --- Uso de ejemplo ---
if __name__ == "__main__":
    # --- Ejecutar animación de carga al inicio ---
    loading_animation()

    default_input_directory = "input_images"
    default_output_directory = "output_images"

    current_input_directory = default_input_directory
    current_output_directory = default_output_directory

    # Crear directorios por defecto si no existen al inicio del programa
    if not os.path.exists(current_input_directory):
        os.makedirs(current_input_directory)
    if not os.path.exists(current_output_directory):
        os.makedirs(current_output_directory)

    saved_watermarks = load_watermarks()

    font_name = "Poppins-Medium.ttf"
    poppins_font_url = "https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-Medium.ttf"
    my_font_path = download_font_if_not_exists(font_name, poppins_font_url)

    my_font_size = 50
    my_font_color = (255, 255, 255, 128) # Blanco, semi-transparente. Para opaco, cambia 128 a 255.
    my_stroke_width = 3
    my_stroke_fill = (0, 0, 0, 255) # Negro opaco para el trazo

    margin_x = 20
    margin_y = 20
    offset_value = 200

    while True:
        print("\n--------------------")
        print("       MENU")
        print("--------------------")
        print("1. Usar marca de agua existente [Guardadas]")
        print("2. Crear nueva marca de agua [Nueva]")
        print("3. Editar o borrar marcas de agua [Gestionar]")
        print("4. Elegir carpetas de entrada/salida [Carpetas]")
        print("5. Salir [X]")
        print("--------------------")
        print(f"(Carpetas actuales: Entrada: '{os.path.abspath(current_input_directory)}', Salida: '{os.path.abspath(current_output_directory)}')")
        print("Si no se especifica, las carpetas se crearan donde se ejecuta el programa.")
        print("--------------------")

        main_menu_choice = input("Elige una opcion: ")

        my_watermark_text = ""
        perform_watermarking = False

        if main_menu_choice == '1':
            if not saved_watermarks:
                print("No hay marcas de agua guardadas. Por favor, crea una nueva primero.")
                input("Presiona Enter para continuar...")
                continue

            print("\n--- Marcas de Agua Guardadas ---")
            for i, wm_text in enumerate(saved_watermarks):
                print(f"{i + 1}. {wm_text}")

            while True:
                try:
                    wm_index = int(input("Introduce el numero de la marca de agua a usar: ")) - 1
                    if 0 <= wm_index < len(saved_watermarks):
                        my_watermark_text = saved_watermarks[wm_index]
                        perform_watermarking = True
                        break
                    else:
                        print("Numero no valido. Intentalo de nuevo.")
                except ValueError:
                    print("Entrada no valida. Por favor, introduce un numero.")

        elif main_menu_choice == '2':
            my_watermark_text = input("Por favor, introduce el nuevo texto de la marca de agua: ")
            if not my_watermark_text.strip():
                print("El texto de la marca de agua no puede estar vacio.")
                input("Presiona Enter para continuar...")
                continue

            while True:
                save_choice = input("¿Deseas guardar esta marca de agua para uso futuro? (s/n): ").strip().lower()
                if save_choice == 's':
                    if my_watermark_text not in saved_watermarks:
                        saved_watermarks.append(my_watermark_text)
                        save_watermarks(saved_watermarks)
                        print("Marca de agua guardada exitosamente.")
                    else:
                        print("Esta marca de agua ya existe en tus guardados.")
                    break
                elif save_choice == 'n':
                    break
                else:
                    print("Opcion no valida. Por favor, introduce 's' o 'n'.")
            perform_watermarking = True

        elif main_menu_choice == '3':
            manage_watermarks(saved_watermarks)
            continue

        elif main_menu_choice == '4':
            new_input_dir, new_output_dir = choose_directories()
            current_input_directory = new_input_dir
            current_output_directory = new_output_dir

            if not os.path.exists(current_input_directory):
                os.makedirs(current_input_directory)
                print(f"Carpeta '{current_input_directory}' creada.")
            if not os.path.exists(current_output_directory):
                os.makedirs(current_output_directory)
                print(f"Carpeta '{current_output_directory}' creada.")

            input("Directorios actualizados. Presiona Enter para continuar...")
            continue

        elif main_menu_choice == '5':
            print("Saliendo del programa. ¡Hasta pronto!")
            break

        else:
            print("Opcion no valida. Por favor, elige un numero del 1 al 5.")
            input("Presiona Enter para continuar...")
            continue

        if perform_watermarking:
            selected_position, center_offset_x, center_offset_y = \
                get_user_position_choice(margin_x, margin_y, offset_value)

            print("\nIniciando proceso de marca de agua...")
            watermark_multiple_images(current_input_directory, current_output_directory,
                                      my_watermark_text, my_font_path, my_font_size, my_font_color,
                                      my_stroke_width, my_stroke_fill, selected_position, margin_x, margin_y,
                                      center_offset_x, center_offset_y)
            print(f"Imagenes con marca de agua guardadas en: {os.path.abspath(current_output_directory)}")
            input("Presiona Enter para volver al menu principal...")