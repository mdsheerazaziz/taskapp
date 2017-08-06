# Task App
Allow user to create a new task, edit a task, delete a task and view all the task.

## Installation and Usage

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/mdsheerazaziz/taskapp.git

# Go into the repository
$ cd taskapp

# Install dependencies
$ pip install -r requirement.txt

# Create Super user
$ python manage.py superuser

# Run the app
$ python manage.py runserver
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Demo
Hosted on heroku at https://rocky-island-61052.herokuapp.com/login/
  1. Username: demouser, Password: demouser
  2. Username: demouser1, Password: demouser1

## How it Works
1. Create a superuser
2. Superuser can create other user accounts
3. User will see his dashboard with list of tasks
4. User has option to add a new task, edit a task and delete a task
5. If a user clicks add a new task, he can specify the description and task name and click save.
6. Once the task is saved it will appear on dashboard
7. User can edit the task by clicking edit.
8. To delete the task he can click delete.

## License

MIT
