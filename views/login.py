import customtkinter as ctk
import myCustomTkinter as mctk
import utils.entidades as entidades
from DataBase.usuario_bd import usuario_bd

from utils.helpers import limpiar_ventana

def revisar_credenciales(entry_u, entry_p):
    global id_usuario_logueado, perfil
    nombre_usuario = entry_u.get()
    password = entry_p.get()
    usuario = entidades.Usuario()
    usuario.set_username(nombre_usuario)
    usuario.set_password(password)
    db = usuario_bd()
    resultado = db.HacerLogin(usuario)
    if resultado:
        id_usuario_logueado, perfil = resultado
        print(f"Intento de login - Usuario: {nombre_usuario}, Password: {password}")
    
    
    

def pantalla_login(ventana):

    limpiar_ventana(ventana)

    ctk.CTkLabel(
        ventana,
        text="Acceso al Sistema",
        font=("Arial", 28, "bold")
    ).pack(pady=(50, 20))

    frame_form = ctk.CTkFrame(
        ventana,
        width=400,
        height=300
    )

    frame_form.pack(pady=20, padx=60)
    frame_form.pack_propagate(False)

    ctk.CTkLabel(
        frame_form,
        text="Usuario:",
        font=("Arial", 14)
    ).pack(pady=(30, 5))

    # Asignamos el Entry a una variable
    entry_usuario = ctk.CTkEntry(
        frame_form,
        placeholder_text="Admin / Cobrador",
        width=250
    )
    entry_usuario.pack(pady=5)

    ctk.CTkLabel(
        frame_form,
        text="Contraseña:",
        font=("Arial", 14)
    ).pack(pady=(15, 5))

    entry_password = mctk.PasswordEntry(
        frame_form,
        placeholder_text="********",
        width=250
    )
    entry_password.pack(pady=5)

    ctk.CTkButton(
        frame_form,
        text="Iniciar Sesión",
        width=200,
        command=lambda: revisar_credenciales(entry_usuario, entry_password)
    ).pack(pady=30)
