'''Base Config for others to implement'''


class ConfigBase(object):
    '''Config Base Class'''

    def get_str(self, prop_name, default_value=None, **kwargs):
        ''' Get the string property by name.

            Raises ValueError if the property is not found.
        '''
        raise NotImplementedError()

    def get_int(self, prop_name, default_value=None, **kwargs):
        ''' Get the int property by name.

            Raises ValueError if the property is not found,
            or if the property value is not an int.
        '''
