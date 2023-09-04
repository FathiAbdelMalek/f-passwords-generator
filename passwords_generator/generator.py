class PasswordGenerator:
    def __init__(self, plain_text: str = None, key_phrase: str = None):
        self._plain_text = plain_text
        self._key_phrase = key_phrase
        self._matrix = [['' for _ in range(5)] for _ in range(5)]
        self._char_replacements = {}
        self._password = ""
        if plain_text:
            self._prepare_text()
        if key_phrase:
            self._prepare_key()
            self._generate_matrix()

    @property
    def plain_text(self):
        return self._plain_text

    @plain_text.setter
    def plain_text(self, text: str):
        self._plain_text = text
        self._prepare_text()

    @property
    def key_phrase(self):
        return self._key_phrase

    @key_phrase.setter
    def key_phrase(self, key: str):
        self._key_phrase = key
        self._prepare_key()
        self._generate_matrix()

    @property
    def password(self):
        return self._password

    @property
    def matrix(self):
        return self._matrix

    @property
    def character_replacements(self):
        return self._char_replacements

    @staticmethod
    def _clean_input(input_str):
        cleaned_str = input_str.lower().replace(' ', '').replace('j', 'i')
        return ''.join(filter(lambda c: 'a' <= c <= 'z', cleaned_str))

    def _prepare_text(self):
        self._plain_text = self._clean_input(self._plain_text)
        for i in range(1, len(self._plain_text)):
            if self._plain_text[i] == self._plain_text[i - 1] and self._plain_text[i].isalpha():
                self._plain_text = self._plain_text[:i] + "x" + self._plain_text[i:]
        if len(self._plain_text) % 2 != 0:
            self._plain_text += 'x'

    def _prepare_key(self):
        self._key_phrase = self._clean_input(self._key_phrase)

    def _generate_matrix(self):
        stash = []
        for c in self._key_phrase:
            if c not in stash:
                stash.append(c)
        for i in range(97, 123):
            if chr(i) not in stash:
                if i == 105 and 'i' in stash:
                    continue
                if i == 106:
                    continue
                stash.append(chr(i))
        index = 0
        for i in range(5):
            for j in range(5):
                self._matrix[i][j] = stash[index]
                index += 1

    def _index_locator(self, char):
        for i, row in enumerate(self._matrix):
            if char in row:
                return i, row.index(char)

    def _playfair(self):
        result = []
        i = 0
        while i < len(self._plain_text):
            if i == len(self._plain_text) - 1 and not self._plain_text[i].isalpha():
                result.append(self._plain_text[i])
                break
            if not self._plain_text[i].isalpha() or not self._plain_text[i + 1].isalpha():
                i += 1
                continue
            n1 = self._index_locator(self._plain_text[i])
            n2 = self._index_locator(self._plain_text[i + 1])
            if n1[1] == n2[1]:
                i1 = (n1[0] + 1) % 5
                j1 = n1[1]
                i2 = (n2[0] + 1) % 5
                j2 = n2[1]
                result.append(self._matrix[i1][j1])
                result.append(self._matrix[i2][j2])
            elif n1[0] == n2[0]:
                i1 = n1[0]
                j1 = (n1[1] + 1) % 5
                i2 = n2[0]
                j2 = (n2[1] + 1) % 5
                result.append(self._matrix[i1][j1])
                result.append(self._matrix[i2][j2])
            else:
                i1 = n1[0]
                j1 = n1[1]
                i2 = n2[0]
                j2 = n2[1]
                result.append(self._matrix[i1][j2])
                result.append(self._matrix[i2][j1])
            i += 2
        self._password = "".join(result)

    def _custom_cipher(self):
        for char, replacement in self._char_replacements.items():
            self._password = self._password.replace(char, replacement)
        for i in range(len(self._password)):
            if self._password[i] in self._plain_text:
                self._password = self._password.replace(self._password[i], self._password[i].upper())

    def replace_character(self, char: str, replacement: str):
        self._char_replacements[char] = replacement

    def reset_character(self, char: str):
        if char in self._char_replacements:
            del self._char_replacements[char]

    def generate_password(self, text: str = None, key: str = None):
        if text:
            self._plain_text = text
            self._prepare_text()
        if key:
            self._key_phrase = key
            self._prepare_key()
            self._generate_matrix()
        self._playfair()
        self._custom_cipher()
