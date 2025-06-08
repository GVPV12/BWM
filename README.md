# Bulk Watermark Maker: Herramienta Sencilla para Marcas de Agua en Imágenes 📸

¡Bienvenido a BWM en consola! 🎉 Esta es una pequeña y fácil de usar aplicación que te permite añadir marcas de agua de texto a tus imágenes. Es perfecta para proteger tus fotos, añadir tu nombre o la URL de tu sitio web de forma rápida y sencilla. ✨

Este es mi primer programa hecho en python. Este programa también tiene una versión con GUI

## ¿Qué hace BWM? (Funcionalidades Principales)

1.  **Añade Marcas de Agua de Texto:** Puedes poner cualquier texto que desees como marca de agua en tus imágenes. ✍️
2.  **Personaliza tu Marca de Agua:**
    * **Color y Transparencia:** Elige el color del texto y qué tan transparente quieres que sea. 🌈
    * **Borde del Texto:** Puedes añadir un borde alrededor del texto para que se vea más nítido. 🛡️
    * **Tamaño:** Ajusta el tamaño de la fuente para que se adapte perfectamente a tus imágenes. 📏
3.  **Posición Flexible de la Marca de Agua:**
    * Puedes colocar la marca de agua en las **cuatro esquinas** (arriba/abajo, izquierda/derecha). ↖️↗️↙️↘️
    * Colocarla en el **centro exacto** de la imagen. 🎯
    * Ajustar el centro ligeramente (más a la izquierda, derecha, arriba o abajo) si lo necesitas. ➕➖
    * ¡O dejar que la aplicación elija una **posición aleatoria** por ti! 🎲
4.  **Procesa Múltiples Imágenes a la Vez:** Simplemente coloca todas tus imágenes en una carpeta de entrada y la aplicación les pondrá la marca de agua a todas. 📁➡️🏞️
5.  **Guarda y Gestiona tus Marcas de Agua:** Una vez que creas una marca de agua, puedes guardarla para usarla una y otra vez. También puedes editar o borrar las marcas de agua que ya no necesites. 💾📝🗑️
6.  **Carpetas Configurables:** Puedes elegir fácilmente dónde están tus imágenes de entrada y dónde quieres que se guarden las imágenes con marca de agua (por defecto, usa "input\_images" y "output\_images" en la misma carpeta del programa). 📂➡️🗂️
7.  **Soporte de Formatos de Imagen:** Funciona con los formatos de imagen más comunes, como **JPG, JPEG y PNG**. Todas las imágenes procesadas se guardarán en formato **JPG**. 🖼️
8.  **Inicio Claro:** Al abrir la aplicación, verás un mensaje de "Cargando..." con una pequeña animación para que sepas que el programa está trabajando y no se ha congelado. ⏳✨

## ¿Cómo funciona? (¡Sencillo! ✅)

1.  **Organiza tus Imágenes:** Crea una carpeta (por ejemplo, `input_images`) y coloca allí todas las fotos a las que quieras añadir una marca de agua. 🖼️➡️📁
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

¡Espero que BWMconsola te sea de gran utilidad! 😊
---
