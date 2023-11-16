from flaskr.extensions import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    """
    用户表
    """
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    rank = db.Column(db.Integer, nullable=False, default=1)
    avatar = db.Column(db.LargeBinary)

    def get_id(self):
        try:
            return self.user_id
        except AttributeError:
            raise NotImplementedError(
                'No `id` attribute - override `get_id`') from None


class Video(db.Model):
    """
    视频表
    """
    video_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    video_url = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False,
                            default=datetime.now)
    sort = db.Column(db.String(50), nullable=False)
