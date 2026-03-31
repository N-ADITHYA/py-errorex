from setuptools import setup, find_packages

setup(
    name="py-errorex",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[],
    author="Adithya N",
    description="Beginner-friendly Python error explainer",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
)