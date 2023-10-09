from cipherspy.cipher import *


class PasswordGenerator:
    def __init__(self, text: str = None, key: str = "password", shift: int = 3, algorithm: str = 'playfair'):
        self._char_replacements = {}
        self._text = text
        self._key = key
        self._shift = shift
        self._algorithm_name = algorithm.lower()
        self._algorithm = self._set_algorithm()

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text

    @property
    def key(self) -> str:
        return self._key

    @key.setter
    def key(self, key: str):
        self._key = key

    @property
    def shift(self) -> int:
        return self._shift

    @shift.setter
    def shift(self, shift: int):
        self._shift = shift

    @property
    def algorithm(self) -> str:
        return self._algorithm_name

    @algorithm.setter
    def algorithm(self, algorithm: str):
        self._algorithm_name = algorithm.lower()
        self._algorithm = self._set_algorithm()

    @property
    def character_replacements(self):
        return self._char_replacements

    def _set_algorithm(self):
        match self._algorithm_name:
            case 'playfair':
                return PlayfairCipher(self._key)
            case 'caesar':
                return CaesarCipher(self._shift)
            case '_':
                return PlayfairCipher(self._key)

    def _custom_cipher(self, password):
        for char, replacement in self._char_replacements.items():
            password = password.replace(char, replacement)
        for i in range(len(password)):
            if password[i] in self._text:
                password = password.replace(password[i], password[i].upper())
        return password

    def _update_algorithm_properties(self):
        self._algorithm = self._set_algorithm()

    def replace_character(self, char: str, replacement: str):
        self._char_replacements[char] = replacement

    def reset_character(self, char: str):
        if char in self._char_replacements:
            del self._char_replacements[char]

    def generate_password(self):
        self._update_algorithm_properties()
        return self._custom_cipher(self._algorithm.encrypt(self._text))
