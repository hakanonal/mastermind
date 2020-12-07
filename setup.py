import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mastermind-hakanonal", # Replace with your own username
    version="0.0.1",
    author="Hakan Onal",
    author_email="hakan.onal@yahoo.com",
    description="AI that plays mastermind",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hakanonal/mastermind",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
