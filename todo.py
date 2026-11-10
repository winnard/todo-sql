import sqlite3
from datetime import datetime, timedelta
from colorama import Fore, Style

conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

with open('todo.sql', 'r') as sql_file:
	sql_script = sql_file.read()

cursor.executescript(sql_script)

def add_task(task_name, description, days_to_due):
	now = datetime.now()
	due = now + timedelta(days=int(days_to_due))

	date_added = now.strftime('%d-%m-%Y %H:%M:%S')
	date_due = due.strftime('%d-%m-%Y %H:%M:%S')

	cursor.execute('''
		INSERT INTO tasks (task_name, description, days_to_due, status, date_added, date_due)
		VALUES (?, ?, ?, 'pending', ?, ?)
		''', (task_name, description, days_to_due, date_added, date_due))
	conn.commit()
	print(Fore.GREEN + f"Task '{task_name}' added successfully." + Style.RESET_ALL)

def view_tasks():
	cursor.execute('SELECT * FROM tasks')
	tasks = cursor.fetchall()
	print('\nCurrent tasks: ')
	for task in tasks:
		print(Fore.CYAN + f'ID: {task[0]}, Name: {task[1]}, Days until due: {task[3]}, Status: {task[4]}, Date due: {task[6]}' + Style.RESET_ALL)
while True:
	print('\nOptions: 1) Add Task 2) View Tasks')
	choice = input('\nChoose an option: ')
	if choice == '1':
		task_name = input('Enter task name: ')
		description = input('Enter task description: ')
		days_to_due = input('Enter days until due: ')
		add_task(task_name, description, days_to_due)
	elif choice == '2':
		view_tasks()
	else:
		print('Invalid selection.')

conn.commit()
conn.close()

