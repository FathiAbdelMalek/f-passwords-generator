class PasswordGenerator:
    def __init__(self, _text: str = None, _key: str = None):
        self._text = _text
        self._key = _key
        self._matrix = [['' for _ in range(5)] for _ in range(5)]
        self._char_replacements = {}
        if _text:
            self._prepare_text()
        if _key:
            self._prepare_key()
            self._generate_matrix()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text
        self._prepare_text()

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key: str):
        self._key = key
        self._prepare_key()
        self._generate_matrix()

    @property
    def matrix(self):
        return self._matrix

    @property
    def character_replacements(self):
        return self._char_replacements

    @staticmethod
    def _clean_input(input_str):
        cleaned_str = input_str.lower().replace(' ', '').replace('j', 'i')
        return ''.join(filter(lambda c: 'a' <= c <= 'z' or '0' <= c <= '9', cleaned_str))

    def _prepare_text(self):
        self._text = self._clean_input(self._text)
        for i in range(1, len(self._text)):
            if self._text[i] == self._text[i - 1] and self._text[i].isalpha():
                self._text = self._text[:i] + "x" + self._text[i:]
        if len(self._text) % 2 != 0:
            self._text += 'x'

    def _prepare_key(self):
        self._key = self._clean_input(self._key)

    def _generate_matrix(self):
        stash = []
        for c in self._key:
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
        while i < len(self._text) - 1:
            if i == len(self._text) - 1 and not self._text[i].isalpha():
                result.append(self._text[i])
                break
            if not self._text[i].isalpha() or not self._text[i + 1].isalpha():
                result.append(self._text[i])
                i += 1
                continue
            n1 = self._index_locator(self._text[i])
            n2 = self._index_locator(self._text[i + 1])
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
        return "".join(result)

    def _custom_cipher(self, password):
        for char, replacement in self._char_replacements.items():
            password = password.replace(char, replacement)
        for i in range(len(password)):
            if password[i] in self._text:
                password = password.replace(password[i], password[i].upper())
        return password

    def replace_character(self, char: str, replacement: str):
        self._char_replacements[char] = replacement

    def reset_character(self, char: str):
        if char in self._char_replacements:
            del self._char_replacements[char]

    def generate_password(self, text: str = None, key: str = None):
        if text:
            self._text = text
            self._prepare_text()
        if key:
            self._key = key
            self._prepare_key()
            self._generate_matrix()
        return self._custom_cipher(self._playfair())
