from webapp.model import db
from datetime import datetime


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_create = db.Column(db.DateTime, default=datetime.utcnow)
    date_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    comment = db.Column(db.Text, nullable=False)
    picture_id = db.Column(db.Integer(), db.ForeignKey('picture.id', ondelete='CASCADE'), index=True)

    def comments_count(self):
        return Comment.query.filter(Comment.id == self.id).count()

    def __repr__(self):
        return '<Comments {} {}>'.format(self.user_id, self.comment)
