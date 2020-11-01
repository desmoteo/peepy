import setuptools

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()    

setuptools.setup(
    name="peepy", # Replace with your own username
    version="0.0.2",
    author="Matteo Ferrabone",
    author_email="matteo.ferrabone@gmail.com",
    license='MIT',
    description="A simple Observer Pattern implementation with decorators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/desmoteo/peepy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
