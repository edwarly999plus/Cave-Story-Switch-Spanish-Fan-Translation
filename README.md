# Cave Story+ (Nintendo Switch) - Traducción al Español (Fan-Translation)

<!-- Insignias -->
<p align="left">
  
  <!-- Estado de traducción (verde) -->
  <img src="https://img.shields.io/badge/Estado%20de%20traducción-45%25-brightgreen?style=for-the-badge&logo=googletranslate&logoColor=white" alt="Traducción 45%">

  <img src="https://img.shields.io/badge/Estado%20de%20traducción%20(Mods)-5%25-brightgreen?style=for-the-badge&logo=googletranslate&logoColor=white" alt="Traducción 5%">
  
  <!-- Licencia CC BY-NC-SA 4.0 (insignia personalizada) -->
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es">
    <img src="https://img.shields.io/badge/Licencia-CC%20BY--NC--SA%204.0-lightgrey?style=for-the-badge&logo=creativecommons&logoColor=white" alt="Licencia CC BY-NC-SA 4.0">
  </a>

¡Bienvenido al repositorio del parche de traducción al español para la versión de **Nintendo Switch** de Cave Story+! 

Este proyecto nace con el objetivo de traer la mejor versión del juego (con sus mejoras de calidad de vida como la escalera del Laberinto y el sistema de multi-carga de perros de Jenka) a nuestro idioma, manteniendo la esencia original y evitando errores gráficos.

---

## 🛠️ Estado del Proyecto
* **Campaña Principal:** En desarrollo (Falta pulir algunas cosas).
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
* Está **ESTRICTAMENTE PROHIBIDO** subir el código del juego como `pxm`, `pxe`, `nso`, `tbl`, `nro`, etc. (si llegara a pasar los archivos seran eliminados).

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
* **Traducción y Edición:** [Tu Nombre o Nick Aquí]

## 💬 Colaboración
Si quieres ayudar a traducir los Mods (Wind Fortress, Nemesis Challenge, etc.) o mejorar los diálogos de la campaña, ¡siéntete libre de hacer un Fork o enviar un Pull Request!
