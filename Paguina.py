from Funciones import *
from Graficas import *
def procesar_datos():
    mensaje = mensaje_var.get()
    bw = int(bw_var.get())
    bps = int(bps_var.get())

    dc = Calcular_dc(mensaje)
    hz,T = Calcular_frecuencia(bps)
    n = int(Calcular_Armonicos(bw, hz))
    df = Tabla_Armonicos(n,mensaje)
    series, gt, junto = Crear_Series(df,hz,n,dc,T)
    Grafica_2D(series,root)
    Grafica_mensaje(gt,len(mensaje),root)
    Grafica_3D(junto,root)

    resultado_window = tk.Toplevel(root)
    resultado_label = tk.Label(resultado_window, text=f"Mensaje: {mensaje}\nAncho de banda: {bw}\nBits por segundo: {bps}")
    resultado_label.pack()

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario")

# Crear variables de control para los campos de entrada
mensaje_var = tk.StringVar()
bw_var = tk.StringVar()
bps_var = tk.StringVar()

# Crear etiquetas y campos de entrada
mensaje_label = tk.Label(root, text="Mensaje binario:")
mensaje_entry = tk.Entry(root, textvariable=mensaje_var)

bw_label = tk.Label(root, text="Ancho de banda:")
bw_entry = tk.Entry(root, textvariable=bw_var)

bps_label = tk.Label(root, text="Bits por segundo:")
bps_entry = tk.Entry(root, textvariable=bps_var)

# Crear botón para procesar datos
procesar_button = tk.Button(root, text="Generar Gráficos", command=procesar_datos)

# Colocar elementos en la ventana principal
mensaje_label.pack()
mensaje_entry.pack()

bw_label.pack()
bw_entry.pack()

bps_label.pack()
bps_entry.pack()

procesar_button.pack()

# Iniciar el bucle de eventos
root.mainloop()