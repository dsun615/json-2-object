import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json2object", # Replace with your own username
    version="0.0.5",
    author="Denna Sun",
    author_email="dennasun615@gmail.com",
    description="This is a simple package that deserializes json to your custom model include custom attributes and child objects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dsun615/json-2-object",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)