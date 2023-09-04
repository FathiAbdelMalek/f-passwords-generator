# f-passwords-generator

<b>Strong Passwords Generator made with python.</b>

## Attributes

- `plain_text` (can be modified, have getter and setter): The plain text to be ciphered.
- `key_phrase` (can be modified, have getter and setter): The key phrase to be used in the operation.
- `characters_replacements` (cannot be modified, have only getter): Custom dictionary you can use to change characters after ciphering, default is empty.
- `matrix` (cannot be modified, have only getter): The matrix used in the cyphering operation.
- `password` (cannot be modified, have only getter): The generated password, when first constructed it's empty string.

## Methods

- `replace_character(char: str, replacement: str)`: used to add an item to `characters_replacements`.
- `reset_character(char: str)`: remove the character from `characters_replacements` if exists.
- `generate_password(text: str = None, key: str = None)`: generate a password from the `plain_text` using `key_phrase` and `characters_replacements`.

## How to use

```python
from passwords_generator import PasswordGenerator

pass_gen = PasswordGenerator(plain_text=None, key_phrase=None)
pass_gen.generate_password(text=None, key=None)
pass_gen.plain_text = "demo text"
pass_gen.key_phrase = "demo key"
pass_gen.replace_character(char="", replacement="")
pass_gen.reset_character(char="")
password = pass_gen.password
```

## Examples

### Example 1

```python
from passwords_generator import PasswordGenerator

pass_gen = PasswordGenerator("demo code", "demo key")
pass_gen.generate_password()
password = pass_gen.password
```

### Example 2

```python
from passwords_generator import PasswordGenerator

pass_gen = PasswordGenerator()
pass_gen.generate_password("demo text", "demo key")
password = pass_gen.password
```

### Example 3

```python
from passwords_generator import PasswordGenerator

pass_gen = PasswordGenerator()
pass_gen.plain_text = "demo text"
pass_gen.key_phrase = "demo key"
pass_gen.generate_password()
password = pass_gen.password
```

## License

The code in this repository is licensed under the MIT License.

You can find the full text of the license in the [LICENSE](https://github.com/fathiabdelmalek/f-passwords-generator/blob/main/LICENSE) file. For more information, please visit the repository on [GitHub](https://github.com/fathiabdelmalek/f-passwords-generator).
