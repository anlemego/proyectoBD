import customtkinter as ctk
from utils.helpers import limpiar_ventana

def pantalla_pagar_servicio(ventana):
    try:
        limpiar_ventana(ventana)
    except:
        pass

    # ---------------- GRID PRINCIPAL ----------------
    ventana.grid_rowconfigure(0, weight=1)
    ventana.grid_rowconfigure(1, weight=0)
    ventana.grid_rowconfigure(2, weight=3)
    ventana.grid_rowconfigure(3, weight=1)
    ventana.grid_columnconfigure(0, weight=1)

    # ---------------- HEADER ----------------
    frame_top = ctk.CTkFrame(ventana, fg_color="transparent")
    frame_top.grid(row=0, column=0,sticky="ns")

    frame_top.grid_columnconfigure((0, 1, 2), weight=1)

    titulo = ctk.CTkLabel(
        frame_top,
        text="Pagar servicio",
        font=ctk.CTkFont(size=24, weight="bold")
    )
    titulo.grid(row=0, column=0, columnspan=3, pady=(10, 15),sticky="n")

    lbl_id = ctk.CTkLabel(frame_top, text="ID servicio:")
    lbl_id.grid(row=1, column=0, sticky="e", padx=5)

    entry_buscar = ctk.CTkEntry(frame_top, width=200)
    entry_buscar.grid(row=1, column=1, padx=5)

    btn_buscar = ctk.CTkButton(frame_top, text="buscar", width=100)
    btn_buscar.grid(row=1, column=2, padx=5)

    # ---------------- FORMULARIO CENTRAL ----------------
    frame_form = ctk.CTkFrame(ventana)
    frame_form.grid(row=2, column=0)

    campos = [
        "ID servicio:",
        "vehículo:",
        "servicio:",
        "duración:",
        "Total a pagar:"
    ]

    for i in range(len(campos)):
        frame_form.grid_rowconfigure(i, weight=1)

    frame_form.grid_columnconfigure(1, weight=1)

    entries = []

    for i, texto in enumerate(campos):
        lbl = ctk.CTkLabel(frame_form, text=texto)
        lbl.grid(row=i, column=0, padx=10, pady=6, sticky="e")

        entry = ctk.CTkEntry(frame_form, width=300)
        entry.grid(row=i, column=1, padx=10, pady=6)
        entries.append(entry)

    # ---------------- BOTONES INFERIORES ----------------
    frame_bottom = ctk.CTkFrame(ventana, fg_color="transparent")
    frame_bottom.grid(row=3, column=0, sticky="se", padx=20, pady=20)

    btn_cancelar = ctk.CTkButton(frame_bottom, text="cancelar", width=120)
    btn_cancelar.pack(side="left", padx=10)

    btn_pagar = ctk.CTkButton(frame_bottom, text="pagar", width=120)
    btn_pagar.pack(side="left", padx=10)