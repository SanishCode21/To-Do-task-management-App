from flask import render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, login_required, logout_user, current_user

from functools import wraps
from sqlalchemy import func
from flask import current_app as app
from application.models import *


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(email=email).first():
            flash("Email already registered", "danger")
            return render_template('register')

        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_pw) # type: ignore

        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully!", "success")
        return redirect(url_for('login'))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Logged in successfully!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials", "danger")
            return render_template('login')

    return render_template("login.html")

# Dashboard
#@app.route("/dashboard")
#@login_required
#def dashboard():
#    tasks = Task.query.filter_by(user_id=current_user.id).all()
#    return render_template("dashboard.html", tasks=tasks)


#Show all task to specific user.
@app.route("/dashboard")
@login_required
def dashboard():
    filter_type = request.args.get('filter', 'all')

    if filter_type == 'completed':
        tasks = Task.query.filter_by(user_id=current_user.id, is_complete=True).all()
    elif filter_type == 'pending':
        tasks = Task.query.filter_by(user_id=current_user.id, is_complete=False).all()
    else:
        tasks = Task.query.filter_by(user_id=current_user.id).all()

    return render_template("dashboard.html", tasks=tasks, filter_type=filter_type)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


@app.route("/task/add", methods=["GET", "POST"])
@login_required
def add_task():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        due_date_str = request.form.get("due_date")
        priority = request.form.get("priority")
        category = request.form.get("category")

        # Convert to datetime
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d') # type: ignore

        new_task = Task(
            title=title, # type: ignore
            description=description, # type: ignore
            due_date=due_date,  # type: ignore
            priority=priority,  # type: ignore
            category=category,  # type: ignore
            owner=current_user  # type: ignore
        )
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully!", "success")
        return redirect(url_for("dashboard"))

    return render_template("add_task.html")


@app.route("/task/<int:id>")
@login_required
def view_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash("Unauthorized access", "danger")
        return redirect(url_for('dashboard'))
    return render_template("view_task.html", task=task)


@app.route('/task/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash("Unauthorized access", "danger")
        return redirect(url_for("dashboard"))

    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        due_date_str = request.form['due_date']  # '2025-05-20'
        
        # Convert string to datetime
        task.due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        
        task.priority = request.form['priority']
        task.category = request.form['category']

        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('edit_task.html', task=task)


@app.route("/task/delete/<int:id>")
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash("Unauthorized access", "danger")
        return redirect(url_for("dashboard"))
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted!", "info")
    return redirect(url_for("dashboard"))


@app.route('/task/toggle_complete/<int:id>')
@login_required
def toggle_complete(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash('Unauthorized', 'danger')
        return redirect(url_for('dashboard'))

    task.is_complete = not task.is_complete
    db.session.commit()
    flash('Task updated successfully!', 'success')
    return redirect(url_for('dashboard'))


