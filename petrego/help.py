"""This module contains implementation for about route. The about rout will
read README.md and display it to the user.
"""
import functools
import markdown
import os

from flask import Blueprint, current_app as app

from petrego.db import get_db

bp = Blueprint('help', __name__, url_prefix='/help/')

@bp.route('/about/', methods=['GET'])
def about():
    """README documentation for installtaion and testing the application.
    """
    with open(
    os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        # Read the content of the file
        content = markdown_file.read()
        # Convert to HTML
        return markdown.markdown(content)

@bp.route('/api/v1/', methods=['GET'])
def apiv1():
    """Documentation for version 1 of the API.
    """
    with open(
    os.path.dirname(app.root_path) + '/APIv1.md', 'r') as markdown_file:
        # Read the content of the file
        content = markdown_file.read()
        # Convert to HTML
        return markdown.markdown(content)

@bp.route('/api/v2/', methods=['GET'])
def apiv2():
    """Documentation for version 2 of the API.
    """
    with open(
    os.path.dirname(app.root_path) + '/APIv2.md', 'r') as markdown_file:
        # Read the content of the file
        content = markdown_file.read()
        # Convert to HTML
        return markdown.markdown(content)
