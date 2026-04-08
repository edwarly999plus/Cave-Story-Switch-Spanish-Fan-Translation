# Cave Story+ (Nintendo Switch) - Spanish Fan-Translation

<p align="left">
  <img src="https://img.shields.io/badge/Translation%20Status-56%25-brightgreen?style=for-the-badge&logo=googletranslate&logoColor=white" alt="Translation 56%">
  <img src="https://img.shields.io/badge/Mods%20Status-5%25-brightgreen?style=for-the-badge&logo=googletranslate&logoColor=white" alt="Mods 5%">
  
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
    <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=for-the-badge&logo=creativecommons&logoColor=white" alt="License CC BY-NC-SA 4.0">
  </a>
</p>

Welcome to the Spanish translation patch repository for the **Nintendo Switch** version of Cave Story+!

This project aims to bring the definitive version of the game (including QoL improvements like the Labyrinth stairs and Jenka’s multi-puppy carry system) to our language, preserving the original essence while fixing native bugs and graphical errors.

---

## 🛠️ Step 1: Install Python (Optional, but Recommended)

While you can copy files manually, **using the installer is highly recommended** to ensure a clean, error-free installation on your console.

### **Windows**
* **Quick Method:** Open a terminal (CMD or PowerShell) and type:
    ```bash
    winget install -e --id Python.Launcher
    ```
* **Other options:** [Microsoft Store](https://apps.microsoft.com/store/detail/python-313/9PJ7PRS2DGQC) or [Manual Installer](https://www.python.org/downloads/windows/).

### **macOS / Linux**
* **Mac:** [Download .pkg](https://www.python.org/ftp/python/3.13.0/python-3.13.0-macos11.pkg)
* **Linux:** `sudo apt install python3`

---

## 📥 Step 2: Installation Guide

### **Option A: Using the Installer (Safest ✅)**
1. Download and extract the `.zip` file from this repository.
2. Run `Instalador Del Parche.py`.
3. The program will automatically prepare the files for your Switch.
4. Copy the resulting folder to your SD card.

### **Option B: Manual Installation (Advanced ⚠️)**
If you prefer not to use Python, copy the `01007D4002682000` folder directly to:
`SD:/atmosphere/contents/`

*Note: Make sure to maintain the `romfs/data/` folder structure for the game to recognize the changes.*

---

## 🛠️ Project Status
* **Main Campaign:** In development (56%).
* **Mods & Extra Content:** Not translated yet (Collaborators welcome!).
* **Compatibility:** Tested on Nintendo Switch hardware and **doukutsu-rs**.

## 💻 Technical Information
* **Base Engine:** Nicalis **C++** reimplementation (Cave Story+ Version).
* **Scripting:** The `.tsc` (Text Script Cassette) files included are compatible with the Switch version's script interpreter.
* **Debugging Environment:** Native testing performed via **doukutsu-rs** (Rust-based engine) to ensure dialogue fluidity and event stability without emulation lag.
* **File Filtering:** Deep cleaning performed using *Everything* to include only modified text and visual assets, excluding untouched map (.pxm) or entity (.pxe) data.

## ⚠️ Localization Notes (Important)
Due to font rendering limitations in the Switch version, this translation follows specific rules to avoid "garbage pixels" or crashes:
* **No Accents:** Accents (á, é, í, ó, ú) have been omitted.
* **No "Ñ" Character:** Replaced by "n" or alternative wording (e.g., "pequena" or "chica").
* **Clean Graphics:** `.png` files have been manually edited and reviewed to localize UI elements like the **YES / NO** prompt boxes.

---

## 📂 Repository Structure
This repository **only contains fan-edited files**. No protected original code is distributed:
* `/data/*.tsc`: Translated event and dialogue scripts (plain text format).
* `/data/Stage/*.png`: UI elements and images with embedded text (reviewed individually).
* It is **STRICTLY FORBIDDEN** to upload game binaries or proprietary assets such as `pxm`, `pxe`, `nso`, `tbl`, or `nro` files.

---

## 🚀 Deployment
1. Ensure you own a legal copy of **Cave Story+** on your Switch.
2. Copy the contents of this repository's output folder.
3. Paste it into your SD card at the following path (replace the ID according to your region, e.g., USA/EU):
   `sdmc:/atmosphere/contents/01007D4002682000/romfs/`
4. Launch the game and enjoy.

---

## ⚖️ License & Legality

<p align="left">
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
    <img src="https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png" alt="CC BY-NC-SA Button">
  </a>
</p>

This project is distributed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)** license.
* **Free Use:** You may share and adapt the material.
* **Non-Commercial:** Sale or commercial profit from this translation is prohibited.
* **Attribution:** Credit must be given to the original translation author.
* **ShareAlike:** Derivative works must use the same license.

**Legal Disclaimer:** This is a non-profit fan project. I am not affiliated with Studio Pixel or Nicalis. This repository **DOES NOT contain the full game**, original C++ source code, or executables. The original game is required to use these files.

---

## 🤝 Credits
* **Original Developer:** [Studio Pixel](https://www.studiopixel.jp/) (Daisuke Amaya).
* **Publisher/Port:** [Nicalis, Inc.](https://www.nicalis.com/)
* **Translation & Editing:** [EdwarlyGamer999+](https://www.youtube.com/@EdwarlyGamer999plusxd) (Me).

## 💬 Contributions
If you want to help translate the Mods (Wind Fortress, Nemesis Challenge, etc.) or improve the campaign's dialogue, feel free to Fork the project or submit a Pull Request!
