class BoyerMoore:
    def __init__(self, patron, secuencia):
        self.patron = patron
        self.secuencia = secuencia
        self.tabla_sufijo_malo = self.crear_tabla_sufijo_malo()
        self.tabla_sufijo_bueno = self.crear_tabla_sufijo_bueno()

    def crear_tabla_sufijo_malo(self):
        claves = ''
        valores = []
        for i in range(len(self.patron)):
            if self.patron[i] not in claves:
                claves += self.patron[i]
                valores.append(len(self.patron) - i - 1)
            else:
                valores[claves.index(self.patron[i])] = len(self.patron) - i - 1
        sufijos = dict(zip(claves, valores))
        sufijos['otros'] = len(self.patron)
    
        return sufijos

    def valor_indice(self, patron, i, a):
        if len(patron[i+1+a:]) == 1 and patron[i+1+a:] not in patron[:i]:
            return len(patron)
        else:
            if patron[i+1+a:] in patron[:i]:
                return len(patron)-patron.index(patron[i+1+a:])-1
            else:
                return self.valor_indice(patron,i,a-1)


    def crear_tabla_sufijo_bueno(self):
        
        sufijo = list(self.patron)
        valores = []
        for i in range(len(self.patron)-1,-1,-1):
            if len(valores) == 0:
                valores.append('-')
            else:                
                v = self.valor_indice(self.patron,i,0)
                valores.insert(0,v)
        return valores
            

    def buscar(self):
        indice = 0
        indices = []
        while indice <= len(self.secuencia) - len(self.patron):
            i = len(self.patron) - 1
            bueno = False
            while i >= 0:
                if self.patron[i] == self.secuencia[i + indice]:
                    i -= 1
                    bueno = True
                else:
                    if bueno:
                        indice += self.tabla_sufijo_bueno[i]
                    else:
                        if self.secuencia[i + indice] in self.patron:
                            indice += self.tabla_sufijo_malo[self.secuencia[i+indice]]
                        else:
                            indice += self.tabla_sufijo_malo['otros']
                    break
            if i == -1:
                indices.append(indice)
                indice+=len(self.patron)
        return indices
