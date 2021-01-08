import os
from codecs import open

from setuptools import find_packages, setup

# Get the long description from the README file
with open(os.path.join(os.path.dirname(__file__), "README.md")) as f:
    long_description = f.read()

version = os.environ.get("GIT_DESCRIBE_TAG", "0.0.0.dev0").lstrip("v")
setup(
    name="dask-cudf",
    version=version,
    description="Utilities for Dask and cuDF interactions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rapidsai/dask-cudf",
    author="NVIDIA Corporation",
    license="Apache 2.0",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Database",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=["docs", "tests", "tests.*", "docs.*"]),
    install_requires=open("requirements.txt").read().strip().split("\n"),
)
