import datetime

from flask import Blueprint, Flask, request, render_template, make_response, jsonify, redirect, url_for, session
from blog_control.user_mgmt import User
from blog_control.session_mgmt import BlogSession
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

        return redirect(url_for('blog.blog_fullstack'))


@blog_abtest.route('/logout')
def logout():
    User.delete( current_user.id )
    logout_user()
    return redirect(url_for( 'blog.blog_fullstack'))


@blog_abtest.route('blog_fullstack')
def blog_fullstack():
    if current_user.is_authenticated:
        webpage_name = BlogSession.get_blog_page( current_user.pageName )
        BlogSession.save_session_info( session['client_id'], current_user.email, webpage_name )
        return render_template( webpage_name, user_email=current_user.email )
    else:
        webpage_name = BlogSession.get_blog_page()
        BlogSession.save_session_info( session['client_id'], 'anonymous', webpage_name)
        return render_template( webpage_name )
    
