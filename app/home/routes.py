# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound
import os
import sqlite3 as sql
import config
from datetime import date


@blueprint.route('/index')
@login_required
def index():
    today_date = date.today()
    basedir = config.Config.basedir 
    dbpath = os.path.join(basedir, 'database.db')
    print(dbpath)
    con = sql.connect(dbpath)
    print("Database successfully opened")
    con.row_factory = sql.Row
    cur = con.cursor()

    cur.execute("select * from reports")
    all_reports = cur.fetchall()
    print(len(all_reports))

    cur.execute("select * from reports where date = ? ", [str(today_date)])
    today_reports = cur.fetchall()
    print(len(today_reports))

    cur.execute("select * from reports where result = 'True Information'")
    true_reports = cur.fetchall()
    print(len(true_reports))

    cur.execute("select * from reports where result = 'Fake Information'")
    fake_reports = cur.fetchall()
    print(len(fake_reports))

    cur.execute("select * from reports where result = 'Unsure'")
    unsure_reports = cur.fetchall()
    print(len(unsure_reports))

    mobile_count = cur.execute("SELECT COUNT(DISTINCT mobile) from reports")
    mobile_count = cur.fetchone()[0]
    print(mobile_count)
    
    
    #if not current_user.is_authenticated:
    #    return redirect(url_for('base_blueprint.login'))

    counts = []
    counts.append(len(all_reports))
    counts.append(len(today_reports))
    counts.append(len(true_reports))
    counts.append(len(fake_reports))
    counts.append(len(all_reports)*2)
    counts.append(mobile_count)
    counts.append(len(unsure_reports))

    return render_template('index.html', all_reports = all_reports, today_reports = today_reports, true_reports = true_reports, fake_reports = fake_reports, all_count = counts, unsure_reports = unsure_reports)

@blueprint.route('/<template>')
def route_template(template):

    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    try:

        return render_template(template + '.html')

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500
