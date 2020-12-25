"""
This script runs the flask_demo application using a development server.
"""

from os import environ
from flask_demo import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
