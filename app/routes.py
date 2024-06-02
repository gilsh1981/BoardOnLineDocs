from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('index.html')
# app/main/views.py

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app.models import Event, Meeting, Task, db

main = Blueprint('main', __name__)

@main.route('/home')
@login_required
def home():
    return render_template('home.html')

@main.route('/events')
@login_required
def events():
    events = Event.query.all()
    return render_template('events.html', events=events)

@main.route('/meetings')
@login_required
def meetings():
    meetings = Meeting.query.all()
    return render_template('meetings.html', meetings=meetings)

@main.route('/tasks')
@login_required
def tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@main.route('/event/new/<date>', methods=['GET', 'POST'])
@login_required
def new_event(date):
    if request.method == 'POST':
        title = request.form['title']
        start = datetime.strptime(request.form['start'], '%Y-%m-%dT%H:%M')
        end = datetime.strptime(request.form['end'], '%Y-%m-%dT%H:%M')
        event = Event(title=title, start=start, end=end, type='event')
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('main.events'))
    return render_template('new_event.html', date=date)

@main.route('/meeting/new/<date>', methods=['GET', 'POST'])
@login_required
def new_meeting(date):
    if request.method == 'POST':
        title = request.form['title']
        start = datetime.strptime(request.form['start'], '%Y-%m-%dT%H:%M')
        end = datetime.strptime(request.form['end'], '%Y-%m-%dT%H:%M')
        meeting = Meeting(title=title, start=start, end=end)
        db.session.add(meeting)
        db.session.commit()
        return redirect(url_for('main.meetings'))
    return render_template('new_meeting.html', date=date)

@main.route('/task/new/<date>', methods=['GET', 'POST'])
@login_required
def new_task(date):
    if request.method == 'POST':
        title = request.form['title']
        start = datetime.strptime(request.form['start'], '%Y-%m-%dT%H:%M')
        end = datetime.strptime(request.form['end'], '%Y-%m-%dT%H:%M')
        task = Task(title=title, start=start, end=end)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('main.tasks'))
    return render_template('new_task.html', date=date)

@main.route('/event/<int:event_id>')
@login_required
def event(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('event.html', event=event)

@main.route('/meeting/<int:meeting_id>')
@login_required
def meeting(meeting_id):
    meeting = Meeting.query.get_or_404(meeting_id)
    return render_template('meeting.html', meeting=meeting)

@main.route('/task/<int:task_id>')
@login_required
def task(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template('task.html', task=task)
