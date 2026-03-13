from db import db_firestore
from flask import session, flash, redirect, url_for
from google.cloud.firestore_v1 import FieldFilter
from werkzeug.security import generate_password_hash, check_password_hash


users = db_firestore.collection('accounts')

def handler_login(email, password):
    # cek user apakah ada di database atau tidak
    user = users.where(filter=FieldFilter('email', '==', email)).stream()

    user_list = list(user)
    if len(user_list) == 0:
        flash("email tidak ditemukan", "danger")
        return redirect(url_for('login'))

    user_data = None
    for u in user_list:
        user_data = u.to_dict()
        break

    if user_data and check_password_hash(user_data['password'], password):
        session['user_email'] = email
        session['user_id'] = u.id
        flash("berhasil login", "success")
        return redirect(url_for('index'))
    else:
        flash("password salah", "danger")
        return redirect(url_for('login'))


def handler_register(username, email, password, confirm_password):
    user = list(users.where(filter=FieldFilter('email', '==', email)).stream())

    print(len(user))

    if len(user) > 0:
        flash("email sudah terdaftar", "danger")
        return redirect(url_for('register'))

    if password != confirm_password:
        flash("password tidak sama", "danger")
        return redirect(url_for('register'))

    users.add({
        "username": username,
        "email": email,
        "password": generate_password_hash(password)
    })

    flash("berhasil mendaftar", "success")
    return redirect(url_for('login'))
