import time
import threading

todo_list = []  

def set_reminder(task, reminder_time):
    """Sets a reminder for a given task at a specific time"""
    def reminder():
        time.sleep(reminder_time * 60)  
        print(f"🔔 Reminder: {task}")
    
    thread = threading.Thread(target=reminder)
    thread.start()
    return f"Reminder set for '{task}' in {reminder_time} minutes."

def add_todo(task):
    """Adds a task to the to-do list"""
    todo_list.append(task)
    return f"Task '{task}' added to the to-do list."

def get_todo_list():
    """Retrieves the current to-do list"""
    if not todo_list:
        return "Your to-do list is empty."
    return "Your to-do list:\n" + "\n".join(f"- {task}" for task in todo_list)

