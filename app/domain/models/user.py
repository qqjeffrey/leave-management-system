from dataclasses import dataclass

@dataclass
class User:
    email: str
    name: str
    hashed_password: str
