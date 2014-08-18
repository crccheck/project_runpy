from setuptools import setup

setup(
    name='project_runpy',
    # remember to update __init__.py
    version='0.3.1',
    author='Chris Chang',
    author_email='c@crccheck.com',
    url='https://github.com/crccheck/project_runpy',
    packages=['project_runpy', ],
    license='Apache License, Version 2.0',
    description='Helper utilities for Python projects',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
