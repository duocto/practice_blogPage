import datetime

from flask import Blueprint, Flask, request, render_template, make_response, jsonify, redirect, url_for, session
from blog_control.user_mgmt import User
from flask_login import login_user, current_user, logout_user

blog_abtest = Blueprint( 'blog', __name__ )


@blog_abtest.route('/set_email', methods=['GET','POST'])
def set_email():
    if request.method == 'GET':
        print( 'set_email', request.args.get('user_email'))
        return redirect(url_for('blog.test_blog'))
    else:
        user = User.create(request.form['user_email'], request.form['blog_id'])
        login_user(user, remember=True, duration=datetime.timedelta(days=365))

        return redirect(url_for('blog.blog_fullstack1'))

