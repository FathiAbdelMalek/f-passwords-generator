# f-passwords-generator

<b>Strong Passwords Generator made with python.</b>

## How to use

```python
from passwords_generator import PasswordGenerator

pass_gen = PasswordGenerator(plain_text=None, key_phrase=None)
pass_gen.generate_password(text=None, key=None)
password = pass_gen.password
```

## Make it a command line tool

- first you need to install python in your machine.
- install pyinstaller with `pip install pyinstaller`.
- run `pyinstaller passwords_generator/__main__.py --name pass-gen`.
- if you in linux make a symlink of `dist/pass-gen/pass-gen` in `/bin` or `/home/username/bin` to use it from terminal.
- if on windows just add it to the PATH.

Now you can just open terminal/command-prompt and type pass-gen

## More about the module

### On python script

`generate_password(plain_text=None, key_phrase=None)` method can accept two optional arguments\
`plain_text`: is the text to be ciphered\
`key_phrase`: is the key to be used in the generation
key optional in the constructor and the method, but the text must be set in one of them

examples:

Example 1:

```python
from passwords_generator import PasswordGenerator

pass_gen = PasswordGenerator("demo text")
pass_gen.generate_password()
password = pass_gen.password
```
Example 2:

```python
from passwords_generator import PasswordGenerator

pass_gen = PasswordGenerator()
pass_gen.generate_password("demo text", "demo key")
password = pass_gen.password
```
Example 3:

```python
from passwords_generator import PasswordGenerator

pass_gen = PasswordGenerator()
pass_gen.generate_password("demo text")
password = pass_gen.password
```
Example 4:

```python
from passwords_generator import PasswordGenerator

pass_gen = PasswordGenerator("demo code", "demo key")
pass_gen.generate_password()
password = pass_gen.password
```

`pass_gen.code` is the result of the encryption

if the key is not set, the class will randomly generate one

### Command Line Usage
![usage example](usage.png)
