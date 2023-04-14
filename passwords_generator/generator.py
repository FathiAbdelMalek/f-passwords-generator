class PassGen:

    def __init__(self, text=None, key=None):
        self.text = text
        self.key = key
        self.code = ""
        self.matrix = [['' for i in range(5)] for j in range(5)]

    def __prepare_text(self):
        self.text = self.text.lower()
        self.text = self.text.replace(' ', '')
        self.text = self.text.replace('j', 'i')
        for c in self.text:
            if ord(c) in range(48, 58) or c == '_':
                continue
            elif ord(c) not in range(97, 123):
                self.text = self.text.replace(c, '')
        for i in range(1, len(self.text)):
            if self.text[i] == self.text[i - 1] and not (ord(self.text[i]) in range(48, 58) or self.text[i] == '_'):
                self.text = self.text[: i] + "x" + self.text[i:]
        if len(self.text) & 1:
            self.text += 'x'

    def __prepare_key(self):
        self.key = self.key.lower()
        self.key = self.key.replace(' ', '')
        self.key = self.key.replace('j', 'i')
        for c in self.key:
            if ord(c) not in range(97, 123):
                self.key = self.key.replace(c, '')

    def __generate_matrix(self):
        stash = []
        for c in self.key:
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
        for i in range(0, 5):
            for j in range(0, 5):
                self.matrix[i][j] = stash[index]
                index += 1
        del stash
        del index

    def __index_locator(self, char):
        char_index = []
        for i, j in enumerate(self.matrix):
            for k, l in enumerate(j):
                if char == l:
                    char_index.append(i)
                    char_index.append(k)
                    return char_index

    def __playfair(self):
        result = []
        i = 0
        while i < len(self.text):
            if i == len(self.text) - 1 and self.text[i - 1] not in range(97, 123):
                result.append(self.text[i])
                break
            if ord(self.text[i]) in range(48, 58) or self.text[i] == '_':
                result.append(self.text[i])
                i += 1
                continue
            if ord(self.text[i + 1]) in range(48, 58) or self.text[i + 1] == '_':
                i += 1
                continue
            n1 = self.__index_locator(self.text[i])
            n2 = self.__index_locator(self.text[i + 1])
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
        self.code = "".join(str(x) for x in result)
        del result
        del i

    def __cipher(self):
        self.code = self.code.replace('a', '@')
        self.code = self.code.replace('e', '#')
        self.code = self.code.replace('i', '$')
        self.code = self.code.replace('o', '15')
        self.code = self.code.replace('u', '21')
        for i in range(len(self.code)):
            if self.code[i] in self.text:
                self.code = self.code.replace(self.code[i], self.code[i].upper())

    def generate_password(self, text=None, key=None):
        if text:
            self.text = text
        if key:
            self.key = key
        self.__prepare_text()
        self.__prepare_key()
        self.__generate_matrix()
        self.__playfair()
        self.__cipher()
