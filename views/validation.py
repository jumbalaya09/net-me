from flask import Blueprint, render_template

validation = Blueprint('validation', __name__)


@validation.route('/')
@validation.route('/index')
@validation.route('/home')
def home():
    return render_template('/validation/index.html')


@validation.route('/icmp')
def v_icmp():
    return render_template('/validation/index.html')


@validation.route('/snmp')
def v_snmp():
    return render_template('/validation/index.html')


@validation.route('/api')
def v_api():
    return render_template('/validation/index.html')
