from enum import Enum


class Email(str, Enum):
    email = "eve.holt@reqres.in"
    wrong_email = "sydney@fife"


class Password(str, Enum):
    password = "pistol"
