from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pypolisen',
    version='2.0.0',
    description="Get events from the Swedish police",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sebastian Karlsson",
    author_email="sebbekarlsson97@gmail.com",
    keywords="events police sweden",
    url="https://github.com/sebbekarlsson/pypolisen",
    install_requires=[
        'requests',
    ],
    tests_require=[
        "pytest==6.1.1"
    ],
    packages=[
        'pypolisen'
    ],
    python_requires=">=3.5",
    entry_points={
        'console_scripts': [
            'polisen = bin:run'
        ]
    }
)
