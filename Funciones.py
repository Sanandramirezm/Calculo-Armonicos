import pandas as pd
import numpy as np

def Calcular_dc(mensaje):
    count = 0
    for i in mensaje:
        if(i == "1"):
            count = count + 1
    return count/len(mensaje)
def Calcular_frecuencia(n):
    T = 8/n
    frecuencia = 1/T
    return frecuencia, T
def Calcular_Armonicos(Bw, Hz):
    return (Bw//Hz)

def calcular_an(x, mensaje):
    PI = np.pi
    resultado = 0.0
    for i, bit in enumerate(mensaje):
        if bit == '1':
            resultado = resultado + ((-1 / (PI * x)) * (np.cos(2 * PI * x * ((i + 1)/len(mensaje))) - np.cos(2 * PI * x * (i/len(mensaje)))))
    return resultado
def calcular_bn(x,mensaje):
    PI = np.pi
    resultado = 0.0
    for i, bit in enumerate(mensaje):
        if bit == '1':
            resultado = resultado + ((1 / (PI * x)) * (np.sin(2 * PI * x * ((i + 1)/len(mensaje))) - np.sin(2 * PI * x * (i/len(mensaje)))))
    return resultado

def calcular_cn_teta(an, bn):
    cn = np.sqrt(an ** 2 + bn ** 2)
    teta = np.arctan2(bn,an)
    return cn, teta

def Tabla_Armonicos(n,mensaje):
    elementos = list(range(1, n + 1))

    # Calcula an y bn para cada elemento de la lista
    an = [calcular_an(x,mensaje) for x in elementos]
    bn = [calcular_bn(x,mensaje) for x in elementos]

    # Calcula cn y teta para cada elemento
    cn, teta = zip(*[calcular_cn_teta(a, b) for a, b in zip(an, bn)])

    # Crea el DataFrame con los resultados
    df = pd.DataFrame({
        'N': elementos,
        'an': an,
        'bn': bn,
        'cn': cn,
        'teta': teta
    })
    return df


def Calcular_gn(df, f, t, j):
    PI = np.pi
    resultado = (df['cn'][j] * np.sin(2 * PI * df['N'][j] * t * f + df['teta'][j]))
    return resultado


def Crear_Series(df, hz, n,dc,T):
    # Lista para acumular los resultados de cada iteración
    resultados = []
    gt = []
    junto = []
    p = T / 99 if T != 0 else 0
    tiempo = np.arange(0, T + p, p)
    for i in tiempo:
        gn = [Calcular_gn(df, hz, i, j) for j in range(n)]
        j = [Calcular_gn(df, hz, i, j) for j in range(n)]
        g = dc + sum(gn)
        gt.append(g)
        resultados.append(gn)
        j.insert(0,g)
        junto.append(j)

    # Crea el DataFrame al final del bucle
    df_resultado = pd.DataFrame(resultados)
    df_sum = pd.DataFrame(gt)
    df_junto = pd.DataFrame(junto)

    # Asigna nombres a las columnas
    column_names = [f'Armonico {i + 1}' for i in range(len(df_resultado.columns))]
    df_resultado.columns = column_names
    df_sum.columns = [f'g(t)']
    column_names.insert(0,'Mensaje')
    df_junto.columns = column_names

    return df_resultado, df_sum, df_junto