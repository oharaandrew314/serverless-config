'''setup.py'''

from setuptools import setup

with open('README.md', 'r') as f:
    README = f.read()

setup(
    name='serverless-config',
    version='0.1.0',

    packages=['serverless_config', 'tests'],

    # dependencies:
    install_requires=['boto3'],

    # PyPI metadata
    author='Andrew O\'Hara',
    author_email='andrew@andrewohara.io',
    description='A configuration client for AWS serverless Python systems',
    long_description=(README),
    license='MIT',
    # keywords = '',
    url='https://github.com/oharaandrew314/serverless-config/',

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    test_suite='tests'
)
