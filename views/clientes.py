import customtkinter as ctk
from CTkTable import CTkTable

from utils.helpers import limpiar_ventana

def pantalla_clientes(ventana):
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

    # ---------------- TOP (TITULO + BUSQUEDA) ----------------
    frame_top = ctk.CTkFrame(ventana, fg_color="transparent")
    frame_top.grid(row=0, column=0,sticky="ns")

    frame_top.grid_columnconfigure((0,1,2), weight=1)

    titulo = ctk.CTkLabel(
        frame_top,
        text="clientes",
        font=ctk.CTkFont(size=24, weight="bold")
    )
    titulo.grid(row=0, column=0, columnspan=3, pady=(10, 15), sticky="n")

    lbl_id = ctk.CTkLabel(frame_top, text="Id:")
    lbl_id.grid(row=1, column=0, sticky="e", padx=5)

    entry_id = ctk.CTkEntry(frame_top, width=200)
    entry_id.grid(row=1, column=1, padx=5)

    btn_buscar = ctk.CTkButton(frame_top, text="buscar", width=100)
    btn_buscar.grid(row=1, column=2, padx=5)

    # ---------------- BLOQUE CENTRAL (FORM + TABLA) ----------------
    frame_centro = ctk.CTkFrame(ventana, fg_color="transparent")
    frame_centro.grid(row=2, column=0)

    frame_centro.grid_columnconfigure(0, weight=1)
    frame_centro.grid_columnconfigure(1, weight=1)

    # -------- FORMULARIO --------
    frame_form = ctk.CTkFrame(frame_centro)
    frame_form.grid(row=0, column=0, padx=20, pady=10)

    campos = [
        "Nombre:",
        "teléfono:",
        "RFC:",
        "CP domicilio fiscal:",
        "Régimen fiscal:"
    ]

    for i in range(len(campos)):
        frame_form.grid_rowconfigure(i, weight=1)

    frame_form.grid_columnconfigure(1, weight=1)

    entries = []

    for i, texto in enumerate(campos):
        lbl = ctk.CTkLabel(frame_form, text=texto)
        lbl.grid(row=i, column=0, padx=10, pady=5, sticky="e")

        entry = ctk.CTkEntry(frame_form, width=250)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    # Botones del formulario
    frame_btn_form = ctk.CTkFrame(frame_form, fg_color="transparent")
    frame_btn_form.grid(row=len(campos), column=0, columnspan=2, pady=15)

    ctk.CTkButton(frame_btn_form, text="eliminar", width=100).pack(side="left", padx=10)
    ctk.CTkButton(frame_btn_form, text="editar", width=100).pack(side="left", padx=10)
    ctk.CTkButton(frame_btn_form, text="nuevo", width=100).pack(side="left", padx=10)

    # -------- TABLA VEHICULOS --------
    frame_tabla = ctk.CTkFrame(frame_centro)
    frame_tabla.grid(row=0, column=1, padx=20, pady=10, sticky="n")

    lbl_tabla = ctk.CTkLabel(frame_tabla, text="vehículos")
    lbl_tabla.pack(anchor="w", padx=10, pady=(5, 0))

    datos_tabla = [
        ["matricula", "marca", "modelo", "color"]
    ] + [["", "", "", ""] for _ in range(5)]

    tabla = CTkTable(
        master=frame_tabla,
        values=datos_tabla
    )
    tabla.pack(padx=10, pady=10)

    # ---------------- BOTONES INFERIORES ----------------
    frame_bottom = ctk.CTkFrame(ventana, fg_color="transparent")
    frame_bottom.grid(row=3, column=0, sticky="se", padx=20, pady=20)

    ctk.CTkButton(frame_bottom, text="cancelar", width=120).pack(side="left", padx=10)
    ctk.CTkButton(frame_bottom, text="guardar", width=120).pack(side="left", padx=10)