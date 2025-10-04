import mysql.connector

#database code

def get_db_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="prem@1208",
        database="todo_app"
    )
    return conn


def create_user(name,email,password):
    conn=get_db_connection()
    cursor=conn.cursor()

    try:
        cursor.execute("insert into users(name,email,password) values (%s,%s,%s)",(name,email,password))
        conn.commit()
        return True
    except mysql.connector.IntegrityError:
        return False
    finally:
        cursor.close()
        conn.close()

def get_user_by_email(email):
    conn=get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("select * from users where email=%s",(email,))
    user=cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def add_task(user_id, title):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (user_id, title) VALUES (%s, %s)", (user_id, title))
    conn.commit()
    cursor.close()
    conn.close()

def get_tasks(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks WHERE user_id = %s", (user_id,))
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks

def mark_task_done(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = TRUE WHERE id = %s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()


