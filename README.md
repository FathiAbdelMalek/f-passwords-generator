# f-passwords-generator

<b>Strong password generator with python</b>

## How to use

`from passwords_generator.generator import PassGen`\
`pass_gen = PassGen(text=None, key=None)`\
`pass_gen.generate_password(text=None, key=None)`\
`password = pass_gen.code`

## Make it a command line tool

- first you need to install python in your machine
- install pyinstaller with `pip install pyinstaller`
- run `pyinstaller --onefile --name pass-gen __main__.py`
- if you in linux copy the dist/pass-gen to /bin or /home/username/bin
- if on windows just add it to the PATH

Now you can just open terminal/command-prompt and type pass-gen

## More about the module

### On python script

`generate_password` method can accept two optional arguments\
`generate_password(text=None, key=None)`\
`text`: is the text to be ciphered\
`key`: is the key to be used in the generation
key optional in the constructor and the method, but the text must be set in one of them

examples:

- `pass_gen = PassGen("demo text"); pass_gen.generate_password(); password = pass_gen.code`\
- `pass_gen = PassGen(); pass_gen.generate_password("demo text", "demo key"); password = pass_gen.code`
- `pass_gen = PassGen(); pass_gen.generate_password("demo text"); password = pass_gen.code`
- `pass_gen = PassGen("demo code", "demo key"); pass_gen.generate_password(); password = pass_gen.code`

`pass_gen.code` is the result of the encryption

if the `key` is not set, the class will randomly generate one

### Command Line Usage

the same if you launch it from terminal
examples:

- `$ pass-gen`
- `$ pass-gen "demo text"`
- `$ pass-gen "demo text" "demo key"`

results:

- in case one: the terminal will prompt to ask you for the text and generate a random key
- in case tow: the terminal will take the entered text and encrypt it with a random generated key
- in case three: the terminal will take the entered text and encrypt it with the given key

we will add more functionality in the future
