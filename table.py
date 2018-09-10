from flask_table import Table, Col
 
 
class Comments(Table):
    id = Col('Id', show=False)
    comment = Col('comment')
    timestamp = Col('timestamp')
    ip = Col('ip')