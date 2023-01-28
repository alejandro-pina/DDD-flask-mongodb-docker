import random
import string

from dataclasses import dataclass
from passlib.hash import sha256_crypt


@dataclass
class PasswordVO:
    value: str


@dataclass(frozen=True)
class PasswordVO:
    value: str

    def create_random_pass():
        letters = string.ascii_lowercase
        plainPassword = ''.join(random.choice(letters) for i in range(30))
        return PasswordVO(sha256_crypt.encrypt(plainPassword))

    def create_hash(plainPassword):
        if len(plainPassword) < 8 or len(plainPassword) > 30 or (' ' in plainPassword) == True:
            raise ValueError('Error VO: PasswordVO - Incorrect password.')
        return PasswordVO(sha256_crypt.encrypt(plainPassword))

    def create_hash_str(plainPassword):
        if len(plainPassword) < 8 or len(plainPassword) > 30 or (' ' in plainPassword) == True:
            raise ValueError('Error VO: PasswordVO - Incorrect password.')
        return sha256_crypt.encrypt(plainPassword)

    def compare_hash(plainPassword, hashPassword):
        return sha256_crypt.verify(plainPassword, str(hashPassword))

    def __str__(self) -> str:
        return self.value
