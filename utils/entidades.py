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