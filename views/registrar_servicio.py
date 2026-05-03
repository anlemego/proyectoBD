import customtkinter as ctk
from CTkTable import CTkTable

from utils.helpers import limpiar_ventana

def pantalla_registrar_servicio(ventana):
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

    # ---------------- TITULO ----------------
    titulo = ctk.CTkLabel(
        ventana,
        text="Registrar servicio",
        font=ctk.CTkFont(size=26, weight="bold")
    )
    titulo.grid(row=0, column=0, pady=(10, 20),sticky="n")

    # ---------------- FORMULARIO ----------------
    frame_form = ctk.CTkFrame(ventana)
    frame_form.grid(row=2, column=0)

    campos = ["ID cliente:", "vehículo:", "servicio:", "duración:"]

    for i in range(len(campos)):
        frame_form.grid_rowconfigure(i, weight=1)

    frame_form.grid_columnconfigure(1, weight=1)

    # --- ID CLIENTE (Entry) ---
    lbl_id = ctk.CTkLabel(frame_form, text="ID cliente:")
    lbl_id.grid(row=0, column=0, padx=10, pady=8, sticky="e")

    entry_id = ctk.CTkEntry(frame_form, width=300)
    entry_id.grid(row=0, column=1, padx=10, pady=8)

    # --- VEHICULO (OptionMenu + botón) ---
    lbl_vehiculo = ctk.CTkLabel(frame_form, text="vehículo:")
    lbl_vehiculo.grid(row=1, column=0, padx=10, pady=8, sticky="e")

    frame_vehiculo = ctk.CTkFrame(frame_form, fg_color="transparent")
    frame_vehiculo.grid(row=1, column=1, padx=10, pady=8, sticky="we")

    option_vehiculo = ctk.CTkOptionMenu(
        frame_vehiculo,
        values=["Vehículo 1", "Vehículo 2"]
    )
    option_vehiculo.pack(side="left", padx=(0, 10),expand=True, fill="x")

    btn_nuevo_vehiculo = ctk.CTkButton(frame_vehiculo, text="nuevo", width=100)
    btn_nuevo_vehiculo.pack(side="right")

    # --- SERVICIO (OptionMenu) ---
    lbl_servicio = ctk.CTkLabel(frame_form, text="servicio:")
    lbl_servicio.grid(row=2, column=0, padx=10, pady=8, sticky="e")

    option_servicio = ctk.CTkOptionMenu(
        frame_form,
        values=["Estacionamiento", "Pensión"]
    )
    option_servicio.grid(row=2, column=1, padx=10, pady=8,sticky="we")

    # --- DURACIÓN (Entry) ---
    lbl_duracion = ctk.CTkLabel(frame_form, text="duración:")
    lbl_duracion.grid(row=3, column=0, padx=10, pady=8, sticky="e")

    entry_duracion = ctk.CTkEntry(frame_form, width=300)
    entry_duracion.grid(row=3, column=1, padx=10, pady=8)

    # ---------------- BOTONES INFERIORES ----------------
    frame_bottom = ctk.CTkFrame(ventana, fg_color="transparent")
    frame_bottom.grid(row=3, column=0, sticky="se", padx=20, pady=20)

    btn_cancelar = ctk.CTkButton(frame_bottom, text="cancelar", width=120)
    btn_cancelar.pack(side="left", padx=10)

    btn_guardar = ctk.CTkButton(frame_bottom, text="guardar", width=120)
    btn_guardar.pack(side="left", padx=10)