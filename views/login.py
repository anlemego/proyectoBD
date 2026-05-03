import customtkinter as ctk
import myCustomTkinter as mctk

from utils.helpers import limpiar_ventana


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

    ctk.CTkEntry(
        frame_form,
        placeholder_text="Admin / Cobrador",
        width=250
    ).pack(pady=5)

    ctk.CTkLabel(
        frame_form,
        text="Contraseña:",
        font=("Arial", 14)
    ).pack(pady=(15, 5))

    mctk.PasswordEntry(
        frame_form,
        placeholder_text="********",
        width=250
    ).pack(pady=5)

    ctk.CTkButton(
        frame_form,
        text="Iniciar Sesión",
        width=200
    ).pack(pady=30)
