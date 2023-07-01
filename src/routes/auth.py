from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash

from src.database.user import User
from src.database.session import get_db_session

# Blueprint for auth routes
auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = False
        with get_db_session() as session:
            user = session.query(User).filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect('/')
        else:
            flash('Incorrect credentials. Please try again.', 'error')

    return render_template('html/login.jinja')


@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')
