"""Implementation for JSON output formatter.
"""
from flask import jsonify

class JSONFormatter():
    """Implementation of formatting for API outputs.
    """
    @staticmethod
    def format_response(err_code, links_data=None):
        """Format POST/PUT/DELETE response.
        """
        resp = dict()

        if links_data:
            resp['links'] = \
                [{'href': link_data[0],
                  'rel': link_data[1],
                  'type' : link_data[2]} for link_data in links_data]

        return jsonify(resp), err_code

    @staticmethod
    def format_data(columns, res):
        """Format GET response.
        """
        resp = dict()
        results = [dict(zip(columns, row)) for row in res]

        if results:
            resp['data'] = results

        return jsonify(resp)
