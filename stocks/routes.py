from flask import render_template, url_for, jsonify, flash, redirect, request, send_file
from stocks import app
from stocks.forms import InputForm
import os
from stocks.yahoo import get_stocks
from werkzeug.utils import secure_filename

# pylint: skip-file

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = InputForm()
    if form.validate_on_submit():
        stock_data = form.stocks.data
        first_date = form.date_start.data
        last_date = form.date_end.data
        get_stocks(stock_data, first_date, last_date)
        flash('Successful!', 'success')
        redirect(url_for('home'))
    else:
        flash('Unsuccessful please try again', 'danger')
        redirect(url_for('home'))
    return render_template('home.html', title='Home', form=form)

@app.route("/downloads", methods=['GET', 'POST'])
def downloads():
    if request.method == 'POST':
        return send_from_directory('sampleDir.zip',
                attachment_filename='downloads.zip',
                as_attachment=True, cache_timeout=-1)