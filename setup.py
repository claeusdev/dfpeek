from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="dfpeek",
    author="Nana Adjei Manu",
    version="1.0.0",
    description="Quickly summarize your data",
    packages=find_packages("src"),
    package_dir={"": "src"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/claeusdev/frame-explorer",
    python_requires=">=3.6",
    install_requires=["pandas", "numpy"],
    entry_points={"console_scripts": ["dfpeek=dfpeek.cli:main"]},
)
