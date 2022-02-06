from passlib.context import CryptContext

password_context = CryptContext(schemes="bcrypt", deprecated="auto")


class PasswordHash(object):
    def __init__(self, password: str):
        self.password = password

    def bcrypt(self):
        return password_context.hash(self.password)

    def verify(self, hashed_password):
        return password_context.verify(self.password, hashed_password)
