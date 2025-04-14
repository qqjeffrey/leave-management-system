from app.domain.models.user import User
import hashlib

class RegisterUserUseCase:
    def execute(self, email: str, name: str, password: str) -> User:
        hashed = self._hash_password(password)
        return User(email=email, name=name, hashed_password=hashed)

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
