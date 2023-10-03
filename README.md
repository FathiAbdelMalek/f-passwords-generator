# f-passwords-generator

<b>Strong Passwords Generator made with python.</b>

## Attributes

- `text` (can be modified, have getter and setter): The plain text to be ciphered.
- `key` (can be modified, have getter and setter): The key phrase to be used in the ciphering operation on algorithms like playfair (default is 'password').
- `shift` (can be modified, have getter and setter): The number to be used as shift on algorithms like caesar (default is 3).
- `algorithm` (can be modified, have getter and setter): The algorithm to be used for ciphering operation (default is playfair).
- `characters_replacements` (cannot be modified, have only getter): Custom dictionary you can use to change characters after ciphering (default is empty).
- `matrix` (cannot be modified, have only getter): The matrix used in the ciphering operation.

## Methods

- `replace_character(char: str, replacement: str)`: used to add an item to `characters_replacements`.
- `reset_character(char: str)`: remove the character from `characters_replacements` if exists.
- `generate_password()`: generate a password from the `text` using `key` or `shift` according to the used `algorithm` and `characters_replacements`.

## How to use

```python
from passwords_generator import PasswordGenerator

pass_gen = PasswordGenerator(text=None, key="password", shift=3, algorithm="playfair")
pass_gen.text = "demo text"
pass_gen.key = "demo key"  # will be used on algorithms like playfair (default is 'password')
pass_gen.shift = 3  # will be used on algorithms like caesar (default is 3)
pass_gen.algorithm = 'playfair'  # specify the algorithm to use (default is playfair)
pass_gen.replace_character(char="", replacement="")
pass_gen.reset_character(char="")
password = pass_gen.generate_password()
```

## Examples

### Example 1

```python
from passwords_generator import PasswordGenerator

pass_gen = PasswordGenerator("demo code", "demo key")
password = pass_gen.generate_password()
```

### Example 2

```python
from passwords_generator import PasswordGenerator

pass_gen = PasswordGenerator()
pass_gen.text = "demo text"
pass_gen.key = "demo key"
password = pass_gen.generate_password()
```

### Example 3

```python
from passwords_generator import PasswordGenerator

pass_gen = PasswordGenerator("demo text", shift=3, algorithm="caesar")
password = pass_gen.generate_password()
```

### Example 4

```python
from passwords_generator import PasswordGenerator

pass_gen = PasswordGenerator()
pass_gen.text = "demo text"
pass_gen.shift = 3
pass_gen.algorithm = 'caesar'
password = pass_gen.generate_password()
```

## Notice

The valid cipher algorithms are only those who has been implemented on `cipherspy` package.
- caesar
- playfair (default one)

## License

The code in this repository is licensed under the MIT License.

You can find the full text of the license in the [LICENSE](https://github.com/fathiabdelmalek/f-passwords-generator/blob/main/LICENSE) file. For more information, please visit the repository on [GitHub](https://github.com/fathiabdelmalek/f-passwords-generator).
