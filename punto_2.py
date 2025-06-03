import tkinter as tk
from tkinter import messagebox
import math

class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0
        self.superficie = 0

    def get_volumen(self):
        return self.volumen

    def get_superficie(self):
        return self.superficie

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.calcular_volumen()
        self.calcular_superficie()

    def calcular_volumen(self):
        self.volumen = math.pi * self.radio**2 * self.altura

    def calcular_superficie(self):
        self.superficie = 2 * math.pi * self.radio * (self.radio + self.altura)

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.calcular_volumen()
        self.calcular_superficie()

    def calcular_volumen(self):
        self.volumen = (4/3) * math.pi * self.radio**3

    def calcular_superficie(self):
        self.superficie = 4 * math.pi * self.radio**2

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.calcular_volumen()
        self.calcular_superficie()

    def calcular_volumen(self):
        self.volumen = (1/3) * self.base**2 * self.altura

    def calcular_superficie(self):
        self.superficie = self.base**2 + 2 * self.base * self.apotema

class VentanaFigura:
    def __init__(self, root, figura_tipo):
        self.root = root
        self.root.title(figura_tipo)

        self.figura_tipo = figura_tipo
        self.entries = {}
        
        if figura_tipo == "Cilindro":
            campos = ["Radio", "Altura"]
        elif figura_tipo == "Esfera":
            campos = ["Radio"]
        elif figura_tipo == "Piramide":
            campos = ["Base", "Altura", "Apotema"]
        
        for i, campo in enumerate(campos):
            label = tk.Label(root, text=f"{campo} (cm):")
            label.grid(row=i, column=0)
            entry = tk.Entry(root)
            entry.grid(row=i, column=1)
            self.entries[campo] = entry
        
        self.calcular_button = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular_button.grid(row=len(campos), column=0, columnspan=2)
        
        self.volumen_label = tk.Label(root, text="Volumen (cm³): ")
        self.volumen_label.grid(row=len(campos)+1, column=0, columnspan=2)
        
        self.superficie_label = tk.Label(root, text="Superficie (cm²): ")
        self.superficie_label.grid(row=len(campos)+2, column=0, columnspan=2)
    
    def calcular(self):
        try:
            valores = {campo: float(self.entries[campo].get()) for campo in self.entries if self.entries[campo].get()}
            
            if self.figura_tipo == "Cilindro":
                obj = Cilindro(valores["Radio"], valores["Altura"])
            elif self.figura_tipo == "Esfera":
                obj = Esfera(valores["Radio"])
            elif self.figura_tipo == "Piramide":
                obj = Piramide(valores["Base"], valores["Altura"], valores["Apotema"])
            else:
                return
            
            self.volumen_label.config(text=f"Volumen (cm³): {obj.get_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm²): {obj.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Figuras")
        
        tk.Button(root, text="Cilindro", command=lambda: self.abrir_ventana("Cilindro")).grid(row=0, column=0)
        tk.Button(root, text="Esfera", command=lambda: self.abrir_ventana("Esfera")).grid(row=0, column=1)
        tk.Button(root, text="Pirámide", command=lambda: self.abrir_ventana("Piramide")).grid(row=0, column=2)
    
    def abrir_ventana(self, figura_tipo):
        nueva_ventana = tk.Toplevel(self.root)
        VentanaFigura(nueva_ventana, figura_tipo)

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()