from App.models import User, Scores
from App.database import db
from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

def get_all_scores():
    return Scores.query.all()

def get_desc_order():
    return Scores.query.order_by(desc(Scores.score))

def create_score(username, score):
    newscore = Scores(username=username,score=score)
    try:
        db.session.add(newscore)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return 'fail'
    return 'pass'

def get_all_scores_json():
    scores = Scores.query.all()
    if not scores:
        return []
    scores = [score.toDict() for score in scores]
    return scores

def delete(id):
    score = Scores.query.filter_by(id = id).first()
    db.session.delete(score)
    db.session.commit()
    return 'pass'
