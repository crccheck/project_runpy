from setuptools import setup

setup(
    name='project_runpy',
    version='0.1-dev.0',
    author='Chris Chang',
    author_email='c@crccheck.com',
    url='https://github.com/crccheck/project_runpy',
    packages=['project_runpy', ],
    license='Apache License, Version 2.0',
    description='Helper utilities for Python projects',
    long_description=open('README.rst').read(),
    install_requires=['dj-settings-helpers>=1.0,<2'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
    ],
)
