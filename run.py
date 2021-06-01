import configparser
import os
import sys

from mflix.factory import create_app

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join('.ini')))
ENV = sys.argv[1] if len(sys.argv) > 1 else 'DEV'

if ENV not in config.sections():
    raise KeyError(f'{ENV} is not a valid environment. Use one of {config.sections()}')

if __name__ == '__main__':
    app = create_app()
    app.config['DEBUG'] = True
    app.config['MFLIX_DB_URI'] = config[ENV]['MFLIX_DB_URI']
    app.config['MFLIX_NS'] = config[ENV]['MFLIX_NS']
    app.config['SECRET_KEY'] = config[ENV]['SECRET_KEY']

    app.run()
