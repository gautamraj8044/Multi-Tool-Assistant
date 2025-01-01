import sqlite3

# SQLite functions for managing To-Do list
def get_db_connection():
    conn = sqlite3.connect('todo.db')  # SQLite database file
    conn.row_factory = sqlite3.Row  # Fetch rows as dictionaries
    return conn

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            status TEXT DEFAULT 'Pending',
            priority TEXT DEFAULT 'Medium',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def add_task_to_db(task_name, priority='Medium'):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task_name, priority) VALUES (?, ?)", (task_name, priority))
    conn.commit()
    cursor.close()
    conn.close()
    return f"Task '{task_name}' added successfully!"

def show_tasks_from_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    
    if not tasks:
        return "Your To-Do list is empty."
    
    task_list = []
    for task in tasks:
        task_list.append(f"ID: {task['id']} - Task: {task['task_name']} - Status: {task['status']} - Priority: {task['priority']} - Created At: {task['created_at']}")
    
    return "\n".join(task_list)



def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return f"Task {task_id} deleted successfully."
