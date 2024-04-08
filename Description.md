# Course Project - Task Managment Project
v15.2
This project involves the construction of the backend of a platform called 'Focus To-Do', using object-oriented design, design patterns, in order to provide different productivity, task management and time management

## Business Model

This is a task management platform that operates on a freemium business model, offering basic features for free, such as starting a timer for the Pomodoro technique. However, if you desire premium features like cloud services and advanced task analytics, among others, you have to buy a subscription. Additionally, the platform may generate revenue through in-app advertisements.

### Business Rules
- The user must provide a valid email address and create a password to register an account.
- Each email can only be associated with one account.
- If the user wants to access the app, they must enter their registered email along with their corresponding password.
- To access premium features, the user must have purchased the premium subscription.
- Subscription plans can only be purchased on a monthly or annual basis.
- Users can create, edit, and delete tasks.
- Users without a premium subscription can create a maximum of 5 projects.
- Users with a premium subscription can create folders.
- Users with premium subscriptions can view productivity statistics.
- Tasks must have attributes such as description (mandatory), due date, priority, and tags.
- Users can set a timer to use the Pomodoro technique.
- By default, the Pomodoro lasts 25 minutes, the short break 5 minutes, and the long break 15 minutes.
- Users can edit the default times for the Pomodoro, short break, and long break.
- Users can organize tasks into projects for better organization.
- Users can provide feedback and report issues.
  
## User Stories
- __As a__ user, __I want__ to be able to create tasks,  __so what__ I can organize my work and daily activities.
- __As a__ user, __I want__ to use the Pomodoro Technique, __so what__ I can manage my work time.
- __As a__ user, __I want__ to be able to set a custom Pomodoro timer, __so what__ I can improve my focus and productivity.
- __As a__ user, __I want__ be able to assign priorities to my tasks, __so what__ I can determine their importance and plan my time more efficiently.
- __As a__ user, __I want__ to receive notifications, __so what__ I can rememeber pending tasks and Pomodoro breaks.
- __As a__ premium user, __I want__ be able to see a report of my completed tasks and the time spent on each one, __so what__ I can evaluate my productivity.
- __As a__ premium user, __I want__ to be able to create unlimited projects, __so what__ I can incorporate all areas of my life into productivity.
- __As a__ premium user, __I want__ to be able to create folders, __so what__ I can organize my projects by life categories.
- __As a__ admin, __I want__ have a report of the number of users, __so what__ I can make decisions to increase the number of users.
- __As an__ admin, __I want__ to have a report of the number of subscribed users, __so what__ I can make decisions to increase the number of premium users.

## Technical Definitions

### Tools to Use

In this case, the backend will be build using _python 3.10_, and some related technologies as _Fast API_ to serve functionalities, _PyTest_ to apply some simple unit tests, and _Black_ to auto-format the code and increase code readibility.

## Entities

- Manager (User): generate reports(), create courses(), create publicities()
- Schedulling: day, hour, sport space[E], payment[E] 
- Publicity: text, deadline, hide()
- Client(User): make_reservations(), show_catalog()
- User:name, id, email, password, login(), logout()
- Course(Service): description, start_date, end_date, list_clients, add client(), remove client()
- Catalog Courses: list courses, add course(), remove course()
- Catalog Sport Spaces: list spaces, add space(), remove space()
- SportSpace (Service): location, dimensions
- Reservations: client[E], sport space [E], start date, end date
- PayChannel: name, description
- Payments: client, value, service[E]
- Service: name, price

# Processes

- Management Publicities:
  
![Activity Diagram](images/activity_management_publicities.png)

- View Schedulling Report:

- View Courses Catalog:

- Create a Reservation:

- Make Online Payment:

- View Payments Report:
