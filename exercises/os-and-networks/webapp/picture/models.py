from webapp.model import db
from datetime import datetime


class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    date_create = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'), index=True)
    comments = db.relationship('Comment', backref='picture')

    def __repr__(self):
        return '<Pictures {} {}>'.format(self.name, self.url)