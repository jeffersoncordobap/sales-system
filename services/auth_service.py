class ServicioAutenticacion:

    def autenticar_usuario(self, usuario, contrasena):
        if usuario == "admin" and contrasena == "123":
            return True
        return False
            
                