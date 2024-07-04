from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
        name="pyviber",
        version="0.1",
        description="Python package for developing Viber Bots",
        packages=find_packages(),
        requires=required
)
