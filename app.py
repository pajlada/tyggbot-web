#!/usr/bin/env python3

import sys
import configparser
import json
import math
from datetime import datetime

from flask import Flask, render_template
import pymysql

app = Flask(__name__)

config = configparser.ConfigParser()

if len(sys.argv) > 1:
    res = config.read(sys.argv[1])
else:
    res = config.read('config.ini')

if len(res) == 0:
    print('config.ini missing.')
    sys.exit(0)

try:
    sqlconn = pymysql.connect(unix_socket=config['sql']['unix_socket'], user=config['sql']['user'], passwd=config['sql']['passwd'], db=config['sql']['db'], charset='utf8')
except pymysql.err.OperationalError as e:
    error_code, error_message = e.args
    if error_code == 1045:
        print('Access denied to database with user \'{0}\'. Review your config file.'.format(config['sql']['user']))
    elif error_code == 1044:
        print('Access denied to database \'{0}\' with user \'{1}\'. Make sure the database \'{0}\' exists and user \'{1}\' has full access to it.'.format(config['sql']['db'], config['sql']['user']))
    else:
        print(e)
    sys.exit(1)


def get_cursor():
    sqlconn.ping()
    return sqlconn.cursor(pymysql.cursors.DictCursor)


def get_normal_cursor():
    sqlconn.ping()
    return sqlconn.cursor()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/commands')
def commands():
    cursor = get_cursor()
    query = 'SELECT * FROM `tb_commands` WHERE `enabled`=1'
    cursor.execute(query)
    custom_commands = []
    point_commands = []
    moderator_commands = []
    for command in cursor:
        action = json.loads(command['action'])
        command['aliases'] = ['!' + s for s in command['command'].split('|')]
        for alias in command['aliases']:
            alias = '!' + alias
        if action['type'] in ['say', 'me', 'whisper']:
            command['output'] = action['message']

        command['arguments'] = []

        try:
            description = json.loads(command['description'])
            if 'description' in description:
                command['description'] = description['description']
            if 'usage' in description:
                if description['usage'] == 'whisper':
                    for x in range(0, len(command['aliases'])):
                        alias = command['aliases'][x]
                        command['aliases'][x] = '/w {0} {1}'.format(config['bot']['full_name'], alias)
                    for alias in command['aliases']:
                        command['aliases']
                command['description'] = description['description']
            if 'arguments' in description:
                command['arguments'] = description['arguments']
            if 'hidden' in description:
                if description['hidden'] is True:
                    continue
        except:
            pass

        if command['level'] > 100:
            moderator_commands.append(command)
        else:
            if command['cost'] > 0:
                point_commands.append(command)
            else:
                if 'output' in command:
                    custom_commands.append(command)
    cursor.close()
    sqlconn.commit()
    try:
        return render_template('commands.html',
                custom_commands=custom_commands,
                point_commands=point_commands,
                moderator_commands=sorted(moderator_commands, key=lambda x: x['level']))
    except Exception as e:
        print(e)


@app.route('/decks')
def decks():
    cursor = get_cursor()
    cursor.execute('SELECT * FROM `tb_deck` ORDER BY `last_used` DESC, `first_used` DESC')
    decks = []
    cursor.close()
    sqlconn.commit()
    for deck in cursor:
        decks.append(deck)
    return render_template('decks.html',
            decks=decks)


@app.route('/user/<username>')
def user_profile(username):
    cursor = get_cursor()
    print(username)
    cursor.execute('SELECT * FROM `tb_user` WHERE `username`=%s', [username])
    user = cursor.fetchone()
    if user:
        return render_template('user.html',
                user=user)
    else:
        return render_template('no_user.html'), 404


@app.route('/points')
def points():
    cursor = get_cursor()
    cursor.execute('SELECT * FROM `tb_user` ORDER BY `points` DESC, `username` ASC LIMIT 30')
    top_30_users = cursor.fetchall()
    cursor.close()
    sqlconn.commit()
    return render_template('points.html',
            top_30_users=top_30_users)


@app.route('/stats')
def stats():
    cursor = get_cursor()
    cursor.execute('SELECT * FROM `tb_commands` ORDER BY `num_uses` DESC LIMIT 15')
    top_5_commands = cursor.fetchall()
    cursor.close()
    sqlconn.commit()

    return render_template('stats.html',
            top_5_commands=top_5_commands)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/discord')
def discord():
    return render_template('discord.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.route('/clr/overlay/<widget_id>')
def clr_overlay(widget_id):
    print(widget_id)
    if widget_id == config['clr-overlay']['widget_id']:
        return render_template('clr/overlay.html',
                widget={})
    else:
        return render_template('errors/404.html'), 404


@app.errorhandler(Exception)
def all_exception_handler(error):
    print(error)
    return 'Error', 500


@app.template_filter()
def number_format(value, tsep=',', dsep='.'):
    s = str(value)
    cnt = 0
    numchars = dsep + '0123456789'
    ls = len(s)
    while cnt < ls and s[cnt] not in numchars:
        cnt += 1

    lhs = s[:cnt]
    s = s[cnt:]
    if not dsep:
        cnt = -1
    else:
        cnt = s.rfind(dsep)
    if cnt > 0:
        rhs = dsep + s[cnt + 1:]
        s = s[:cnt]
    else:
        rhs = ''

    splt = ''
    while s != '':
        splt = s[-3:] + tsep + splt
        s = s[:-3]

    return lhs + splt[:-1] + rhs


default_variables = {
        'bot': dict(config['bot']),
        'site': dict(config['site']),
        'streamer': dict(config['streamer'])
        }


@app.context_processor
def inject_default_variables():
    return default_variables


@app.after_request
def add_header(response):
    response.cache_control.max_age = 10
    return response


def time_since(t1, t2, format='long'):
    time_diff = t1 - t2
    if format == 'long':
        num_dict = ['day', 'hour', 'minute', 'second']
    else:
        num_dict = ['d', 'h', 'm', 's']
    num = [math.trunc(time_diff / 86400),
           math.trunc(time_diff / 3600 % 24),
           math.trunc(time_diff / 60 % 60),
           round(time_diff % 60, 1)]

    i = 0
    j = 0
    time_arr = []
    while i < 2 and j < 4:
        if num[j] > 0:
            if format == 'long':
                time_arr.append('{0:g} {1}{2}'.format(num[j], num_dict[j], 's' if num[j] > 1 else ''))
            else:
                time_arr.append('{0}{1}'.format(num[j], num_dict[j]))
            i += 1
        j += 1

    if format == 'long':
        return ' and '.join(time_arr)
    else:
        return ''.join(time_arr)


@app.template_filter('time_ago')
def time_ago(t):
    return time_since(datetime.now().timestamp(), t.timestamp())

if __name__ == '__main__':
    app.run(debug=True)
