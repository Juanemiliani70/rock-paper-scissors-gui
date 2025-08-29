import tkinter as tk
from tkinter import messagebox
import random


opciones = ['piedra', 'papel', 'tijera']


def jugar(eleccion_jugador):
    eleccion_computadora = random.choice(opciones)

    if eleccion_jugador == eleccion_computadora:
        resultado = "¡Empate!"
        color = "orange"
    elif (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or \
         (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or \
         (eleccion_jugador == "tijera" and eleccion_computadora == "papel"):
        resultado = "¡Ganaste!"
        color = "green"
    else:
        resultado = "¡Perdiste!"
        color = "red"

    etiqueta_resultado.config(
        text=f"Tú: {eleccion_jugador.capitalize()}  |  PC: {eleccion_computadora.capitalize()}\n{resultado}",
        fg=color
    )

   
    respuesta = messagebox.askyesno("¿Jugar de nuevo?", "¿Querés jugar otra vez?")
    if respuesta:  
        etiqueta_resultado.config(text="", fg="white")
    else:
        ventana.quit()


ventana = tk.Tk()
ventana.title("Juego Piedra, Papel o Tijera")
ventana.geometry("400x350")
ventana.config(bg="#1e1e2e")


titulo = tk.Label(ventana, text="✊ ✋ ✌️ Piedra, Papel o Tijera", 
                  font=("Arial", 16, "bold"), fg="white", bg="#1e1e2e")
titulo.pack(pady=15)


frame_botones = tk.Frame(ventana, bg="#1e1e2e")
frame_botones.pack(pady=20)

def crear_boton(texto, color, eleccion):
    return tk.Button(frame_botones, text=texto, font=("Arial", 12, "bold"),
                     bg=color, fg="white", width=10, height=2, relief="flat",
                     activebackground="#333", command=lambda: jugar(eleccion))

btn_piedra = crear_boton("✊ Piedra", "#4CAF50", "piedra")
btn_papel = crear_boton("✋ Papel", "#2196F3", "papel")
btn_tijera = crear_boton("✌️ Tijera", "#E91E63", "tijera")

btn_piedra.grid(row=0, column=0, padx=10)
btn_papel.grid(row=0, column=1, padx=10)
btn_tijera.grid(row=0, column=2, padx=10)


etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 14, "bold"), 
                              bg="#1e1e2e", fg="white", wraplength=350, justify="center")
etiqueta_resultado.pack(pady=25)


btn_salir = tk.Button(ventana, text="Salir", font=("Arial", 12, "bold"),
                      bg="gray", fg="white", width=12, height=2, relief="flat",
                      command=ventana.quit)
btn_salir.pack(pady=10)

ventana.mainloop()
