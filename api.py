from flask import Blueprint, jsonify, request
from ..models import Concern, ChatMessage
from ..extensions import db
from ..services.llm_adapter import ask

bp = Blueprint('api', __name__)

@bp.route('/concerns', methods=['GET'])
def list_concerns():
    items = Concern.query.order_by(Concern.created_at.desc()).limit(200).all()
    return jsonify([i.to_dict() for i in items])

@bp.route('/chat', methods=['POST'])
def api_chat():
    payload = request.get_json() or {}
    q = payload.get('q','')
    if not q:
        return jsonify({'error':'no question provided'}), 400
    reply = ask(q)
    msg = ChatMessage(role='user', content=q)
    db.session.add(msg)
    db.session.commit()
    resp = ChatMessage(role='assistant', content=reply)
    db.session.add(resp)
    db.session.commit()
    return jsonify({'question':q, 'reply': reply})
