CREATE TABLE IF NOT EXISTS tasks (
	id INTEGER PRIMARY KEY,
	task_name TEXT NOT NULL,
	description TEXT,
	days_to_due TEXT,
	status TEXT DEFAULT 'pending',
	date_due TEXT
);
