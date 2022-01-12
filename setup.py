from setuptools import find_packages, setup

install_requires = ["numpy>=1.20.3"]

tests_require = [
    "coverage==5.3",
    "pytest==5.4.3",
    # Linting
    "isort==4.3.21",
    "flake8==3.8.4",
    "flake8-blind-except==0.1.1",
    "flake8-debugger==3.2.1",
    "flake8-imports==0.1.1",
]

setup(
    name="levenshtein-package",
    version="0.0.2",
    description="Package for calculating Levenshtein distance and similarity",
    long_description=open("README.rst", "r").read(),
    url="https://www.github.com/leongraumans/levenshtein/",
    author="Leon Graumans",
    author_email="hey@leongraumans.nl",
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={"test": tests_require},
    entry_points={},
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    license="Proprietary",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: Other/Proprietary License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    zip_safe=False,
)
