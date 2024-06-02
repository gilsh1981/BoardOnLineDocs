from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint('main', __name__)

@main.route('/home')
@login_required
def home():
    return render_template('home.html')
# app/main/views.py

@main.route('/events')
@login_required
def get_events():
    events = Event.query.all()
    event_list = []
    for event in events:
        event_list.append({
            'title': event.title,
            'start': event.start.isoformat(),
            'end': event.end.isoformat() if event.end else None,
            'url': url_for('main.event', event_id=event.id)
        })
    return jsonify(event_list)
