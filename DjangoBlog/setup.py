import os
import setuptools

os.chdir(os.pardir)

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="DjangoBlogSvorcan",
    version="0.0.1",
    author="Aleksandar Svorcan",
    author_email="aleksandar@svorcan.info",
    description="My first Django project - blog application for learning purposes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stalker92/DjangoBlog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)