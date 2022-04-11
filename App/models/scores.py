from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Scores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), db.ForeignKey('user.username'), nullable=False)
    score =  db.Column(db.Integer,unique=False,nullable=False)

    def __init__(self, username,score):
        self.username = username
        self.score = score

    def toDict(self):
        return{
            'id': self.id,
            'username': self.username,
            'score': self.score
        }
