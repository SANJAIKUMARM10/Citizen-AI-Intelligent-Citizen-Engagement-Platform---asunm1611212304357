from .extensions import db
from datetime import datetime

class Concern(db.Model):
    __tablename__ = 'concerns'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String(20), default='neutral')
    status = db.Column(db.String(20), default='open')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'sentiment': self.sentiment,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

class ChatMessage(db.Model):
    __tablename__ = 'chat_messages'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(10), nullable=False)  # 'user' or 'assistant'
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'role': self.role,
            'content': self.content,
            'created_at': self.created_at.isoformat()
        }
