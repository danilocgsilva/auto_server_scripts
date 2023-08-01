from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="auto_server_scripts",
    version=VERSION,
    description="Helps to forge common terms used for servers setup",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="server setup",
    url="https://github.com/danilocgsilva/auto_server_scripts",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=[
        "auto_server_scripts", 
        "auto_server_scripts.scripts",
        "auto_server_scripts.exceptions"
    ],
    entry_points={"console_scripts": ["aus=auto_server_scripts.__main__:main"],},
    include_package_data=True
)

