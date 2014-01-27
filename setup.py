from distutils.core import setup

setup(
    name='project_runpy',
    version='0.2.0',
    author='Chris Chang',
    author_email='c@crccheck.com',
    url='https://github.com/crccheck/project_runpy',
    packages=['project_runpy', ],
    license='Apache License, Version 2.0',
    description='Helper utilities for Python projects',
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
    ],
)
