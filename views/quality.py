from flask import Blueprint, render_template

quality = Blueprint('quality', __name__)


@quality.route('/')
@quality.route('/index')
@quality.route('/home')
def home():
    return render_template('/quality/index.html')


@quality.route('/routers')
def q_routers():
    return render_template('/quality/index.html')


@quality.route('/firewalls')
def q_fws():
    return render_template('/quality/index.html')


@quality.route('/switches')
def q_switches():
    return render_template('/quality/index.html')
