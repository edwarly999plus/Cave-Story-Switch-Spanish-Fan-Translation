# <p align="center"> Cave Story+ (Nintendo Switch) - Traducción al Español

<p align="center">
  <img width="256" height="256" alt="csnssptlogo" src="https://github.com/user-attachments/assets/082a78cb-6e1b-4000-8b36-5262d70fc5d4" />
</p>

<p align="center">
  <b>Cambiar idioma / Change language / 言語を選択:</b><br>
  Español 🇪🇸 | <a href="Readme_Langs/README_ENG.md">English 🇺🇸</a> | <a href="Readme_Langs/README_JP.md">日本語 🇯🇵</a>
</p>

<!-- Insignias -->
<p align="center">
  
  <!-- Estado de traducción (verde) -->
  <img src="https://img.shields.io/badge/Estado%20de%20traducción-100%25-brightgreen?style=for-the-badge&logo=googletranslate&logoColor=white" alt="Traducción 100%">

  <img src="https://img.shields.io/badge/Estado%20de%20traducción%20(Mods)-5%25-brightgreen?style=for-the-badge&logo=googletranslate&logoColor=white" alt="Traducción 5%">
  
  <!-- Licencia CC BY-NC-SA 4.0 (insignia personalizada) -->
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es">
    <img src="https://img.shields.io/badge/Licencia-CC%20BY--NC--SA%204.0-lightgrey?style=for-the-badge&logo=creativecommons&logoColor=white" alt="Licencia CC BY-NC-SA 4.0">
  </a>

<p align="center">
  <a href="https://github.com/edwarly999plus/Cave-Story-Switch-Spanish-Fan-Translation/releases/latest">
  <a href="https://github.com/edwarly999plus/Cave-Story-Switch-Spanish-Fan-Translation/releases/latest">
    <img src="https://img.shields.io/badge/DESCARGAR_PARCHE_AQUÍ-¡ÚLTIMA_VERSIÓN!-orange?style=for-the-badge&logo=github" alt="Descargar Parche">
  </a>
  <br>
  <em>(Haz clic arriba para ir a la sección de descargas / Click above to go to the download section)</em>
</p>

## 🔨 Sobre El Proyecto

¡Bienvenido al repositorio del parche de traducción al español para la versión de **Nintendo Switch** de Cave Story+! 

Este proyecto nace con el objetivo de traer la mejor versión del juego (con sus mejoras de calidad de vida como la escalera del Laberinto y el sistema de multi-carga de perros de Jenka) a nuestro idioma, manteniendo la esencia original y evitando errores gráficos.

### 1. Menús e Interfaz
<p align="left">
  <img width="852" height="477" alt="Comandos principales en español" src="https://github.com/user-attachments/assets/c7e0ea81-faf5-4932-9dd8-65bf11ecea7f" />
</p>

*Edición de botones SÍ/NO y menús de sistema para evitar errores gráficos.*

---

### 2. Inventario y Objetos
<p align="left">
  <img width="848" height="476" alt="Inventario en español" src="https://github.com/user-attachments/assets/441baf49-33f0-4960-944b-56f49426042d" />
</p>

*Descripciones de armas y objetos clave localizadas.*

---

### 3. Diálogos y Cinemáticas
<p align="left">
  <img width="853" height="475" alt="Corredor De Huevos 2" src="https://github.com/user-attachments/assets/4b0f70b0-8c04-4a55-be20-8fa16ce96243" />

<img width="853" height="474" alt="Kazuma" src="https://github.com/user-attachments/assets/abd6f80e-bd68-475b-b35d-eeb80f2d6798" />
</p>

<img width="847" height="472" alt="image" src="https://github.com/user-attachments/assets/e29dc171-ed8b-4216-b3df-85829ac9ea16" />


*Textos adaptados para una lectura fluida, respetando la personalidad de cada personaje.*

---

## 🛠️ Paso 1: Instalar Python (Opcional, pero Recomendado)

Aunque puedes copiar los archivos manualmente, **se recomienda encarecidamente usar el instalador** para asegurar una instalación limpia y sin errores en tu consola.

### **Windows**
* **Método Rápido:** Abre una terminal (CMD o PowerShell) y escribe:
    ```bash
    winget install -e --id Python.Launcher
    ```
