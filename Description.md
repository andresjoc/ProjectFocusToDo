# Course Project - Task Management Project
v15.2
This project involves the construction of the backend of a platform called 'Focus To-Do', using object-oriented design, and design patterns, to provide different productivity, task management and time management

## Business Model

This is a task management platform that operates on a freemium business model, offering basic features for free, such as starting a timer for the Pomodoro technique. However, if you desire premium features like cloud services and advanced task analytics, among others, you have to buy a subscription. Additionally, the platform may generate revenue through in-app advertisements.

### Business Rules
- The client must provide a valid email address and create a password to register an account.
- Each email can only be associated with one account.
- If the client wants to access the app, they must enter their registered email along with their corresponding password.
- To access premium features, the client must have purchased the premium subscription.
- Subscription plans can only be purchased on a monthly or annual basis.
- Clients can create, edit, and delete tasks.
- Clients without a premium subscription can create a maximum of 5 projects.
- Clients with a premium subscription can create folders.
- Clients with premium subscriptions can view productivity statistics.
- Tasks must have attributes such as description (mandatory), due date, priority, and tags.
- Clients can set a timer to use the Pomodoro technique.
- By default, the Pomodoro lasts 25 minutes, the short break 5 minutes, and the long break 15 minutes.
- Clients can edit the default times for the Pomodoro, short break, and long break.
- Clients can organize tasks into projects for better organization.
- Clients can provide feedback and report issues.
  
## User Stories
- __As a__ client, __I want__ to be able to create, edit and delete tasks and subtasks,  __so what__ I can organize my work and daily activities.
- __As a__ client, __I want__ to be able to set a custom Pomodoro timer, __so what__ I can improve my focus and productivity.
- __As a__ client, __I want__ to be able to assign priorities and tags to my tasks, __so what__ I can determine their importance and categorize them to plan my time more efficiently.
- __As a__ client, __I want__ to receive notifications, __so what__ I can remember pending tasks and Pomodoro breaks.
- __As a__ premium client, __I want__ to be able to see my stats of completed tasks and the time spent on each one, __so what__ I can evaluate my productivity.
- __As a__ premium client, __I want__ to be able to automatically repeat tasks, __so what__ I can plan my work more efficiently.
- __As a__ premium client, __I want__ to be able to create unlimited projects, __so what__ I can incorporate all areas of my life into productivity.
- __As a__ premium client, __I want__ to be able to create folders, __so what__ I can organize my projects by life categories.
- __As an__ admin, __I want__ to have a report of the number of clients, __so what__ I can make decisions to increase the number of clients.
- __As an__ admin, __I want__ to have a report of the number of subscribed clients, __so what__ I can make decisions to increase the number of premium clients.

## Technical Definitions

### Tools to Use

In this case, the backend will be built using _Python_ 3.11_, and some related technologies as _Fast API_ to serve functionalities, _PyTest_ to apply some simple unit tests, and _Black_ to auto-format the code and increase code readability.

## Entities
- User: name, id, email, password, login(), logout()
- Admin (User): get_client_reports(), get_premium_client_reports()
- Client (User): make_tasks(), view_tasks(), edit_tasks(), delete_tasks(), create_project(), edit_project(), receive_notifications(), start_pomodoro_timer(), stop_pomodoro_timer(), custom_pomodoro_timer()
- Premium Client (Client): view_productivity_stats(), create_folder(), repeat_tasks()
- Task: name, description, due_date, priority, status, tags
- Subtask: name, status, Task[E]
- Notification: message, send(), show(), Client[E]
- Pomodoro: short_break, long_break, pomodoro_length, set_long_break()
- Project: name, Client[E], Task[E], add_task(), remove_task()
- Folder: name, Project[E], Client[E], add_project(), remove_project()
- TaskStats: Client[E], total_completed_tasks, weekly_completed_tasks, today_completed_tasks, task_focus_time, project_time
- Report: date, number_of_clients, number_of_premium_clients


# Processes

- Management Publicities:
  
![Activity Diagram](images/activity_management_publicities.png)

- View Schedulling Report:

- View Courses Catalog:

- Create a Reservation:

- Make Online Payment:

- View Payments Report:
