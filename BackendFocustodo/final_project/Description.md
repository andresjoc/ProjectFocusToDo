# Course Project - Task Management Project
v15.2
This project involves the construction of the backend of a platform called 'Focus To-Do', using object-oriented design, and design patterns, to provide different productivity, task management and time management

## Business Model

This is a task management platform that operates on a freemium business model, offering basic features for free, such as starting a timer for the Pomodoro technique. However, if you desire premium features like advanced task analytics and better organization, you have to buy a subscription.

### Business Rules
- Each username can only be associated with one account.
- If the client wants to access the app, they must enter their registered username along with their corresponding password.
- To access premium features, the client must have purchased the premium subscription.
- Subscription plans can only be purchased on a monthly or annual basis.
- Clients can create, and delete tasks.
- Clients with a premium subscription can create folders.
- Clients with premium subscriptions can view productivity statistics.
- Clients can set a timer to use the Pomodoro technique.
- By default, the Pomodoro lasts 25 minutes, the short break 5 minutes, and the long break 15 minutes.
- Clients can edit the default times for the Pomodoro, short break, and long break.
- Clients can organize tasks into projects for better organization.
  
## User Stories
- __As a__ client, __I want__ to be able to create, and delete tasks and subtasks __so what__ I can organize my work and daily activities.
- __As a__ client, __I want__ that automatically tasks and subtasks are deleted when are done __so what__ I can get rid of tasks I don't need
- __As a__ client, __I want__ to be able to set a custom Pomodoro timer, __so what__ I can improve my focus and productivity.
- __As a__ client, __I want__ to receive notifications, __so what__ I can remember pending tasks and Pomodoro breaks.
- __As a__ client, __I want__ to see all plans for subscriptions, __so what__ I can choose the best plan for my needs.
- __As a__ client, __I want__ to pay for subscriptions, __so what__ I can access to all features of the platform.
- __As a__ premium client, __I want__ to be able to see my report of completed tasks and the time spent on each one, __so what__ I can evaluate my productivity.
- __As a__ premium client, __I want__ to be able to add tag to my tasks, __so what__ I can categorize them to plan my time more efficiently.
- __As a__ premium client, __I want__ to be able to create unlimited projects, __so what__ I can incorporate all areas of my life into productivity.
- __As a__ premium client, __I want__ to be able to create folders and delete, __so what__ I can organize my projects by life categories.
- __As an__ admin, __I want__ to have a report of the number of clients and premium, __so what__ I can make decisions to increase the number of clients and premium clients.

## Technical Definitions

### Tools to Use

In this case, the backend will be built using _Python_ 3.11_, and some related technologies such as _Fast API__ to serve functionalities, _PyTest_ to apply some simple unit tests, and _Black_ to auto-format the code and increase code readability.

## Entities
- User: 
  - Properties: name, id, email, password
  - Methods: login(), logout()

- Client (User): 
  - Properties: tasks, subtasks, projects, folders, tags, notifications, pomodoro_timer, subscription
  - Methods: create_task(), delete_task(), create_subtask(), delete_subtask(), edit_task(), edit_subtask(), create_tag(), edit_tag(), delete_tag(), view_projects(), view_subtasks(), create_project(), edit_project(), delete_project(), receive_notifications(), start_pomodoro_timer(), stop_pomodoro_timer(), custom_pomodoro_timer(), see_plans(), pay_for_subscription()

- Premium Client (Client): 
  - Properties: productivity_stats, folders
  - Methods: view_productivity_stats(), create_folder(), edit_folder(), delete_folder(), repeat_tasks()

- Task: 
  - Properties: name

- Tag: 
  - Properties: name

- Subtask: 
  - Properties: name, status, task

- Notification: 
  - Properties: message, client
  - Methods: send(), show()

- Pomodoro: 
  - Properties: short_break, long_break, pomodoro_length, long_break_after, client

- Project: 
  - Properties: name, client, tasks
  - Methods: add_task(), remove_task()

- Folder: 
  - Properties: name, client, projects
  - Methods: add_project(), remove_project()

- Plan: 
  - Properties: name, price, description

- Subscription: 
  - Properties: plan, start_date, end_date, clients
  - Methods: add_client(), remove_client()

- Report: 
  - Properties: title, description, date, type

- TaskStats (Report): 
  - Properties: client, total_completed_tasks, weekly_completed_tasks, today_completed_tasks, task_focus_time, project_time
  - Methods: create_task_report()

- ClientsStats (Report): 
  - Properties: number_of_clients, number_of_premium_clients
  - Methods: create_client_report()
