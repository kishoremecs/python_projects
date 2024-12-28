from setuptools import setup, find_packages

setup(
    name="hello-world",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    python_requires=">=3.7",
    author="Kishore Rachuti",
    author_email="kmr.kishore@gmail.com",
    description="A simple Hello World application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kishoremecs/hello-world",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)