import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bytetrie",
    version="0.0.2",
    url="https://git.friedl.net/incubator/bytetrie",
    license="MIT",
    author="Armin Friedl",
    author_email="dev@friedl.net",

    description="A self-compressing radix trie with radix 256 in pure python",
    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=setuptools.find_packages(exclude=("tests",)),
    include_package_data=True,

    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ]
)
