import tkinter as tk
from tkinter import messagebox
import statistics

class NotasApp:
    def __init__(self, master):
        self.master = master
        master.title("Notas del Estudiante")
        master.geometry("300x350")
        master.resizable(False, False)

        self.labels = []
        self.entries = []

        for i in range(5):
            label = tk.Label(master, text=f"Nota {i+1}:")
            label.place(x=20, y=20 + i*30)
            entry = tk.Entry(master)
            entry.place(x=100, y=20 + i*30)
            self.labels.append(label)
            self.entries.append(entry)

        self.btn_calcular = tk.Button(master, text="Calcular", command=self.calcular)
        self.btn_calcular.place(x=40, y=190)

        self.btn_limpiar = tk.Button(master, text="Limpiar", command=self.limpiar)
        self.btn_limpiar.place(x=160, y=190)

        self.lbl_promedio = tk.Label(master, text="Promedio = ")
        self.lbl_promedio.place(x=20, y=230)

        self.lbl_desviacion = tk.Label(master, text="Desviación estándar = ")
        self.lbl_desviacion.place(x=20, y=260)

        self.lbl_mayor = tk.Label(master, text="Nota mayor = ")
        self.lbl_mayor.place(x=20, y=290)

        self.lbl_menor = tk.Label(master, text="Nota menor = ")
        self.lbl_menor.place(x=20, y=320)

    def calcular(self):
        try:
            notas = [float(entry.get()) for entry in self.entries]

            if len(notas) != 5 or any(entry.get() == "" for entry in self.entries):
                raise ValueError("Debe ingresar las 5 notas.")

            promedio = sum(notas) / len(notas)
            desviacion = (sum((x - promedio)**2 for x in notas) / len(notas))**0.5  # Poblacional
            mayor = max(notas)
            menor = min(notas)

            self.lbl_promedio.config(text=f"Promedio = {promedio:.2f}")
            self.lbl_desviacion.config(text=f"Desviación estándar = {desviacion:.2f}")
            self.lbl_mayor.config(text=f"Nota mayor = {mayor}")
            self.lbl_menor.config(text=f"Nota menor = {menor}")

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese solo números válidos en los 5 campos.")

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
        self.lbl_promedio.config(text="Promedio = ")
        self.lbl_desviacion.config(text="Desviación estándar = ")
        self.lbl_mayor.config(text="Nota mayor = ")
        self.lbl_menor.config(text="Nota menor = ")

if __name__ == "__main__":
    root = tk.Tk()
    app = NotasApp(root)
    root.mainloop()
