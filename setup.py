import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='naviance-client',

    version='0.0.1',

    description='A simple client for the Naviance SchoolSync REST API',

    long_description=LONG_DESCRIPTION,

    url='https://github.com/IronCountySchoolDistrict/naviance-client',

    author='Iron County School District',
    author_email='data@ironmail.org',

    license='MIT',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Topic :: Software Development',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='naviance schoolsync client rest',

    packages=find_packages(),

    install_requires=['requests'],

)
