from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Event
from app import db, bcrypt

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return redirect(url_for('main.home'))

@main.route('/home')
@login_required
def home():
    events = Event.query.all()
    return render_template('home.html', events=events)
