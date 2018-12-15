from flask import Flask, json, Response, render_template, flash, \
    redirect, jsonify, url_for, current_app
# from flask_mail import Mail, Message
# from threading import Thread
import os
import configparser
import logging
from logging.handlers import RotatingFileHandler
from views import quality, validation, reporting

app = Flask(__name__)
app.register_blueprint(quality.quality, url_prefix="/quality")
app.register_blueprint(validation.validation, url_prefix="/validation")
app.register_blueprint(reporting.reporting, url_prefix="/reporting")

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

# app.config['MAIL_SERVER'] = config['PROD']['MAIL_SERVER']
# app.config['MAIL_PORT'] = config['PROD']['MAIL_PORT']
# app.config['MAIL_USE_SSL'] = config['PROD']['MAIL_USE_SSL']
# app.config['MAIL_USERNAME'] = config['PROD']['MAIL_USERNAME']
# app.config['MAIL_PASSWORD'] = config['PROD']['MAIL_PASSWORD']
# mail = Mail(app)


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template("index.html", title="Home")
    # return render_template("index.html", title="Home", image=None)


# @app.route('/events', methods=['GET'])
# def events():
#     event = db.get_events()
#     return render_template('schedule.html', title='Events', events=event)


# @app.route('/registration', methods=['GET', 'POST'])
# def registration():
#     events = []
#     for data in db.get_events():
#         events.append((data["week"],
#                        f"Week: {data['week']} Event: {data['name']} Cost: ${data['cost']}"))
#     form = forms.RegisterForm()
#     form.classes_selected.choices = events
#     if form.validate_on_submit():
#         try:
#             cleaned_data = cleaning.clean_form(form, db=db)
#             sheets.addto_master(cleaned_data)  # googlesheets update here
#             # TODO: Add paypal creation here - not this go around
#             db.register_user(db_input=cleaned_data)
#             cc_emails = emails.format_recipients(other=cleaned_data["otherEmails"])
#
#             msg = Message(subject="Registration",
#                           sender=app.config['MAIL_USERNAME'],
#                           recipients=[cleaned_data['primaryEmail']],
#                           cc=cc_emails,)
#
#
#             msg.html = render_template('email/confirmation.html',
#                                        to=cleaned_data['parentFirst'],
#                                        child=cleaned_data['childFirst'],
#                                        total=cleaned_data['totalCost'],
#                                        classes=cleaned_data['classes'],
#                                        fee=fee)
#             # print(f'{cleaned_data["registrationFee"]}')
#             Thread(target=emails.send_async_email, args=(app, msg, mail)).start()
#             flash([f'Registration successful for {cleaned_data["childFirst"]}!  You will receive'
#                   f' an email shortly with your schedule, cost, and additional information.'])
#             return redirect('/events')
#         except Exception as err:
#             flash([f'Registration failed for {form.child_first_name.data}. '
#                    f'Please try again. If the issue persists, contact us.'])
#             app.logger.warning(f"{form.child_first_name.data} {form.child_last_name.data}: {err}")
#
#     return render_template('registration.html', title='Registration', form=form)


# @app.route('/blog')
# def blog():
#     # collections = db.return_collections()
#     return render_template('index.html', title='Blog')


# @app.route('/documents', methods=['GET', 'POST'])
# def documents():
#     events = []
#     for data in db.get_events():
#         events.append((data["week"], f"Week: {data['week']} Event: {data['name']} Cost: ${data['cost']}"))
#     form = forms.RegisterForm()
#     form.classes_selected.choices = events
#     if form.validate_on_submit():
#         return redirect('/documents')
#     return render_template('test.html', title='Forms', form=form)


# Configuration
if __name__ == '__main__':
    app.config['DEBUG'] = config['TEST']['DEBUG']
    # app.config['DB_URI'] = config['PROD']['DB_URI']
    app.config['SECRET_KEY'] = config['TEST']['SECRET_KEY']
    app.run("0.0.0.0")
else:
    # app.config['DB_URI'] = config['PROD']['DB_URI']
    app.config['SECRET_KEY'] = config['PROD']['SECRET_KEY']
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/netthings.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Melspage startup')
