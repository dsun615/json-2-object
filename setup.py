import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json-to-object",
    version="0.0.1",
    author="Original author: Denna Sun, Maintained by Vladimir Podolian",
    author_email="vladimir.podlyan64@gmail.com",
    description="This is a simple package that deserializes json to your custom model include custom attributes and child objects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EnvInc/JsonToModel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
