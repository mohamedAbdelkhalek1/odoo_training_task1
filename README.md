# odoo_training_task1
To-Do odoo addon

# Task Statements:
1- To-Do model:
  -Create a new model named todo.task to represent tasks in the to-do list.
  -Include fields such as Task Name, Assign To, Description, Due Date, and Status (New, In Progress, Completed).
2- List View:
  -Add a menu item under the main menu "To-Do" named "All Tasks".
  -Design a list view to display all the tasks with their key information.
3- Form View:
  -Create a form view for the todo.task model to add and edit tasks.
  -Include form fields for Task Name, Assign To, Description, Due Date, and Status.
4- Search View:
  -Create a search view for the todo.task model to add Status filters and some defaults group by Assign To, Status and Due Date.
  -User also can search with Task Name and Assign To fields.
5- List:
  -Add field to todo.task model "estimated time".
  -Timesheet lines related to the task, allow users to record all their timesheets in this task.
  -Make sure total times in related lines not exceed estimated time.
6- Archiving technique:
  -Add archiving feature to todo.task model.
7- Server Action:
  -Add a server action named "Close" to close tickets(One record or multiple).
8- Cron Job:
  -Create an automated action related to todo.task model to alarm end users that there are late tickets depending on the "Due Date" field, and color these records in the tree view.
9- Report Action:
  -Users can print any task as in the following design.
