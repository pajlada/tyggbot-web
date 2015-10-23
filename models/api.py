from flask import Blueprint
from flask import jsonify
from flask import make_response
import pymysql


page = Blueprint('api', __name__)

sqlconn = False


def get_cursor():
    sqlconn.ping()
    return sqlconn.cursor(pymysql.cursors.DictCursor)

@page.route('/api/v1/user/<username>')
def get_user(username):
    cursor = get_cursor()
    cursor.execute('SELECT *, `points` as `user_points`, (SELECT COUNT(*)+1 FROM `tb_user` WHERE `points` > `user_points` ORDER BY `username` ASC) as `rank` FROM `tb_user` WHERE `username`=%s', [username])
    user = cursor.fetchone()
    if user:
        accessible_data = {
                'id': user['id'],
                'username': user['username'],
                'username_raw': user['username_raw'],
                'points': user['points'],
                'rank': user['rank'],
                'level': user['level'],
                'last_seen': user['last_seen'],
                'last_active': user['last_active'],
                'subscriber': user['subscriber'] == 1,
                'num_lines': user['num_lines'],
                'minutes_in_chat_online': user['minutes_in_chat_online'],
                'minutes_in_chat_offline': user['minutes_in_chat_offline'],
                'banned': user['banned'] == 1,
                'ignored': user['ignored'] == 1,
                }
        return jsonify(accessible_data)

    return make_response(jsonify({'error': 'Not found'}), 404)

def init(_sqlconn):
    global sqlconn
    sqlconn = _sqlconn
