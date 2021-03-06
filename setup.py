import setuptools
import os
environment_variable_value = os.environ.get("BITBUCKET_BUILD_NUMBER", None )

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hadoop-yarn-cluster-checker-lib",
    version=environment_variable_value,
    author="fafi84",
    author_email="ffischer1984@googlemail.com",
    description="fires an event if your hadoop-yarn cluster gets empty",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/ffischer/hadoop-yarn-cluster-checker-model",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)