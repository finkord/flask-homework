import sqlite3
from datetime import datetime
import json

import click
from flask import current_app
from flask import g


def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """Clear existing data and create new tables."""
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))

    with current_app.open_resource("db_data.json") as f:
        data = json.load(f)

    print(data)

    cursor = db.cursor()

    # Insert groups and links
    for group in data['groups']:
        cursor.execute("INSERT INTO groups (group_name, icon) VALUES (?, ?)", (group['name'], group['icon']))
        group_id = cursor.lastrowid

        for item in group['items']:
            cursor.execute(
                "INSERT INTO links (name, link, logo, group_id) VALUES (?, ?, ?, ?)",
                (item['name'], item['url'], item['logo'], group_id)
            )
    db.commit()

@click.command("init-db")
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


sqlite3.register_converter("timestamp", lambda v: datetime.fromisoformat(v.decode()))


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
