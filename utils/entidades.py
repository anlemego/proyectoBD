class Usuario:
    def __init__(self):
        self._usuario_id = 0
        self._nombre = ""
        self._email = ""
        self._username = ""
        self._password = ""
        self._perfil = ""

    def get_usuario_id(self):
        return self._usuario_id

    def set_usuario_id(self, valor):
        self._usuario_id = valor

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, valor):
        self._nombre = valor

    def get_email(self):
        return self._email

    def set_email(self, valor):
        self._email = valor

    def get_username(self):
        return self._username

    def set_username(self, valor):
        self._username = valor

    def get_password(self):
        return self._password

    def set_password(self, valor):
        self._password = valor

    def get_perfil(self):
        return self._perfil

    def set_perfil(self, valor):
        self._perfil = valor

class Vehiculo:
    def __init__(self):
        self._matricula = ""
        self._modelo = ""
        self._marca = ""
        self._color = ""
        self._cliente_id = 0

    def get_matricula(self):
        return self._matricula

    def set_matricula(self, valor):
        self._matricula = valor

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, valor):
        self._modelo = valor

    def get_marca(self):
        return self._marca

    def set_marca(self, valor):
        self._marca = valor

    def get_color(self):
        return self._color

    def set_color(self, valor):
        self._color = valor

    def get_cliente_id(self):
        return self._cliente_id

    def set_cliente_id(self, valor):
        self._cliente_id = valor