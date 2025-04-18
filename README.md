![Logo of the project](static/assets/img/chef.svg)

# Kitchen Service
> Kitchen management system for restaurants: dishes, categories, and assigned chefs

This web application is designed to help manage kitchen and restaurant operations efficiently. The system supports two types of users: administrators and cooks, each with different permissions and capabilities.

👨‍🍳 Administrator Capabilities:
 - Add new cooks to the system.
 - Create, edit, and delete dishes.
 - Create, edit, and delete dish categories.
 - Manage staff profiles: view, create, edit, and delete information about all employees.

🧑‍🍳 Cook Capabilities:
 - Log in using pre-created credentials provided by an administrator.
 - Create, edit, and delete dishes.
 - View dish categories (read-only access).
 - View a full list of all employees, but can only edit their own profile information.

🔍 Search Functionality:
 - Dishes can be searched by name and category.
 - On the category page, users can search categories by their name only.

## Getting started

A quick introduction of the minimal setup you need to get started.

```shell
# After cloning the project create a virtual environment:
python -m venv venv
venv\Scripts\activate # for Windows
source venv/bin/activate # for macOS/Linux

pip install -r requirements.txt # install dependencies
python manage.py migrate # apply migrations

python manage.py createsuperuser 
python manage.py generate_fake_datф # to add data to DB
python manage.py runserver
```

After executing all commands, you can run the server and the Kitchen Service will work.


## Contributing

If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome.

