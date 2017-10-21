'''setup.py'''

from setuptools import setup

setup(
    name='serverless-config',
    version='0.1.0',

    packages=['serverless_config', 'tests'],

    # dependencies:
    install_requires=['boto3'],
    # tests_require=parse_requirements('requirements-test.txt'),

    # PyPI metadata
    author='Andrew O\'Hara',
    author_email='andrew@andrewohara.io',
    description='A configuration client for AWS serverless Python3 systems',
    license='MIT',
    # keywords = '',
    url='https://github.com/oharaandrew314/serverless-config/',

    #   long_description=(read('README.rst') +
    #                     read('CHANGES.txt') +
    #                     read('TODO.txt')),

    classifiers=['Development Status :: 4 - Beta',
                # 'Environment :: Web Environment',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: BSD License',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Programming Language :: Python :: 3.3',
                'Programming Language :: Python :: 3.4',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: Implementation :: PyPy',
                'Topic :: Internet',
                ('Topic :: Software Development :'
                ': Libraries :: Python Modules'),
                ],
    test_suite='tests'
)