* **Otras opciones:** [Microsoft Store](https://apps.microsoft.com/detail/9pnrbtzxmb4z?hl=en-US&gl=US) o [Instalador Manual](https://www.python.org/downloads/windows/).

### **macOS / Linux**
* **Mac:** [Descargar .pkg](https://www.python.org/ftp/python/3.13.0/python-3.13.0-macos11.pkg)
* **Linux:** `sudo apt install python3`

---

## 📥 Paso 2: Cómo Instalar el Parche

### **Opción A: Usando el Instalador (Más Seguro ✅)**
1. Descarga y extrae el archivo `.zip` del repositorio.
2. Ejecuta `Instalador Del Parche.py`.
3. El programa preparará los archivos automáticamente para tu Switch.
4. Copia la carpeta resultante en tu SD.

### **Opción B: Instalación Manual (Avanzado ⚠️)**
Si prefieres no usar Python, puedes copiar la carpeta `01007D4002682000` directamente en:
`SD:/atmosphere/contents/`

*Nota: Asegúrate de respetar la estructura de carpetas `romfs/data/` para que el juego reconozca los cambios.*

---
  
## 🛠️ Estado del Proyecto
* **Campaña Principal:** En desarrollo (Todo el juego principal traducido).
* **Mods y Contenido Extra:** No traducidos (¡Se buscan colaboradores!).
* **Compatibilidad:** Probado en Nintendo Switch y doukutsu-rs.

## 💻 Información Técnica
* **Motor Base:** Reimplementación de Nicalis en **C++** (Versión Cave Story+).
* **Scripting:** Los archivos `.tsc` (Text Script Cassette) contenidos aquí son compatibles con el intérprete de scripts de la versión de Switch.
* **Entorno de Debugging:** Testeo nativo realizado mediante **doukutsu-rs** (motor en Rust) para garantizar la fluidez de los diálogos y la estabilidad de los eventos sin lag de emulación.
* **Filtrado de Archivos:** Se ha realizado una limpieza profunda mediante *Everything* para incluir únicamente archivos de texto y recursos visuales, eliminando datos de mapas (.pxm) o entidades (.pxe) no modificados.

## ⚠️ Notas de Localización (Importante)
Debido a limitaciones en el renderizado de fuentes de la versión de Switch, esta traducción sigue estas reglas para evitar "píxeles basura" o crashes:
* **Sin Acentos:** Se han omitido los acentos (á, é, í, ó, ú).
* **Sin letra Ñ:** Sustituida por "n" o palabras alternativas (ej. "pequena" o "chica").
* **Gráficos Limpios:** Se han editado archivos `.png` mediante revisión individual para localizar opciones de menú como el cuadro de **SÍ / NO**.

---

## 📂 Estructura del Repositorio
Este repositorio **solo contiene archivos editados por fans**. No se distribuye ninguna parte protegida del código original:
* `/data/*.tsc`: Scripts de eventos y diálogos traducidos (formato de texto plano).
* `/data/Stage/*.png`: Elementos de interfaz y diálogos incrustados en imágenes (revisados uno a uno).
* `/data_base` Archivos de referencia en inglés NO TOCAR
* Está **ESTRICTAMENTE PROHIBIDO** subir el código del juego como `pxm`, `pxe`, `nso`, `tbl`, `nro`, etc. (si llegara a pasar los archivos seran eliminados).

---


### 🛠️ Reglas de Contribución y Seguridad (CODEOWNERS)

Para garantizar la estabilidad de la traducción y evitar errores críticos en el motor del juego (Switch), este repositorio cuenta con reglas estrictas de protección de ramas:

#### 1. 🛡️ Protección de Integridad (Archivos `.tsc`)
* **Mecánicas Intactas:** Está terminantemente prohibido alterar, mover o eliminar cualquier comando de lógica del juego. Esto incluye, pero no se limita a: `<FLJ`, `<EVE`, `<TRA`, `<ANP`, `<GIT`, `<IT+`, `<IT-`, `<ML+`.
* **Solo Traducción:** Las contribuciones deben limitarse exclusivamente al texto contenido dentro de las etiquetas `<MSG>`. Cualquier cambio fuera de estas etiquetas resultará en el rechazo inmediato del Pull Request.

#### 2. 🗂️ Estructura de Carpetas
* **`data/` (Principal):** Es la carpeta de trabajo donde se aplica la traducción al español.
* **`data_base/` (Backup):** Contiene los archivos originales en inglés. **NO SE DEBE EDITAR**. Esta carpeta funciona como punto de referencia técnica para comparar y reparar scripts dañados.

#### 3. 🔐 Flujo de Revisión (Code Owners)
* **Revisión Obligatoria:** El usuario **@edwarly999plus** ha sido configurado como **Code Owner** de las carpetas de datos.
* **Aprobación Manual:** Ningún cambio (Pull Request) será integrado a la rama principal sin la revisión y aprobación manual del dueño del proyecto. Esto previene la vandalización de scripts o la introducción de bugs que crasheen el juego.

#### 4. 📝 Formato de Texto
* Se debe respetar el límite de líneas de los cuadros de texto originales (31-36 Max.) para evitar que el texto se corte en la pantalla de la consola.
* **IMPORTANTE:** No usar tildes ni eñes en los archivos `.tsc` para garantizar compatibilidad total con el motor de la consola y evitar caracteres extraños.

---

## 🚀 Instalación
1. Asegúrate de tener una copia legal de **Cave Story+** en tu Switch.
2. Copia el contenido de la carpeta de este repositorio.
3. Pégalo en tu tarjeta SD en la siguiente ruta (sustituye el ID según la versión que tengas, ej (USA)(EU)):
   `sdmc:/atmosphere/contents/01007D4002682000/romfs/`
4. Inicia el juego y disfruta.

---

## ⚖️ Licencia y Legalidad   

<p align="left">
  <!-- Botón oficial de Creative Commons -->
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es">
    <img src="https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png" alt="Botón CC BY-NC-SA">
  </a>
</p>

Este proyecto se distribuye bajo la licencia **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.
* **Uso libre:** Puedes compartir y adaptar el material.
* **No Comercial:** No se permite la venta ni lucro derivado de esta traducción.
* **Créditos:** Se debe dar crédito al autor original de la traducción.
* **Compartir Igual:** Las obras derivadas deben usar esta misma licencia.

**Aviso Legal:** Este es un proyecto de fans sin fines de lucro. No estoy afiliado a Studio Pixel ni a Nicalis. Este repositorio **NO contiene el juego completo**, código fuente original de C++, archivos `.nso`, `.nro` ni ejecutables. Se requiere el juego original para utilizar estos archivos.

---

## 🤝 Créditos
* **Desarrollador Original:** [Studio Pixel](https://www.studiopixel.jp/) (Daisuke Amaya).
* **Editor/Port:** [Nicalis, Inc.](https://www.nicalis.com/)
* **Traducción y Edición:** [EdwarlyGamer999+](https://www.youtube.com/@EdwarlyGamer999plusxd) (Yo).

---

  
## 👥 Créditos de Colaboradores

Este mod es un esfuerzo comunitario. Los nombres que aparecen en los créditos finales del juego son:

*  👑 **EdwarlyGamer999+ (Admin)** - Traducciones al Español de la campaña Principal y Programación TSC.
* **LAIB** - Traducciones al Español de Curly Story (En Proceso...).


> **Nota para colaboradores:** Si deseas contribuir, puedes enviar un Pull Request. ¡Todas las contribuciones aceptadas serán añadidas a los créditos dentro del juego!

<div align= "center">
  
## **¡GRACIAS COLABORADORES!** 

<p align= "center">

<img width="64" height="64" alt="image" src="https://github.com/user-attachments/assets/d8ec7815-4705-471a-954e-8ca856d51fa4" /> 
<img width="64" height="64" alt="LAIB" src="https://github.com/user-attachments/assets/c698b57f-8a78-4ce9-9215-7af10f3ce85b" />

---

<div align= "left">

## 💬 Colaboración
Si quieres ayudar a traducir los Mods (Wind Fortress, Nemesis Challenge, etc.) o mejorar los diálogos de la campaña, ¡siéntete libre de hacer un Fork o enviar un Pull Request!

Para más info visita este [thread](https://forum.cavestory.org/threads/cave-story-switch-spanish-translation.18209/)
