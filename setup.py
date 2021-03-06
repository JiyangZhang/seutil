import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="seutil",
    version="0.5.0",
    author="Pengyu Nie",
    author_email="prodigy.sov@gmail.com",
    description="Python utilities for SE research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prodigysov/seutil",
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=(
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
    ),
    install_requires=["numpy>=1.14.4", "PyYAML>=5.1", "PyGitHub>=1.40", "unidiff>=0.5.5", "recordclass>=0.11.1", "typing_inspect>=0.4.0"],
    #data_files=[("config", ["pyutil_config.json"]),]
)
