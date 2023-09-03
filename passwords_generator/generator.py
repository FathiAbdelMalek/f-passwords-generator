class PasswordGenerator:
    def __init__(self, plain_text=None, key_phrase=None):
        self.plain_text = plain_text
        self.key_phrase = key_phrase
        self.password = ""
        self.matrix = [['' for _ in range(5)] for _ in range(5)]

    @staticmethod
    def __clean_input(input_str):
        cleaned_str = input_str.lower().replace(' ', '').replace('j', 'i')
        return ''.join(filter(lambda c: 'a' <= c <= 'z', cleaned_str))

    def __prepare_text(self):
        self.plain_text = self.__clean_input(self.plain_text)
        for i in range(1, len(self.plain_text)):
            if self.plain_text[i] == self.plain_text[i - 1] and self.plain_text[i].isalpha():
                self.plain_text = self.plain_text[:i] + "x" + self.plain_text[i:]
        if len(self.plain_text) % 2 != 0:
            self.plain_text += 'x'

    def __prepare_key(self):
        self.key_phrase = self.__clean_input(self.key_phrase)

    def __generate_matrix(self):
        stash = []
        for c in self.key_phrase:
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
                self.matrix[i][j] = stash[index]
                index += 1

    def __index_locator(self, char):
        for i, row in enumerate(self.matrix):
            if char in row:
                return i, row.index(char)

    def __playfair(self):
        result = []
        i = 0
        while i < len(self.plain_text):
            if i == len(self.plain_text) - 1 and not self.plain_text[i].isalpha():
                result.append(self.plain_text[i])
                break
            if not self.plain_text[i].isalpha() or not self.plain_text[i + 1].isalpha():
                i += 1
                continue
            n1 = self.__index_locator(self.plain_text[i])
            n2 = self.__index_locator(self.plain_text[i + 1])
            if n1[1] == n2[1]:
                i1 = (n1[0] + 1) % 5
                j1 = n1[1]
                i2 = (n2[0] + 1) % 5
                j2 = n2[1]
                result.append(self.matrix[i1][j1])
                result.append(self.matrix[i2][j2])
            elif n1[0] == n2[0]:
                i1 = n1[0]
                j1 = (n1[1] + 1) % 5
                i2 = n2[0]
                j2 = (n2[1] + 1) % 5
                result.append(self.matrix[i1][j1])
                result.append(self.matrix[i2][j2])
            else:
                i1 = n1[0]
                j1 = n1[1]
                i2 = n2[0]
                j2 = n2[1]
                result.append(self.matrix[i1][j2])
                result.append(self.matrix[i2][j1])
            i += 2
        self.password = "".join(result)

    def __cipher(self):
        char_map = {'a': '@', 'e': '#', 'i': '$', 'o': '15', 'u': '21'}
        for char, replacement in char_map.items():
            self.password = self.password.replace(char, replacement)
        for i in range(len(self.password)):
            if self.password[i] in self.plain_text:
                self.password = self.password.replace(self.password[i], self.password[i].upper())

    def generate_password(self, text=None, key=None):
        if text:
            self.plain_text = text
        if key:
            self.key_phrase = key
        self.__prepare_text()
        self.__prepare_key()
        self.__generate_matrix()
        self.__playfair()
        self.__cipher()
