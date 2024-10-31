from setuptools import setup, find_packages

def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    with open(filename, 'r') as f:
        return f.read().splitlines()

setup(
    name='DiaPredict',  # Library name
    version='0.1',  # Version number
    packages=find_packages(),  # Automatically find all packages
    install_requires=parse_requirements('requirements.txt'),  # Read from requirements.txt
    description='Diabetes prediction project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Viktoria, Tarang and Enzo from DSDM 2025',
    author_email='viktoria.gagua@bse.eu',
    url='https://github.com/Viktoriag27/computing_hw5',  # URL of your project repository
    classifiers=[  # Classifiers for Python Package Index (PyPI)
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version
)
