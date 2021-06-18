import configparser
import sys, os

sys.path.insert(0, os.path.abspath("../"))

from API import app, api, db

parser = configparser.ConfigParser()
parser.read('./conf/settings.ini')

db_settings = parser['db']

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_settings['db_user']}:{db_settings['db_passwd']}@{db_settings['db_host']}/{db_settings['db_name']}"

db.create_all()

if __name__ == '__main__':
    app.run(load_dotenv=True, host='127.0.0.1', port=6969)