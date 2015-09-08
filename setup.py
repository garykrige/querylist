import sys

from setuptools import setup, find_packages

import querylist

# If we're using Python 2.7 or higher, we don't need unittest2.
unittest2_module = 'unittest2<1.2' if sys.version_info < (2, 7) else ''


setup(
    name='querylist',
    version=querylist.__version__,
    url='https://github.com/thomasw/querylist',
    download_url='https://github.com/thomasw/querylist/downloads',
    author=querylist.__author__,
    author_email='thomas.welfley+querylist@gmail.com',
    description='This package provides a QueryList class with django '
                'ORM-esque filtering, excluding, and getting for lists. It '
                'also provides BetterDict, a dot lookup/assignment capable '
                'wrapper for dicts that is 100% backwards compatible.',
    packages=find_packages(),
    tests_require=[
        'nose>=1.3.6,<1.4',
        'spec>=1.2.2,<1.3',
        unittest2_module
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
    ],
    test_suite='nose.collector',
)
