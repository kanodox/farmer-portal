import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from . import auth

from . import db_handler

bp = Blueprint('items', __name__, url_prefix='/items')
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = db_handler.get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
@bp.route('/add', methods=('GET', 'POST'))
@auth.login_required
def add():
    if request.method == 'POST':
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        seller_name = request.form['seller']
        price = request.form['price']
        db = db_handler.get_db()
        error = None

        for param in [item_name, quantity, seller_name, price]:
            if param is None:
                error = f"{param} is required"

        if error is None:
            try:
                db.execute(
                    "INSERT INTO chain_data (item_name, quantity, seller_name, price) VALUES (?, ?,?, ?)",
                    (item_name, quantity, seller_name, price),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Error inserting item"

        flash(error)

    return render_template('items/add.html')
