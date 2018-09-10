import os
from flask_sqlalchemy import SQLAlchemy
from app import app


POSTGRES = {
    'user': '***',
    'pw': '****',
    'db': '****',
    'host': 'localhost:5432',
}

# PostgreSQL configuration
POSTGRES_USER = os.getenv('PGUSERTA') or POSTGRES['user']
POSTGRES_URL = os.getenv('PGURL') or POSTGRES['host']
POSTGRES_PW = os.getenv('PGPWTA') or POSTGRES['pw']
POSTGRES_DB = os.getenv('PGDBTA') or POSTGRES['db']

# DB URL
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)


app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning



db = SQLAlchemy(app)
# db.init_app(app)
