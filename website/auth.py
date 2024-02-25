from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/affirmations')
def affirmations():
    return render_template('affirmations.html')