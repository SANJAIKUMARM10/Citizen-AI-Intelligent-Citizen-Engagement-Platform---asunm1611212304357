from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import db
from ..models import Concern, ChatMessage
from ..services.sentiment import classify
from ..services.llm_adapter import ask

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/chat', methods=['GET','POST'])
def chat():
    if request.method == 'POST':
        question = request.form.get('message','').strip()
        if not question:
            flash('Please enter a message.', 'warning')
            return redirect(url_for('main.chat'))
        # persist user message
        user_msg = ChatMessage(role='user', content=question)
        db.session.add(user_msg)
        db.session.commit()
        # ask adapter for reply
        reply_text = ask(question)
        assistant_msg = ChatMessage(role='assistant', content=reply_text)
        db.session.add(assistant_msg)
        db.session.commit()
        return redirect(url_for('main.chat'))
    messages = ChatMessage.query.order_by(ChatMessage.created_at.desc()).limit(50).all()
    return render_template('chat_v2.html', messages=messages)

@bp.route('/report', methods=['GET','POST'])
def report():
    if request.method == 'POST':
        title = request.form.get('title','').strip()
        description = request.form.get('description','').strip()
        if not title or not description:
            flash('All fields required.', 'danger')
            return redirect(url_for('main.report'))
        sentiment = classify(description)
        c = Concern(title=title, description=description, sentiment=sentiment)
        db.session.add(c)
        db.session.commit()
        flash('Report received — thank you!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('report_v2.html')

@bp.route('/dashboard')
def dashboard():
    concerns = Concern.query.order_by(Concern.created_at.desc()).limit(100).all()
    stats = {'positive':0,'neutral':0,'negative':0}
    for c in concerns:
        stats[c.sentiment] = stats.get(c.sentiment,0) + 1
    return render_template('dashboard_v2.html', concerns=concerns, stats=stats)
