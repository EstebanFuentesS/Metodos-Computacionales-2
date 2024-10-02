import numpy as np
import pandas as pd

def crearF(book, n):
    #Parametros
    caracteres = sorted(set("abcdefghijklmnopqrstuvwxyz .,;:?!\n"))
    unicos = np.unique([book[i:i+n] for i in range(len(book)-n)]) #Me da las combinaciones unicas de n caracteres
    ngramas = []
    for i in unicos:
        ngramas.append(str(i))
    #print(ngramas)

    #Creando DataFrame
    F = pd.DataFrame(np.zeros((len(ngramas), len(caracteres)), dtype=int), index=ngramas, columns=caracteres)

    for i in range(len(book) - n):
        posicion = book[i:i+n]
        posicion_sig = book[i+n]
        if posicion in ngramas and posicion_sig in caracteres:
        #print(posicion, posicion_sig)
            F.loc[posicion, posicion_sig] += 1

    return F