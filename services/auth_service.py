class AuthService:

    def authenticate_user(self, user, password):
        if user == "admin" and password == "123":
            return True
        return False
            
                