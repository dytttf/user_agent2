# coding:utf8
from setuptools import setup, find_packages

version = "2021.12.11"

setup(
    name="user_agent2",
    version=version,
    description="generate random user agent",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    author="Dytttf",
    author_email="dytttf@foxmail.com",
    url="https://github.com/dytttf/user_agent2",
    packages=find_packages(),
    install_requires=[
        "user_agent==0.1.10",
    ],
    license="BSD",
    classifiers=[],
    keywords=["user_agent"],
)
