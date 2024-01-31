import plotly.graph_objects as go
import tkinter as tk
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def mostrar_grafico_emergente(root,img_base64):
    # Crear una nueva ventana para mostrar la imagen
    ventana_emergente = tk.Toplevel(root)
    ventana_emergente.title('Gráfico 2D')

    # Decodificar la imagen base64
    img_data = base64.b64decode(img_base64)

    # Crear un objeto PhotoImage a partir de la imagen
    img = tk.PhotoImage(data=img_data)

    # Mostrar la imagen en un widget Label
    label_imagen = tk.Label(ventana_emergente, image=img)
    label_imagen.image = img  # Mantener una referencia para evitar que se elimine la imagen
    label_imagen.pack()
def Grafica_2D(df,root):
    # Crear una figura y ejes
    fig, ax = plt.subplots(figsize=(10, 6))
    # Graficar tus datos
    df.plot(ax=ax)
    # Título de la gráfica
    plt.title('Series')
    # Ajustar el diseño
    plt.tight_layout()
    # Nombres ejes
    ax.set_xlabel('Marcas')
    ax.set_ylabel('Hz')
    # Ajustar el margen inferior para dar espacio a los títulos de los ejes
    plt.subplots_adjust(bottom=0.2, top=0.9)

    # Convertir el gráfico a una imagen en formato base64
    img_data = BytesIO()
    fig.savefig(img_data, format='png')
    img_data.seek(0)
    img_base64 = base64.b64encode(img_data.getvalue()).decode('utf-8')

    # Mostrar la gráfica en una ventana emergente
    mostrar_grafico_emergente(root,img_base64)


def Grafica_mensaje(df,l,root):
    # Crear una figura y ejes
    fig, ax = plt.subplots(figsize=(10, 6))
    # Graficar tus datos
    df.plot(ax=ax)
    # Título de la gráfica
    plt.title('Mensaje')

    tiempo_flotante = 1.0 / l  # Define el tiempo flotante deseado
    n_puntos = int(100 * tiempo_flotante)  # Calcula el número de puntos correspondientes
    for i in range(0, 100, n_puntos):
        ax.axvline(x=i, linestyle='--', color='gray', alpha=0.5)

    # Ajustar el diseño
    plt.tight_layout()
    # Nombres ejes
    ax.set_xlabel('Marcas')
    ax.set_ylabel('Hz')
    # Ajustar el margen inferior para dar espacio a los títulos de los ejes
    plt.subplots_adjust(bottom=0.2, top=0.9)
    # Convertir el gráfico a una imagen en format
    # o base64
    img_data = BytesIO()
    fig.savefig(img_data, format='png')
    img_data.seek(0)
    img_base64 = base64.b64encode(img_data.getvalue()).decode('utf-8')

    # Mostrar la gráfica en una ventana emergente
    mostrar_grafico_emergente(root,img_base64)

def Grafica_3D(df,root):
    # Crear gráfico 3D
    fig = go.Figure()

    # Ajustar el tamaño y la forma de los puntos
    marker_size = 1
    marker_line_width = 4

    # Agregar cada serie como una línea en el gráfico 3D
    for i, columna in enumerate(df.columns):
        fig.add_trace(go.Scatter3d(
            x=[i] * len(df),  # Armonico
            y=df.index,  # Tiempo
            z=df[columna],  # Valor
            mode='lines+markers',
            name=columna,
            line=dict(width=marker_line_width),
            marker=dict(size=marker_size)
        ))

    # Configuración del diseño
    fig.update_layout(scene=dict(
        xaxis=dict(title='', autorange='reversed'),  # Invertir el eje x
        yaxis_title='Marcas',
        zaxis_title='Hz'
    ))

    # Mostrar el gráfico
    fig.show()