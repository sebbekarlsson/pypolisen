from setuptools import setup, find_packages


setup(
    name='pypolisen',
    version='1.1.2',
    install_requires=[
        'requests',
        'bs4'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'polisen = pypolisen.bin:run'
        ]
    }
)
