from flask import Blueprint, redirect, render_template, request, send_from_directory

api_views = Blueprint('api_views', __name__, template_folder='../templates')

@api_views.route('/', methods=['GET'])
def get_login_page():
    return render_template('login.html')

@api_views.route('/signup')
def get__signup_page():
    return render_template('signup.html')