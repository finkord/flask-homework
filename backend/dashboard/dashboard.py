from flask import Blueprint, jsonify, request
from flask import render_template

from .db import get_db

bp = Blueprint("dashboard", __name__)

def get_groupped_links():
    db = get_db()
    groups = db.execute('SELECT * FROM groups').fetchall()
    data = []
    for group in groups:
        items = db.execute('SELECT * FROM links WHERE group_id = ?', (group['id'],)).fetchall()
        data.append({
            'id': group['id'],
            'name': group['group_name'],
            'icon': group['icon'],
            'items': [{'name': item['name'], 'url': item['link'], 'logo': item['logo']} for item in items]
        })
    return {'groups': data}

@bp.route("/links", methods=['GET'])
def get_links():
    # Return all links
    db = get_db()
    links = db.execute('SELECT * FROM links').fetchall()
    return jsonify([{'id': link['id'], 'name': link['name'], 'url': link['link'], 'logo': link['logo']} for link in links])

@bp.route("/links/groupped", methods=['GET'])
def get_links_groupped():
    # Return all links groupped by group
    return jsonify(get_groupped_links())

@bp.route('/links', methods=['POST'])
def add_link():
    db = get_db()
    data = request.form

    if not data:
        return jsonify({"error": "No data received"}), 400

    db.execute('INSERT INTO links (name, link, logo, group_id) VALUES (?, ?, ?, ?)',
               (data.get('link_name', ''), data.get('link_url', ''), data.get('link_logo', None), data.get('group', '')))
    db.commit()

    return jsonify({"message": "Link added successfully"})
    # Add a new link 

@bp.route('/groups', methods=['GET'])
def get_groups():
    db = get_db()
    groups = db.execute('SELECT * FROM groups').fetchall()
    return jsonify({
        "message": "Groups",
        "groups": [dict(group) for group in groups]  
    })
    # Return all groups

@bp.route('/groups', methods=['POST'])
def add_group():
    db = get_db()
    data = request.json
    db.execute(
    'INSERT INTO groups (group_name, icon) VALUES (?, ?)',
    (data['new_group_name'], data['new_group_icon']))
    db.commit()
    return jsonify({"message": "Group added to database"})
    # Add a new group

