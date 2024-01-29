from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.db import get_db
bp = Blueprint('activity', __name__)

def get_activity(id):
    activity = get_db().execute(
        'Select * from activity'
        ' WHERE id = ?',
        (id,)
    ).fetchone()
    if activity is None:
        abort(404, f"Post id {id} doesn't exist.")
    return activity
@bp.route('/')

def index():
    db = get_db()
    activities = db.execute("Select * from activity").fetchall()
    return render_template("activity/index.html", activities = activities)

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    activity = get_activity(id)
    if request.method == 'POST':
        name = request.form['name']
        duration = request.form['duration']
        distance = request.form['distance']
        averageHR = request.form['averageHR']
        calories = request.form['calories']
        error = None
        if not name:
            error = 'Name is required.'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE activity SET name = ?, distance = ?, duration = ?, averageHR = ?, calories = ?'
                ' WHERE id = ?',
                (name, distance, duration, averageHR, calories, id)
            )
            db.commit()
            return redirect(url_for('activity.index'))
    return render_template('activity/update.html', activity=activity)

@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    activity = get_activity(id)
    db = get_db()
    db.execute('Delete from activity where id = ?', (id,))
    db.commit()
    return redirect(url_for('activity.index'))