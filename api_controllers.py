from functools import wraps
from app import *
from models import *
from sqlalchemy import desc


# GET controllers
def get_comments():
    comments = Comment.query.order_by(desc(Comment.timestamp)).all()
    comments_array = []
    for comment in comments:
        comment_dict = {
                     "comment": comment.comment,
                     "timestamp": comment.timestamp,
                     "ip": comment.ip
                     }
        comments_array.append(comment_dict)
    return {"content": comments_array}

# POST controllers
def add_comment(form):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    comment = Comment()

    comment.comment = form.comment.data
    comment.ip = request.remote_addr

    # Add the new client to the database
    db.session.add(comment)
 
    # commit the data to the database
    db.session.commit()