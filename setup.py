import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="peepy", # Replace with your own username
    version="0.0.1",
    author="Matteo Ferrabone",
    author_email="matteo.ferrabone@gmail.com",
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
