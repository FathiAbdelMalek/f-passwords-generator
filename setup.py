import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="f-passwords-generator",
    version="0.1.0",
    author="FathiAbdelMalek",
    author_email="abdelmalek.fathi.2001@gmail.com",
    url="https://github.com/FathiMalek/f-pass-gen.git",
    description="Strong Passwords Generator made with python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "passwords_generator"},
    packages=setuptools.find_packages(where="passwords_generator"),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
