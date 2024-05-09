from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Topsis-Param-102103259",
    version="1.0.0",
    author="Paramdeep Singh Gill",
    author_email="paramdeepsinghgill03@gmail.com",
    url="https://github.com/paramdeepsinghgill/UCS654_assignment_1",
    description="A python package for implementing topsis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas", "numpy"],
    entry_points={"console_scripts": ["Topsis_Paramdeep_102103259 = Topsis_Paramdeep_102103259.main:main"]},
)