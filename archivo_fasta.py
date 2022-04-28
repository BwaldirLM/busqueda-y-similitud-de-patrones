class ArchivoFasta:
    def __init__(self, secuencias, nombre):
        self.secuencias = secuencias  
        self.nombre = nombre  
    
    @classmethod
    def desde_archivo(self, ruta):        
        file = open(ruta, 'r')
        Lines = file.readlines()
        sequences={}
        nombre=""
        for linea in Lines:
            linea=linea.strip()
            if len(linea)==0: continue
            if linea[0]=='>':
                nombre=linea
                sequences[nombre]=""
            else: sequences[nombre]+=linea 
        return ArchivoFasta(sequences, ruta.split('/')[-1])
            
                
                
        

class Secuencia:

  

    def __init__(self,):
        self.descripcion = ''
        self.cadenas = ''
        self.cadena = ''

    @staticmethod
    def convertir_cadena(cadenas) -> str:
      cad = ''
      for cadena in cadenas:
        cad += cadena[:-1]
      return cad

    @staticmethod
    def aminoacido(ac, base):
        if ac == 'U':
            return base[0]
        elif ac == 'C':
            return base[1]
        elif ac == 'A':
            return base[2]
        elif ac == 'G':
            return base[3]

    def __str__(self) -> str:
        return self.cadenas

    def transcripcion(self):
      cadena = self.convertir_cadena(self.cadenas)
      return cadena.replace('T', 'U')

    def transcripcion_inversa(self):
      cadena = self.convertir_cadena(self.cadenas)
      return cadena.replace('U', 'T')

    def traduccion(self, cadena):
      proteina = ''
      for i in range(-1, len(cadena), 3):
        if i != -1:
          ac1 = cadena[i-2]
          ac2 = cadena[i-1]
          ac3 = cadena[i]
          base2 = []
          base3 = []
          if ac1 == 'G':
            base2 = self.CODIGO_GENETICO[0]
            if ac2 == 'U':
              base3 = base2[0]
              proteina += self.aminoacido(ac3, base3)
            elif ac2 == 'C':
              base3 = base2[1]
              proteina += self.aminoacido(ac3, base3)
            elif ac2 == 'A':
              base3 = base2[2]
              proteina += self.aminoacido(ac3, base3)
            elif ac2 == 'G':
              base3 = base2[3]
              proteina += self.aminoacido(ac3, base3)
          elif ac1 == 'A':
            base2 == self.CODIGO_GENETICO[1]
            if ac2 == 'U':
              base3 = base2[0]
              proteina += self.aminoacido(ac3, base3)
            elif ac2 == 'C':
              base3 = base2[1]
              proteina += self.aminoacido(ac3, base3)
            elif ac2 == 'A':
              base3 = base2[2]
              proteina += self.aminoacido(ac3, base3)
            elif ac2 == 'G':
              base3 = base2[3]
              proteina += self.aminoacido(ac3, base3)
          elif ac1 == 'C':
            base2 == self.CODIGO_GENETICO[2]
            if ac2 == 'U':
              base3 = base2[0]
              proteina += self.aminoacido(ac3, base3)
            elif ac2 == 'C':
              base3 = base2[1]
              proteina += self.aminoacido(ac3, base3)
            elif ac2 == 'A':
              base3 = base2[2]
              proteina += self.aminoacido(ac3, base3)
            elif ac2 == 'G':
              base3 = base2[3]
              proteina += self.aminoacido(ac3, base3)
          elif ac1 == 'U':
            base2 == self.CODIGO_GENETICO[3]
            if ac2 == 'U':
              base3 = base2[0]
              proteina += self.aminoacido(ac3, base3)
            elif ac2 == 'C':
              base3 = base2[1]
              proteina += self.aminoacido(ac3, base3)
            elif ac2 == 'A':
              base3 = base2[2]
              proteina += self.aminoacido(ac3, base3)
            elif ac2 == 'G':
              base3 = base2[3]
              proteina += self.aminoacido(ac3, base3)
      return proteina

