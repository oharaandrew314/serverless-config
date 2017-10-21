# serverless-config

A simple configuration client for AWS serverless Python3 systems.

## Quickstart

```python
from serverless_config import default_config
config = default_config()

string_prop = config.get_str('string_prop')
other_prop = condfig.get_str('missing_prop', default_value='other_prop')
```

The default config will search for a parameter with the following order of precedence: `System Environment`, `AWS SSM Parameter Store`.  You can learn more about them below.

## Supported Configuration Sources

### System Environment

The System environment is a good place to store microservice-specific parameters.  They are set on the lambda function itself.

```python
from serverless_config import env_config
config = env_config()
config.get_str('string_prop')
```

### AWS SSM Parameter Store

SSM is perfect for storing parameters that are shared across microservices.  It is fully managed, and does not require any configuration to get started.

**Note**: the IAM role requires the `AmazonSSMReadOnlyAccess` policy to get properties from SSM.

```python
from serverless_config import ssm_config
config = ssm_config()
config.get_str('string_prop')
```

### Composite configs, i.e. multiple configs, with an order of precedence

The `default_config` will first search in the `system environment`.  If the  parameter is not there, then it will search in `AWS SSM`.

```python
from serverlessa_config import default_config
config = default_config()
```

### Custom Configs

You can even implement your own custom configs and composite configs!

```python
from serverless_config import ConfigBase, custom_composite_config, env_config

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
custom_config = custom_composite_config(map_config, env_config())
```