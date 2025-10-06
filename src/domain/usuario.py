
class Usuario:
    def __init__(self, id, nombre, apellido_1, apellido_2, email, contrasena):
        self.id = id
        self.nombre = nombre
        self.apellido_1 = apellido_1
        self.apellido_2 = apellido_2
        self.email = email
        self.contrasena = contrasena

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido_1} {self.apellido_2}"

    def verificar_contrasena(self, contrasena_introducida):
        return self.contrasena == contrasena_introducida

    def cambiar_contrasena(self, nueva_contrasena):
        self.contrasena = nueva_contrasena

