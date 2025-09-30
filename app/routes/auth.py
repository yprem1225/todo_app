from flask import render_template,session,url_for,redirect,flash,Blueprint
from app.forms import RegistrationForm,LoginForm
from app.models import get_user_by_email,create_user

auth_bp=Blueprint("auth",__name__)

@auth_bp.route("/register",methods=["GET","POST"])
@auth_bp.route("/",methods=["GET","POST"])
def register():
    form=RegistrationForm()

    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        password=form.password.data

        if create_user(name,email,password):
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for("auth.login"))
        else:
            flash("Email already exists!", "danger")

    return render_template("register.html",form=form)

@auth_bp.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm()

    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data

        user=get_user_by_email(email)

        if user and user["password"] == password: 
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]

            flash(f"Welcome back, {user['name']}!", "success")
            return redirect(url_for("tasks.task_list"))
        else:
             flash("Invalid email or password", "danger")

    return render_template("login.html",form=form)

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))




