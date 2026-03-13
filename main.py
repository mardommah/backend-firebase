from backend.users import add_user, get_users, get_user_by_id, delete_user, update_user, is_admin
from backend.account import handler_login, handler_register
from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = '123456'


def admin_required(f):
    def wrap(*args, **kwargs):
        if 'user_email' not in session:
            flash("Anda harus login terlebih dahulu", "warning")
            return redirect(url_for('login'))
        
        if not is_admin(session['user_email']):
            flash("Akses ditolak. Halaman ini hanya untuk admin.", "danger")
            return redirect(url_for('index'))
        
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__
    return wrap

@app.route('/', methods=['GET'])
def index():
    users = get_users()
    print("Response users:", users)
    print("Users data:", users['data'])
    return render_template('index.html', users=users['data'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        return handler_login(request.form['email'], request.form['password'])
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle login logic here
        handler_register(
            request.form['username'], 
            request.form['email'], 
            request.form['password'], 
            request.form['confirm_password']
        )
    
    return render_template('register.html')


@app.route("/users", methods=['POST', 'GET'])
@admin_required
def users_page():
    users = get_users()
    return render_template('users.html', users=users['data'])


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.clear()
    flash("Berhasil logout", "success")
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)