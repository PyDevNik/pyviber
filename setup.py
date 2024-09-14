from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('README.md') as md:
    long_desc = md.read()

setup(
        name="pyviber",
        version="0.2",
        description="Python package for developing Viber Bots",
        packages=find_packages(),
        long_description=long_desc,
        long_description_content_type='text/markdown',
        requires=required
)
