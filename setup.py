#!/usr/bin/env python
""" setup.py for yamlenc - a simple YAML-based Regular Expression Puppet ENC """
from setuptools import setup

from yamlenc import __version__

setup(
    name='yamlenc',
    version=__version__,
    description='Simple YAML-based Regular Expression Puppet ENC',
    author='Jakob Schlyter',
    author_email='jakob@kirei.se',
    url='https://github.com/kirei/puppet-yaml-enc',
    packages=['yamlenc'],
    long_description="""\
yamlenc is a simple YAML-based Regular Expression Puppet ENC
(External Node Classifier).

The user supplies a YAML-file (examples included) where regular expression
based host name patterns form the key. The output is then consumed by a
puppet master to perform external node classification for a calling node.
""",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Systems Administration",
    ],
    keywords='yaml puppet external node classifier enc regular expression regex re',
    license='BSD',
    install_requires=[
        'setuptools',
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'yamlenc = yamlenc.yamlenc:main',
        ]
    }
)
