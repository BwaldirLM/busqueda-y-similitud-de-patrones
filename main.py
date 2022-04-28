import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from boyer_moore import BoyerMoore as bm
from similitud import *
import kmp

from archivo_fasta import ArchivoFasta

archivos_fasta = []

class Ventana(tk.Tk):

    resultados = """Resultados de simiitud:
    Hamming:
    Levenshtein:
    n gramas:
    Jaro:   
    Ventana Deslizante:
     """

    def __init__(self):
        super().__init__()
        self.title('Similitud y busqueda de patrones')
        self.geometry('960x620')
        self.resizable(False, False)
        self.config(bg = '#f2f2f2')
        #self.iconbitmap('icono.ico')
       
        self.cargar_archivo_btn = ttk.Button(self, text = 'Cargar archivo', command = self.cargar_archivo)
        self.cargar_archivo_btn.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        self.lbl_1 = ttk.Label(self, text = 'Seleccione un archivo', font=('Arial', 10))
        self.lbl_1.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.combo = ttk.Combobox(self, values = [], state = 'readonly')
        self.combo.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.btn = ttk.Button(self, text = 'Buscar', command = self.selected)
        self.btn.grid(row = 1, column = 2, padx = 10, pady = 10)
        
        self.similitud_lbl = ttk.Label(self, text = 'Similitud de secuencias', font=('Arial', 12, 'bold'))
        self.similitud_lbl.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.secuencias_listbx = tk.Listbox(self, width = 50, height = 10, selectmode = 'extended')
        self.secuencias_listbx.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.similitud_result_lbl = ttk.Label(self, text = self.resultados, font=('Arial', 10))
        self.similitud_result_lbl.grid(row = 3, column = 1, padx = 10, pady = 10)
        self.selec_similitud_lbl = ttk.Label(self, text = 'Seleccione dos secuencia', font=('Arial', 10))
        self.selec_similitud_lbl.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.similitud_btn = ttk.Button(self, text = 'Calcular similitud', command=self.calcular_similitud)
        self.similitud_btn.grid(row = 4, column = 1, padx = 10, pady = 10)



        self.buscar_patron_lbl = ttk.Label(self, text = 'Busqueda de patrones',font=('Arial', 12, 'bold'))
        self.buscar_patron_lbl.grid(row = 5, column = 0, padx = 10, pady = 10)
        self.secuencia_lbl = ttk.Label(self, text = 'Selecionar secuencia', font=('Arial', 10, ))
        self.secuencia_lbl.grid(row = 6, column = 0, padx = 5, pady = 5)
        self.secuencia_combo = ttk.Combobox(self, values = [], state = 'readonly')
        self.secuencia_combo.grid(row = 6, column = 1, padx = 10, pady = 10)
        self.patron_lbl = ttk.Label(self, text = 'Ingrese patron', font=('Arial', 10, ))
        self.patron_lbl.grid(row = 6, column = 2, padx = 5, pady = 5)
        self.patron_txt = ttk.Entry(self, width = 20)
        self.patron_txt.grid(row = 6, column = 3, padx = 10, pady = 10)
        
        self.buscar_patron_btn = ttk.Button(self, text = 'Buscar patron', command = self.buscar_patron_bm)
        self.buscar_patron_btn.grid(row = 6, column = 4, padx = 10, pady = 10)
        self.metod_lbl = ttk.Label(self, text = 'Metodo de busqueda: ', font=('Arial', 10, ))
        self.metod_lbl.grid(row = 7, column = 0, padx = 10, pady = 10)
        self.busqueda_cmb = ttk.Combobox(self, values = ['Boyer Moore', 'kmp'], state = 'readonly')
        self.busqueda_cmb.grid(row = 7, column = 1, padx = 10, pady = 10)
        self.resultado_busqueda_lbl = ttk.Label(self, text = 'Resultado de la busqueda: ', font=('Arial', 10, ))
        self.resultado_busqueda_lbl.grid(row = 7, column = 2, padx = 10, pady = 10)

    def calcular_similitud(self):
        if len(self.secuencias_listbx.curselection()) == 2:
            secuencia_1 = self.secuencias_listbx.get(self.secuencias_listbx.curselection()[0])
            secuencia_2 = self.secuencias_listbx.get(self.secuencias_listbx.curselection()[1])
            hamming = Hamming(secuencia_1, secuencia_2)
            levenshtein = Levenshtein(secuencia_1, secuencia_2)
            n_gramas = N_Gramas(secuencia_1, secuencia_2, 122)
            jaro = Jaro(secuencia_1, secuencia_2)
            ventana = ventana_deslizante(secuencia_1, secuencia_2, 3, 2)
            self.resultados = 'Hamming: ' + str(hamming) + '\n' + 'Levenshtein: ' + str(levenshtein) + '\n' + 'N-Gramas: ' + str(n_gramas) + '\n' + 'Jaro: ' + str(jaro) + '\n' + 'Ventana: ' + str(ventana)
            self.similitud_result_lbl.config(text = self.resultados)
        else:
            self.similitud_result_lbl.config(text = 'Seleccione dos secuencia')

    def buscar_patron_bm(self):
        patron = self.patron_txt.get().upper()
        secuencia = self.secuencia_combo.get()
        metodo = self.busqueda_cmb.current()
        #resultado = None
        if metodo == 0:
            busqueda = bm(patron, secuencia)
            resultado = len(busqueda.buscar())
        elif metodo == 1:
            resultado = kmp.KmpPatternSearch(patron, secuencia)
        
        
        self.resultado_busqueda_lbl.config(text = 'Resultado de la busqueda: ' + str(resultado))
        
        

    def selected(self):
        selected = self.combo.current()
        self.secuencia_combo.config(values = [secuencia for secuencia in archivos_fasta[selected].secuencias.values()])
        sec = [secuencia for secuencia in archivos_fasta[selected].secuencias.values()]
        self.secuencias_listbx.insert(tk.END, *sec)
    
   

    def cargar_archivo(self, archivos = archivos_fasta):
        archivo = fd.askopenfilename(filetypes=[('Archivos FASTA', '*.fasta')])
        archivos.append(ArchivoFasta.desde_archivo(archivo))
        self.combo.config(values = [archivo.nombre for archivo in archivos])
        for archivo in archivos_fasta:
            print(archivo.nombre)


if __name__ == '__main__':
    ventana = Ventana()
    ventana.mainloop()
    

"""
window = tk.Tk()
window.title("Proyecto")
window.geometry("400x400")

cargar_archivo_lbl = ttk.Label(window, text="Cargar archivo:")
cargar_archivo_lbl.place(x=10, y=10)

cargar_archivo_btn = ttk.Button(window, text="...", width=5, command=lambda: cargar_archivo())
cargar_archivo_btn.place(x=110, y=10)

for i in range(len(archivos_fasta)):
    archivo_lbl = ttk.Label(window, text=archivos_fasta[i].nombre)
    archivo_lbl.place(x=10, y=50 + i * 30)

#for i in range(len(archivos_fasta)):
 #   archivo_lbl = ttk.Label(window, text=archivos_fasta[i].descripcion)
  #  archivo_lbl.place(x=10, y=50 + (i * 20))






window.mainloop()



"""