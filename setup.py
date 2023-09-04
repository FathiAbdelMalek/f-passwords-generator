import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="f-passwords-generator",
    version="1.4.0",
    author="Fathi AbdelMalek",
    author_email="abdelmalek.fathi.2001@gmail.com",
    url="https://github.com/fathiabdelmalek/f-passwords-generator.git",
    description="Strong Passwords Generator made with python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['passwords_generator'],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
