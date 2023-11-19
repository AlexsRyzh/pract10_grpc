from beanie import Document


class User(Document):
    username: str
    login: str
    password: str
