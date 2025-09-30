from flask import Blueprint, render_template, redirect, url_for, session, flash
from app.forms import TaskForm
from app.models import add_task, get_tasks, mark_task_done

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/tasks", methods=["GET", "POST"])
def task_list():
    if "user_id" not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for("auth.login"))

    user_id = session["user_id"]
    form = TaskForm()

    if form.validate_on_submit():
        title = form.title.data
        add_task(user_id, title)
        flash("Task added!", "success")
        return redirect(url_for("tasks.task_list"))  # avoid resubmission on refresh

    tasks = get_tasks(user_id)
    return render_template("task.html", form=form, tasks=tasks)

@tasks_bp.route("/tasks/<int:task_id>/done")
def complete_task(task_id):
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    mark_task_done(task_id)
    flash("Task marked as done!", "success")
    return redirect(url_for("tasks.task_list"))
