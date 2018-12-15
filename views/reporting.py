from flask import Blueprint, render_template

reporting = Blueprint('reporting', __name__)


@reporting.route('/')
@reporting.route('/index')
@reporting.route('/home')
def home():
    return render_template('/reporting/index.html')


@reporting.route('/excel')
def r_excel():
    return render_template('/reporting/index.html')


@reporting.route('/csv')
def r_csv():
    return render_template('/reporting/index.html')


@reporting.route('/graphs')
def r_graphs():
    return render_template('/reporting/index.html')
