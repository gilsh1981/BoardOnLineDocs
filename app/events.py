from flask import Blueprint, render_template

events = Blueprint('events', __name__)

@events.route('/events')
def event_list():
    return render_template('events.html')
