#!/usr/bin/env python
""" setup.py for yamlenc - a simple YAML-based Regular Expression Puppet ENC """
from setuptools import setup

setup(
    name='yamlenc',
    version='0.2',
    description='Simple YAML-based Regular Expression Puppet ENC',
    author='IPnett AS',
    author_email='info@cloud.ipnett.com',
    url='https://github.com/IPnett/puppet-yaml-enc',
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
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Systems Administration",
    ],
    keywords='yaml puppet external node classifier enc regular expression'\
             'regex re',
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
