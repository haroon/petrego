"""This module will contain version 1 extension of the API baseclass.
"""
from .api import API

class APIV1(API):
    """Class used to register version of the API.
    """
    def __init__(self, dbhelper, output_formatter,
                    name, import_name, **kwargs):
        """Set the URL prefix for the version 1 of the API.
        """
        kwargs['url_prefix'] = '/api/v1'
        API.__init__(self, dbhelper, output_formatter,
                        name, import_name, **kwargs)
