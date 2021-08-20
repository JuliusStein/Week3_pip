import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cogworks_week3",
    version="1.0.0",
    author="Ryan Soklaski (@rsokl)",
    author_email="ry26099@mit.edu",
    url="https://github.com/JuliusStein/Week2_pip",
    description="Provides resources and required libraries for the Language Module of CogWorks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = 'MIT',
    zip_safe = False,
    install_requires=[
        "jupyter",
        "notebook",
        "numpy",
        "matplotlib",
        "numba",
        "scikit-learn",
        "nltk",
        "mygrad",
        "mynn",
        "noggin",
        "gensim"
    ],
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
)
