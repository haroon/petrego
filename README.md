# Implementation of a flask-based RESTful API
A flask-driven restful API for PetRego pet registration service.


## Dependencies
* **[Python3](https://www.python.org/)** - Version 3 of the Python programming language
* **[Flask](http://flask.pocoo.org/)** - A microframework for web application development written in Python programming language
* **[SQLite](https://www.sqlite.org/)** - A small and self-contained SQL database engine.

## Installation / Usage
* You need Python3 installed on your computer. On OpenSuse Linux, e.g., you can install Python3 as follows:

    ```
        $ sudo zypper install python3
    ```

* Details for other platforms can be found on the [Python website](https://www.python.org).
* Once you have install Python, you might want to create a virtual environment.

    ```
        $ python3 -m venv <your_venv_name>
    ```

* For the rest of this document, we will assume you have activated your virtual environment.

    ```
        $ source </path/to/your/venv>/bin/activate
    ```

* Git clone this repo to your PC

    ```
        $ git clone git@github.com:haroon/petrego.git
    ```

* #### Dependencies
    1. CD into the cloned repo

        ```
            $ cd petrego
        ```

    2. Install dependencies:

        ```
            $ pip install -r requirements.txt
        ```

* #### Environment Variables
    Set up FLASK environment:

    ```
        $ export FLASK_APP=petrego
    ```

* #### Initialize database
    Initialize the database by issuing following command

    ```
    $ flask init-db
    ```

* #### Run
    On your terminal, run the app with following command:

    ```
    $ flask run
    ```

    You can access the help (this document) by going to

    [http://localhost:5000/help/about/](http://localhost:5000/help/about/)

    API documentation can be accessed at (replace the version after /api/ to the API version of your choice):

    [http://localhost:5000/help/api/v1/](http://localhost:5000/help/api/v1/)


## Testing
* This app uses Python's *unittest* framework. You can test the application by running the following command:

    ```
    $ python3 -m unittest discover tests
    ```
