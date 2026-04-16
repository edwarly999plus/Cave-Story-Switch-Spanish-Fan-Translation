import zipfile
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import re
from datetime import datetime

# --- VALIDACIONES (Para Evitar Escribir En La Versión De Steam) ---

def validar_faceanm(ruta):
    """Verifica la cabecera oficial de Switch."""
    try:
        with open(ruta, 'r', encoding='utf-8', errors='ignore') as f:
            return f.readline().strip() == "CAVE STORY FRAME HOLD COUNTS"
    except: return False

def validar_nombre_backup(nombre_carpeta):
    """Valida el formato del nombre: BACKUP_CS_YYYYMMDD_HHMMSS."""
    return re.match(r"^BACKUP_CS_\d{8}_\d{6}$", nombre_carpeta) is not None

# --- UI DE CARGA ---

class PantallaCarga(tk.Toplevel):
    def __init__(self, parent, titulo="Procesando..."):
        super().__init__(parent)
        self.title(titulo)
        self.geometry("500x200")
        self.configure(bg="#000")
        self.resizable(False, False)
        self.attributes('-topmost', True)

        self.label_accion = tk.Label(self, text="Iniciando...", fg="#ffff00", bg="#000", font=("Verdana", 9, "bold"))
        self.label_accion.pack(pady=15)

        self.progress = ttk.Progressbar(self, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        self.label_archivo = tk.Label(self, text="", fg="#00ff00", bg="#000", font=("Verdana", 7))
        self.label_archivo.pack()

    def actualizar(self, valor, accion, archivo):
        self.progress["value"] = valor
        self.label_accion["text"] = accion
        self.label_archivo["text"] = f"Actual: {archivo}"
        self.update()

# --- LÓGICA DE INSTALACIÓN ---

def proceso_instalar(path_zip, path_dest, root):
    loading = PantallaCarga(root, "Instalador Cave Story+")
    try:
        # 1. Backup: MOVER archivos en lugar de copiar
        loading.actualizar(10, "MOVIENDO ARCHIVOS ORIGINALES AL BACKUP...", "Preparando carpetas...")
        
        backup_name = f"BACKUP_CS_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        path_backup_parent = os.path.dirname(path_dest)
        path_backup_full = os.path.join(path_backup_parent, backup_name)
        
        # En lugar de copytree, usamos move. 
        # Esto 'vacia' la carpeta data original y la pone en el backup.
        shutil.move(path_dest, path_backup_full)
        
        # Crear la carpeta data de nuevo (vacía) para recibir el parche
        os.makedirs(path_dest)

        # Crear archivo de verificación dentro del backup
        with open(os.path.join(path_backup_full, "Original_Files.txt"), "w", encoding="utf-8") as f:
            f.write(f"INDICE DE SEGURIDAD - {datetime.now()}\nArchivos movidos satisfactoriamente.")

        loading.withdraw()
        confirmar = messagebox.askyesno("Backup Finalizado", 
            f"Los archivos originales se han movido a:\n{backup_name}\n\n"
            "¿Deseas proceder con la instalación del parche?")
        
        if not confirmar:
            loading.destroy()
            return
        
        loading.deiconify()

        # 2. Extracción del ZIP
        temp_dir = "temp_patch"
        if os.path.exists(temp_dir): shutil.rmtree(temp_dir)
        
        with zipfile.ZipFile(path_zip, 'r') as zr:
            miembros = [m for m in zr.namelist() if m.startswith('data/')]
            for i, m in enumerate(miembros):
                zr.extract(m, temp_dir)
                loading.actualizar(20 + (i/len(miembros)*30), "EXTRAYENDO PARCHE, NO APAGUE EL PC...", os.path.basename(m))

        # 3. Aplicar Parche
        src_data = os.path.join(temp_dir, "data")
        todos = []
        for r, d, f in os.walk(src_data):
            for file in f: todos.append(os.path.join(r, file))

        for i, f_orig in enumerate(todos):
            rel = os.path.relpath(f_orig, src_data)
            f_final = os.path.join(path_dest, rel)
            os.makedirs(os.path.dirname(f_final), exist_ok=True)
            shutil.copy2(f_orig, f_final)
            loading.actualizar(50 + (i/len(todos)*50), "INSTALANDO TRADUCCIÓN...", rel)

        shutil.rmtree(temp_dir)
        loading.destroy()
        messagebox.showinfo("Éxito", "Parche aplicado correctamente.\nArchivos originales resguardados en el Backup.")

    except PermissionError:
        if 'loading' in locals(): loading.destroy()
        messagebox.showerror("Error de Permisos", "No se pudieron mover los archivos. Asegúrate de que el juego o un editor no estén abiertos.")
    except Exception as e:
        if 'loading' in locals(): loading.destroy()
        messagebox.showerror("Error Crítico", f"Ocurrió un fallo: {e}")

# --- LÓGICA DE RESTAURACIÓN ---

def proceso_restaurar(path_backup, path_data_actual, root):
    nombre_folder = os.path.basename(os.path.normpath(path_backup))
    
    if not validar_nombre_backup(nombre_folder):
        messagebox.showerror("Error", "Nombre de carpeta de backup no válido.")
        return

    if not os.path.exists(os.path.join(path_backup, "Original_Files.txt")):
        messagebox.showerror("Error", "No se encontró el archivo 'Original_Files.txt' en el backup.")
        return

    if not messagebox.askyesno("Confirmar", "¿Borrar parche actual y restaurar originales?"):
        return

    loading = PantallaCarga(root, "Restaurando...")
    try:
        loading.actualizar(30, "BORRANDO PARCHE...", "Limpiando carpeta...")
        shutil.rmtree(path_data_actual)
        
        loading.actualizar(70, "RESTAURANDO ORIGINALES...", "Moviendo archivos de vuelta...")
        # Volvemos a mover la carpeta para que sea instantáneo
        shutil.move(path_backup, path_data_actual)
        
        # Intentar borrar el archivo de texto de control si quedó dentro
        txt_ctrl = os.path.join(path_data_actual, "Original_Files.txt")
        if os.path.exists(txt_ctrl): os.remove(txt_ctrl)
            
        loading.actualizar(100, "COMPLETADO", "Éxito")
        loading.destroy()
        messagebox.showinfo("Listo", "Juego restaurado a su estado original.")
    except Exception as e:
        if 'loading' in locals(): loading.destroy()
        messagebox.showerror("Error", str(e))

# --- INTERFAZ ---

def lanzar_instalar():
    z = filedialog.askopenfilename(title="Seleccionar Parche ZIP", filetypes=[("ZIP", "*.zip")])
    if not z: return
    d = filedialog.askdirectory(title="Seleccionar carpeta 'data' del juego")
    if not d: return
    
    # Validaciones Switch
    pb = os.path.join(d, "base")
    if not os.path.exists(os.path.join(pb, "ogg17")):
        messagebox.showerror("Error", "No es la carpeta de la versión Switch.")
        return
    if not validar_faceanm(os.path.join(pb, "faceanm.dat")):
        messagebox.showerror("Error", "faceanm.dat no válido.")
        return

    threading.Thread(target=proceso_instalar, args=(z, d, root), daemon=True).start()

def lanzar_restaurar():
    b = filedialog.askdirectory(title="Seleccionar Carpeta de Backup")
    if not b: return
    d = filedialog.askdirectory(title="Seleccionar carpeta 'data' actual")
    if not d: return
    threading.Thread(target=proceso_restaurar, args=(b, d, root), daemon=True).start()

root = tk.Tk()
root.title("Cave Story+ Switch Translation Manager")
root.geometry("450x380")
root.configure(bg="#000")

style = ttk.Style()
style.theme_use('clam')
style.configure("TProgressbar", thickness=15, background='#0000aa', bordercolor='#fff')

tk.Label(root, text="CS+ SWITCH TRANSLATION MANAGER", fg="#ffff00", bg="#000", font=("Verdana", 14, "bold")).pack(pady=30)

tk.Button(root, text="INSTALAR TRADUCCIÓN", command=lanzar_instalar, 
          bg="#0000aa", fg="#fff", font=("Verdana", 10, "bold"), width=30, pady=12).pack(pady=10)

tk.Button(root, text="RESTAURAR ORIGINALES", command=lanzar_restaurar, 
          bg="#333", fg="#fff", font=("Verdana", 10, "bold"), width=30, pady=12).pack(pady=10)

tk.Label(root, text="V1.0.", fg="#444", bg="#000", font=("Verdana", 7)).pack(side="bottom", pady=15)

root.mainloop()
