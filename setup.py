'''setup.py'''

from setuptools import setup

README_FILENAME = 'README.rst'

with open(README_FILENAME, 'r') as f:
    README = f.read()

setup(
    name='serverless-config',
    version='0.3.1',
    packages=['serverless_config'],

    # PyPI metadata
    author='Andrew O\'Hara',
    author_email='andrew@andrewohara.io',
    description='A configuration client for AWS serverless Python systems',
    long_description=(README),
    license='MIT',
    url='https://github.com/oharaandrew314/serverless-config/',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ]
)
