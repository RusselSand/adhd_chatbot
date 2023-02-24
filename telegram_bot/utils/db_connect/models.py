from gino import Gino
from sqlalchemy import func

db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.String, primary_key=True)
    user_account = db.Column(db.String)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user_email = db.Column(db.String)
    user_password_hash = db.Column(db.String)


class Step(db.Model):
    __tablename__ = 'steps'

    step_id = db.Column(db.Integer, primary_key=True)
    step_name = db.Column(db.String)

class Statistic(db.Model):
    __tablename__ = 'statistics'

    stats_id = db.Column(db.String, primary_key=True)
    session_id = db.Column(db.String)
    step_id = db.Column(db.Integer, db.ForeignKey('steps.step_id'))
    previous_step_id = db.Column(db.Integer, db.ForeignKey('steps.step_id'))
    step_date = db.Column(db.DateTime(timezone=True), default=func.now())


