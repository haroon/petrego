"""This module will contain version 2 extension of the API baseclass.
"""


from .api import API, request

class APIV2(API):
    """Class used to register version 2 of the API.
    """
    def __init__(self, dbhelper, output_formatter,
                    name, import_name, **kwargs):
        """Set the URL prefix for the version 2 of the API.
        """
        kwargs['url_prefix'] = '/api/v2'
        API.__init__(self, dbhelper, output_formatter,
                        name, import_name, **kwargs)

    def getpets(self, first_name, last_name):
        """Implementation of the version 2 of the getpets API.
        """
        res = self.dbhelper.get_pets(first_name, last_name)
        columns = \
            ['first_name', 'last_name', 'pet_name', 'pet_type', 'food_name']
        return self.output_formatter.format_data(columns, res)
