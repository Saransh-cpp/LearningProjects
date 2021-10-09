from setuptools import setup, find_packages

f = open("requirements.txt", "r")
install_requires = f.read().splitlines()
f.close()

classifiers = [
    "Operating System :: OS Independent",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.9",
]

setup(
    name="create_gif",
    version="0.1.0",
    license="MIT",
    description="Create a GIF for LAMMPS with a single line.",
    packages=find_packages(include=["create_gif"]),
    classifiers=classifiers,
    install_requires=install_requires,
)