import os
import uuid
from flask import Flask, jsonify, request, \
                  redirect, url_for, send_from_directory, \
                  abort, render_template, flash
from werkzeug.utils import secure_filename
from werkzeug.security import safe_join
import logging
from logging.handlers import RotatingFileHandler


from flask_sqlalchemy import SQLAlchemy
from api_controllers import *
from form import CommentForm
from table import Comments

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('APPTASK') or 'el-secreto'
app.config['WTF_CSRF_SECRET_KEY'] = os.getenv('WTFCSRFTASK') or 'el-secreto'


@app.route("/", methods=['GET', 'POST'])
def main():
    form = CommentForm(request.form)
    table = Comments(get_comments()['content'])
    table.border = True
    if request.method == 'POST' and form.validate():
        # save the album
        add_comment(form)
        flash('Comment created successfully!')
        return redirect('/')
    return render_template('index.html', form=form, table=table)
    


@app.route('/clients', methods=['GET'])
def api_clients():
    return jsonify(get_clients())

app.config['DEBUG'] = True

if __name__ == "__main__":
    app.run()
