serverless-config
=================

.. image:: https://img.shields.io/pypi/status/serverless-config.svg
    :target: https://pypi.org/project/serverless-config

.. image:: https://travis-ci.org/oharaandrew314/serverless-config.svg?branch=master
    :target: https://travis-ci.org/oharaandrew314/serverless-config
    
.. image:: https://img.shields.io/pypi/v/serverless-config.svg
    :target: https://pypi.org/project/serverless-config

.. image:: https://img.shields.io/pypi/l/serverless-config.svg
    :target: https://pypi.org/project/serverless-config

.. image:: https://img.shields.io/pypi/pyversions/serverless-config.svg
    :target: https://pypi.org/serverless-config
    
.. image:: https://codecov.io/github/oharaandrew314/serverless-config/coverage.svg?branch=master
    :target: https://codecov.io/github/oharaandrew314/serverless-config
    :alt: codecov.io

A simple configuration client for AWS serverless Python systems.

There is also a `jvm version <https://github.com/oharaandrew314/aws-lambda-config-jvm>`_.

Installation
------------

.. code-block:: bash

    pip install serverless-config

or

.. code-block:: bash

    pipenv install serverless-config

AWS lambda includes *boto3* in its environment, so *serverless-config* does not include it as a dependency in order to decrease the deployment package size.
If you wish to use *serverless-config* locally, be sure to install *boto3* as well.


Quickstart
----------

.. code-block:: python

    from serverless_config import default_config
    config = default_config()

    string_prop = config.get_str('string_prop')
    int_prop = config.get_int('missing_int_prop', default_value=123)
    secret_prop = config.get_str('secret_prop', WithDecryption=True)

The default config will search for a parameter with the following order of precedence: **System Environment**, **AWS SSM Parameter Store**.  You can learn more about them below.

Supported Config Sources
------------------------

System Environment
~~~~~~~~~~~~~~~~~~

The System environment is a good place to store microservice-specific parameters.  They are set on the lambda function itself.

.. code-block:: python

    from serverless_config import EnvConfig
    config = EnvConfig()
    config.get_str('string_prop')

AWS SSM Parameter Store
~~~~~~~~~~~~~~~~~~~~~~~

SSM is perfect for storing parameters that are shared across microservices, and for storing encrypted secrets.  It is fully managed, and does not require any configuration to get started.

**Note**: the IAM role requires the `AmazonSSMReadOnlyAccess` policy to get properties from SSM.

.. code-block:: python

    from serverless_config import SsmConfig
    config = SsmConfig()
    config.get_str('string_prop')

A secret can optionally be decrypted in transit.  That way, you do not need to worry about configuring your IAM role for access to the KMS Key.

.. code-block:: python

    from serverless_config import SsmConfig
    config = SsmConfig()
    config.get_str('string_prop', WithDecryption=True)


Composite Configs
~~~~~~~~~~~~~~~~~

The **default_config** will first search in the **system environment**.  If the  parameter is not there, then it will search in **AWS SSM**.

.. code-block:: python

    from serverless_config import default_config
    config = default_config()

Custom Configs
~~~~~~~~~~~~~~

You can even implement your own custom configs and composite configs!

.. code-block:: python

    from serverless_config import ConfigBase, CompositeConfig, EnvConfig

    class DictConfig(ConfigBase):

        def __init__(self, prop_dict):
            self.prop_dict = prop_dict

        def get_str(prop_name, default_value=None):
            if prop_name in self.prop_dict:
                return self.prop_dict[prop_name]
            elif default_value:
                return default_value

            # You must raise a ValueError if the property is not found
            raise ValueError('Property not found: ' + prop_name)

    # You can make a standalone custom config
    props = dict(foo='bar', toll='troll')
    map_config = DictConfig(props)

    # And you can make a custom composite config with your new config
    custom_config = CompositeConfig(map_config, EnvConfig())
    
Caching
-------

The **default_config** will cache properties for 5 minutes.  If you wish to use a specific or custom config, you can wrap the **CachedConfig** around it.

.. code-block:: python

    from serverless_config import default_config
    
    config = default_config()
    value = config.get_str('prop')  # getting value from env and ssm
    value = config.get_str('prop')  # getting cached value
    
.. code-block:: python

    from datetime import timedelta
    from serverless_config import EnvConfig, SsmConfig, CachedConfig, CompositeConfig
    
    CachedConfig(SsmConfig())  # config with default 5 minute cache duration
    CachedConfig(SsmConfig(), timedelta(hours=1)  # config with 1 hour cache duration
    CachedConfig(CompositeConfig(SsmConfig(), EnvConfig()))  # you can even cache a composite config!
