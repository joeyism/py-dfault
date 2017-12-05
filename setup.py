from setuptools import setup


version = "1.0.1"


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name = "dfault",
    packages = ["dfault"],
    version = version,
    description = "A simple lightweight class that allows the user to fallback on default values",
    long_description = long_descr,
    author = "Joey Sham",
    author_email = "sham.joey@gmail.com",
    url = "http://www.joeyism.com",
    )
