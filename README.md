Herramienta Sencilla para Marcas de Agua en Imágenes 

Esta es una pequeña y fácil de usar aplicación que te permite añadir marcas de agua de texto a tus imágenes. Es perfecta para proteger tus fotos, añadir tu nombre o la URL de tu sitio web de forma rápida y sencilla. 

Link de descarga: https://github.com/GVPV12/BWM/releases/download/v1.0/BWMconsola.exe

Este es mi primer programa hecho en Python. 

Este programa también tiene una versión con GUI: [https://github.com/GVPV12/BWM-GUI](https://github.com/GVPV12/BWM-GUI)

![Captura2](https://github.com/user-attachments/assets/8a32f74f-de64-49d8-b505-3983f52b41e0)

![imagen_2025-06-07_221450377](https://github.com/user-attachments/assets/4882edc2-51e0-4c42-8f6d-e11e58811e6e)

## Ejemplo de Proceso realizado con éxito
![Ejemplo de Proceso realizado con exito](https://github.com/user-attachments/assets/f927ecdd-c889-441e-a941-aa11df83ac3e)

## Output
![20220605_201843 (1)](https://github.com/user-attachments/assets/7408c52a-fcdd-4e73-9c6a-fd51533f65f5) 


## ¿Qué hace BWM? (Funcionalidades Principales)

1.  **Añade Marcas de Agua de Texto:** Puedes poner cualquier texto que desees como marca de agua en tus imágenes (la fuente, el color y el tamaño no se pueden cambiar, en el programa con versión GUI se puede cambiar el tamaño). ✍️
2.  **Edita o elimina tus Marca de Agua:**
    * **Guarda:** Escribe el texto que quieras como Watermark. 
    * **Edita:** Puedes editarlo luego de guardarlo. 
    * **Elimina:** Elimina y gestiona todas las marcas de agua que has guardado a tu preferencia. 
3.  **Posición Flexible de la Marca de Agua:**
    * Puedes colocar la marca de agua en las **cuatro esquinas** (arriba/abajo, izquierda/derecha). ↖️↗️↙️↘️
    * Colocarla en el **centro exacto** de la imagen. 🎯
    * Ajustar el centro ligeramente (más a la izquierda, derecha, arriba o abajo) si lo necesitas. ➕➖
    * ¡O dejar que la aplicación elija una **posición aleatoria** por ti! 🎲
4.  **Procesa Múltiples Imágenes a la Vez:** Simplemente coloca todas tus imágenes en una carpeta de entrada y la aplicación les pondrá la marca de agua a todas. 📁➡️🏞️
5.  **Guarda y Gestiona tus Marcas de Agua:** Una vez que creas una marca de agua, puedes guardarla para usarla una y otra vez. También puedes editar o borrar las marcas de agua que ya no necesites. 💾📝🗑️
6.  **Carpetas Configurables:** Puedes elegir fácilmente dónde están tus imágenes de entrada y dónde quieres que se guarden las imágenes con marca de agua (por defecto, usa "input\_images" y "output\_images" en la misma carpeta del programa). 📂➡️🗂️
7.  **Soporte de Formatos de Imagen:** Funciona con los formatos de imagen más comunes, como **JPG, JPEG y PNG**. Todas las imágenes procesadas se guardarán en formato **JPG**. 🖼️
8.  **Inicio Claro:** Al abrir la aplicación, verás un mensaje de "Cargando..." con una pequeña animación para que sepas que el programa está trabajando y no se ha congelado. Se tardará unos 8 a 10 segundos en cargar luego de abrir la consola. ⏳✨

## ¿Cómo funciona? (¡Sencillo! ✅)

1.  **Organiza tus Imágenes:** En la carpeta donde esta el programa (`input_images`) coloca allí todas las fotos a las que quieras añadir una marca de agua. También puedes cambiar donde quieres que este esta carpeta (Descargas, documentos, etc) 🖼️➡️📁
2.  **Ejecuta el Programa:** Simplemente haz doble clic en el archivo `BWMconsola.exe`. 💻
3.  **Sigue el Menú:** El programa te guiará con un menú interactivo en la ventana de la consola (un cuadro de texto negro). Simplemente escribe el número o la letra de la opción que quieras y presiona `Enter`. ⌨️
4.  **Selecciona tu Marca de Agua:** Puedes usar una marca de agua que ya hayas guardado o crear una nueva al momento. 🏷️
5.  **Elige la Posición:** Decide dónde quieres que aparezca la marca de agua en tus fotos. 📍
6.  **¡Listo!** El programa procesará tus imágenes y las guardará en una carpeta de salida (por defecto, `output_images`). 🚀

## Opciones del Menú Principal:

Al iniciar el programa, verás estas opciones:

* **1. Usar marca de agua existente [Guardadas]:** Elige una marca de agua que ya creaste y guardaste previamente. 💾
* **2. Crear nueva marca de agua [Nueva]:** Escribe un nuevo texto para tu marca de agua. El programa te preguntará si quieres guardarla para el futuro. ➕
* **3. Editar o borrar marcas de agua [Gestionar]:** Entra a un sub-menú donde puedes ver tus marcas de agua guardadas, cambiarlas o eliminarlas. ✏️🗑️
* **4. Elegir carpetas de entrada/salida [Carpetas]:** Si no quieres usar las carpetas por defecto, aquí puedes especificar dónde están tus imágenes y dónde quieres guardarlas. 📂
* **5. Salir [X]:** Cierra la aplicación. 🚪

## Archivos compatibles
El programa ahora **"soporta" teóricamente cualquier tipo de archivo que la librería Pillow (PIL) pueda abrir como una imagen.**

### Imágenes soportadas
Pillow es una biblioteca muy potente y compatible con una amplia gama de formatos de imagen. En general, soporta los formatos de imagen más comunes y muchos otros, incluyendo:

- **Formatos populares:**
    - **JPEG / JPG** (.jpg, .jpeg, .jfif)
    - **PNG** (.png)
    - **BMP** (.bmp)
    - **GIF** (.gif)
    - **TIFF / TIF** (.tif, .tiff)
    - **WebP** (.webp)
- **Otros formatos comunes:**
    - **ICO** (Icono de Windows)
    - **PCX**
    - **PPM, PGM, PBM** (Netpbm formats)
    - **PSD** (Adobe Photoshop - soporte limitado, puede no manejar todas las capas o características avanzadas)
    - **EPS** (PostScript Encapsulado - requiere Ghostscript para renderizar)
    - **PDF** (Pillow puede leer la primera página de un PDF, pero requiere `poppler` o `Ghostscript` para renderizar PDFs de forma más robusta)
    - **OpenEXR**
    - **DDS** (DirectDraw Surface)
    - **FLI, FLC** (Autodesk Animation)
    - **SPIDER**
    - **TGA** (Truevision Targa)
    - **XBM, XPM** (X Window System bitmaps/pixmaps)

### Imágenes _no_ soportadas

A pesar de su amplia compatibilidad, Pillow tiene algunas limitaciones:

1. **Formatos de imágenes RAW de cámara:** Pillow no soporta directamente los formatos RAW de cámaras fotográficas (como .CR2, .NEF, .ARW, etc.). Para estos, necesitarías usar librerías especializadas como `rawpy` o `imageio` (que pueden usar backend de Pillow o otros) o convertirlos a un formato soportado primero.
2. **Formatos vectoriales puros:** Pillow es una librería de procesamiento de imágenes _rasterizadas_ (basadas en píxeles). No soporta formatos vectoriales puros como:
    - **SVG** (Scalable Vector Graphics): Para SVGs, necesitarías un motor de renderizado SVG (como `cairosvg` o `svglib` con `reportlab`) para rasterizar el SVG en una imagen antes de que Pillow pueda procesarlo.
    - **AI** (Adobe Illustrator): Similar a SVG, son formatos vectoriales.
    - **CDR** (CorelDRAW): También vectorial.
3. **Archivos corruptos o no estándar:** Si un archivo está corrupto o no sigue estrictamente la especificación de un formato de imagen, Pillow puede fallar al intentar abrirlo, resultando en un error.
4. **Algunos formatos muy específicos o propietarios:** Aunque cubre la mayoría, siempre puede haber formatos de imagen muy de nicho o propietarios que no estén implementados en Pillow.
5. **Archivos que no son imágenes:** Si pones un archivo de texto (`.txt`), un documento de Word (`.docx`), un ejecutable (`.exe`), o cualquier otro archivo que no sea una imagen en la carpeta de entrada, Pillow intentará abrirlo, fallará, y el script lo reportará como un "archivo no procesado como imagen" o "imagen con error". Esto es lo esperado, ya que no son imágenes válidas.

¡Espero que BWM te sea de gran utilidad! ╰(*°▽°*)╯

-----

# ENG

# Bulk Watermark Maker: Simple Image Watermarking Tool 

This is a small, easy-to-use application that allows you to add text watermarks to your images. It's perfect for protecting your photos, adding your name, or your website's URL quickly and easily. ✨

Download link: [https://github.com/GVPV12/BWM/releases/download/v1.0/BWMconsola.exe](https://github.com/GVPV12/BWM/releases/download/v1.0/BWMconsola.exe)

This is my first program made in Python. 

This program also has a version with GUI: [https://github.com/GVPV12/BWM-GUI](https://github.com/GVPV12/BWM-GUI)

![Captura2](https://github.com/user-attachments/assets/8a32f74f-de64-49d8-b505-3983f52b41e0)

![imagen_2025-06-07_221450377](https://github.com/user-attachments/assets/4882edc2-51e0-4c42-8f6d-e11e58811e6e)

## Example of successful output
![Ejemplo de Proceso realizado con exito](https://github.com/user-attachments/assets/f927ecdd-c889-441e-a941-aa11df83ac3e)

## Output
![20220605_201843 (1)](https://github.com/user-attachments/assets/7408c52a-fcdd-4e73-9c6a-fd51533f65f5) 


## What Does BWM Do? (Core Features)

1.  **Adds Text Watermarks:** You can place any text you want as a watermark on your images (the font, color, and size cannot be changed; in the GUI version, the size can be changed). ✍️
2.  **Edit or Delete Your Watermark:**
      * **Save:** Type the text you want as a Watermark. 
      * **Edit:** You can edit it after saving. 
      * **Delete:** Delete and manage all the watermarks you have saved to your preference. 
3.  **Flexible Watermark Positioning:**
      * You can place the watermark in the **four corners** (top/bottom, left/right). ↖️↗️↙️↘️
      * Place it in the **exact center** of the image. 🎯
      * Slightly offset the center (further left, right, up, or down) if needed. ➕➖
      * Or let the application choose a **random position** for you\! 🎲
4.  **Process Multiple Images at Once:** Simply place all your images in an input folder, and the application will watermark them all. 📁➡️🏞️
5.  **Save and Manage Your Watermarks:** Once you create a watermark, you can save it for future use. You can also edit or delete watermarks you no longer need. 💾📝🗑️
6.  **Configurable Folders:** You can easily choose where your input images are located and where you want to save the watermarked images (by default, it uses "input\_images" and "output\_images" in the same folder as the program). 📂➡️🗂️
7.  **Image Format Support:** It works with common image formats like **JPG, JPEG, and PNG**. All processed images will be saved in **JPG** format. 🖼️
8.  **Clear Startup:** When you open the application, you'll see a "Loading..." message with a small animation so you know the program is working and hasn't frozen. It will take about 8 to 10 seconds to load after opening the console. ⏳✨

## How Does It Work? (Simple\! ✅)

1. ** Organize your images: ** In the folder where the program is located, you will see a folder (`input_images`) put all the photos you want to add a watermark. You can also change where you want this folder (downloads, documents, etc.) 🖼️➡️📁
2.  **Run the Program:** Simply double-click the `BWMconsola.exe` file. 💻
3.  **Follow the Menu:** The program will guide you through an interactive menu in the console window (a black text box). Simply type the number or letter of your desired option and press `Enter`. ⌨️
4.  **Select Your Watermark:** You can either use a watermark you've already saved or create a new one on the spot. 🏷️
5.  **Choose the Position:** Decide where you want the watermark to appear on your photos. 📍
6.  **That's It\!** The program will process your images and save them to an output folder (by default, `output_images`). 🚀

## Main Menu Options:

When you start the program, you'll see these options:

  * **1. Use existing watermark [Saved]:** Choose a watermark you've previously created and saved. 💾
  * **2. Create new watermark [New]:** Type in new text for your watermark. The program will ask if you want to save it for future use. ➕
  * **3. Edit or delete watermarks [Manage]:** Enter a sub-menu where you can view, change, or remove your saved watermarks. ✏️🗑️
  * **4. Choose input/output folders [Folders]:** If you don't want to use the default folders, here you can specify where your images are and where you want to save them. 📂
  * **5. Exit [X]:** Close the application. 🚪

## Compatible Files

The program now **theoretically supports any file type that the Pillow (PIL) library can open as an image.**

### Supported Images

Pillow is a very powerful library compatible with a wide range of image formats. In general, it supports the most common image formats and many others, including:

  - **Popular Formats:**
      - **JPEG / JPG** (.jpg, .jpeg, .jfif)
      - **PNG** (.png)
      - **BMP** (.bmp)
      - **GIF** (.gif)
      - **TIFF / TIF** (.tif, .tiff)
      - **WebP** (.webp)
  - **Other Common Formats:**
      - **ICO** (Windows Icon)
      - **PCX**
      - **PPM, PGM, PBM** (Netpbm formats)
      - **PSD** (Adobe Photoshop - limited support, may not handle all layers or advanced features)
      - **EPS** (Encapsulated PostScript - requires Ghostscript to render)
      - **PDF** (Pillow can read the first page of a PDF, but requires `poppler` or `Ghostscript` for more robust PDF rendering)
      - **OpenEXR**
      - **DDS** (DirectDraw Surface)
      - **FLI, FLC** (Autodesk Animation)
      - **SPIDER**
      - **TGA** (Truevision Targa)
      - **XBM, XPM** (X Window System bitmaps/pixmaps)

### Unsupported Images

Despite its broad compatibility, Pillow has some limitations:

1.  **Camera RAW formats:** Pillow does not directly support camera RAW formats (such as .CR2, .NEF, .ARW, etc.). For these, you would need to use specialized libraries like `rawpy` or `imageio` (which may use Pillow's backend or others) or convert them to a supported format first.
2.  **Pure vector formats:** Pillow is a *raster image* processing library (pixel-based). It does not support pure vector formats such as:
      - **SVG** (Scalable Vector Graphics): For SVGs, you would need an SVG rendering engine (like `cairosvg` or `svglib` with `reportlab`) to rasterize the SVG into an image before Pillow can process it.
      - **AI** (Adobe Illustrator): Similar to SVG, these are vector formats.
      - **CDR** (CorelDRAW): Also vector.
3.  **Corrupt or non-standard files:** If a file is corrupt or does not strictly follow an image format specification, Pillow may fail to open it, resulting in an error.
4.  **Some very specific or proprietary formats:** While it covers most, there may always be very niche or proprietary image formats not implemented in Pillow.
5.  **Non-image files:** If you place a text file (`.txt`), a Word document (`.docx`), an executable (`.exe`), or any other non-image file in the input folder, Pillow will attempt to open it, fail, and the script will report it as an "unprocessed file" or "image with error." This is expected, as they are not valid images.

I hope BWM is useful to you\! ╰(*°▽°*)╯
