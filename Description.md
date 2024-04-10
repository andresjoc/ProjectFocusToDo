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
- __As a__ client, __I want__ to see all plans for subscriptions, __so what__ I can choose the best plan for my needs.
- __As a__ client, __I want__ to pay for subscriptions, __so what__ I can access to all features of the platform.
- __As a__ premium client, __I want__ to be able to see my report of completed tasks and the time spent on each one, __so what__ I can evaluate my productivity.
- __As a__ premium client, __I want__ to be able to automatically repeat tasks, __so what__ I can plan my work more efficiently.
- __As a__ premium client, __I want__ to be able to create unlimited projects, __so what__ I can incorporate all areas of my life into productivity.
- __As a__ premium client, __I want__ to be able to create folders, __so what__ I can organize my projects by life categories.
- __As an__ admin, __I want__ to have a report of the number of clients, __so what__ I can make decisions to increase the number of clients.
- __As an__ admin, __I want__ to have a report of the number of subscribed clients, __so what__ I can make decisions to increase the number of premium clients.

## Technical Definitions

### Tools to Use

In this case, the backend will be built using _Python_ 3.11_, and some related technologies such as _Fast API__ to serve functionalities, _PyTest_ to apply some simple unit tests, and _Black_ to auto-format the code and increase code readability.

## Entities
- User: name, id, email, password, login(), logout()
- Admin (User): get_client_reports(), get_premium_client_reports()
- Client (User): create_tasks(), create_subtasks(), view_tasks(), edit_tasks(), edit_subtasks(), delete_tasks(), delete_subtasks(), create_tag(), edit_tag(), delete_tag(), view_projects(), view_subtasks(), create_project(), edit_project(), delete_project(), receive_notifications(), start_pomodoro_timer(), stop_pomodoro_timer(), custom_pomodoro_timer(), see_plans(), pay_for_subscription()
- Premium Client (Client): view_productivity_stats(), create_folder(), edit_folder(), delete_folder(), repeat_tasks()
- Task: name, description, due_date, priority, status, tags, Client[E], create_subtask(), edit_subtask(), delete_subtask()
- Tag: name
- Subtask: name, status, Task[E]
- Notification: message, send(), show(), Client[E]
- Pomodoro: short_break, long_break, pomodoro_length, long_break_after
- Project: name, Client[E], Task[E], add_task(), remove_task()
- Folder: name, Project[E], Client[E], add_project(), remove_project()
- Plan: name, price, description
- Subscription: Plan[E], start_date, end_date, add client(), remove client(), Client[E]
- Report: title, description, date, type
- TaskStats(Report): Client[E], total_completed_tasks, weekly_completed_tasks, today_completed_tasks, task_focus_time, project_time, create_task_report()
- ClientsStats(Report): date, number_of_clients, number_of_premium_clients, create_client_report(), Admin[E]

# Processes

- Login:
  
![Diagrama sin título-Log in Managment  drawio](https://github.com/andresjoc/ProjectFocusToDo/assets/163566801/f9d81cc0-21c5-47cc-9b19-3dd6b47663bd)

- Create a Task:
- Edit a Task:
- Delete a Task:
- View Tasks:

![task management](https://github.com/andresjoc/ProjectFocusToDo/assets/163566801/b1b29b5b-3110-4c48-bbe4-62bdac221403)
-  Create a project:
-  Edit a Project:
-  Delete a Project:
-  View Projects:


 ![Diagrama sin título-Project man drawio](https://github.com/andresjoc/ProjectFocusToDo/assets/163566801/1381b063-f4c3-4d60-ad62-526718dab153)
- Create a Folder:
- Edit a Folder:
- Delete a Folder:
- View Folders:

![Diagrama sin título-Folder Man drawio](https://github.com/andresjoc/ProjectFocusToDo/assets/163566801/8eaeaff8-c6b9-4c47-9648-2d044da3bb7e)

- Create subtask:
- Edit Subtask:
- Delete Subtask:
- View Subtasks:

![Subtask management](https://github.com/andresjoc/ProjectFocusToDo/assets/163566801/64ab4f36-1d45-4e24-b807-7bb8012c8aac)

- Start a Pomodoro:
- Stop a Pomodoro:
- Customize a Pomodoro:

![Diagrama sin título-Pomodoro Managment drawio](https://github.com/andresjoc/ProjectFocusToDo/assets/163566801/306dfa06-f45a-484f-8c35-9512306084d5)  

- See Plans:
- Buy Subscription:
- Add a client to the subscription:
- Remove a client from the subscription:

![Diagrama sin título-Subscription Manager drawio (1)](https://github.com/andresjoc/ProjectFocusToDo/assets/163566801/5808043e-33ce-43a8-921e-7201da8ff7f1)

- Send Notification:
- Show Notifications:

![Diagrama sin título-Notification Managment  drawio](https://github.com/andresjoc/ProjectFocusToDo/assets/163566801/9093d6c2-db96-4252-be22-a6f34dfdc879)



