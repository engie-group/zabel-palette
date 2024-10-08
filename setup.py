# Copyright (c) 2020-24 Martin Lafaix (martin.lafaix@external.engie.com)
#
# This program and the accompanying materials are made
# available under the terms of the Eclipse Public License 2.0
# which is available at https://www.eclipse.org/legal/epl-2.0/
#
# SPDX-License-Identifier: EPL-2.0

from setuptools import setup, find_namespace_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='zabel-palette',
    version='0.1.0',
    description='The Zabel **palette** library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/engie-group/zabel-palette',
    author='Martin Lafaix',
    author_email='martin.lafaix@external.engie.com',
    license='Eclipse Public License 2.0',
    packages=find_namespace_packages(include=['zabel.*']),
    install_requires=[],
    extras_require={'all': ['psycopg2']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
    ],
    python_requires='>= 3.8.0',
)
