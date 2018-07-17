from setuptools import setup, find_packages


setup(
    name='pypolisen',
    version='1.1',
    install_requires=[
        'requests'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'polisen = pypolisen.bin:run'
        ]
    }
)
