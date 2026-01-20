from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Topsis-Saniya-102303183",
    version="1.0.0",
    author="Saniya Jindal",
    author_email="saniya.jindal@example.com",
    description="A Python package for solving MCDM problems using TOPSIS method",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "topsis=topsis_102303183.topsis:main",
        ],
    },
)
