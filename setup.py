from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pnrw',
    version='0.1.4',
    description='Python Nanocurrency RPC Wrapper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MiranDaniel/pnrw",
    author='MiranDaniel',
    author_email='mirandaniel@protonmail.com',
    license='License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    packages=['pnrw'],
    install_requires=[],

    classifiers=[
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
    desctiption=(
        "PNRW is a Python wrapper for the Nanocurrency RPC protocol"
    ),
    python_requires='>=3.6'
)
