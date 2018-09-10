from dbconfig import *
import datetime


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    ip = db.Column(db.Text, unique=False, nullable=False)

