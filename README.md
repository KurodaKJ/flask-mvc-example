# Flask-MVC-Example
This is a simple example of a Flask application using the MVC pattern.

## Libraries used
You can find the libraries used in the `requirements.txt` file.

## Installation

### Recommended
- Create a virtual environment using the following command:
```python -m venv venv```
This will create a virtual environment in the current directory.

- To activate the virtual environment, run the following command:
```venv\Scripts\activate```

Then
1. Clone the repository
2. Install the requirements using pip:
``` pip install -r requirements.txt```
3. Set up the database for migrations in MySQL.
4. Run the flask migration command:
```flask db upgrade```
5. Run the application:
```flask run```

To stop the application, press `Ctrl + C` in the terminal.


# Migration tutorial
1. Create a model in python file.
2. Before creating a migration, make sure to create a database in MySQL.
3. Run the following command to create a migration repository:
```flask db init```
4. Run the following command to create a migration:
```flask db migrate -m "migration message"```
4. Run the following command to apply the migration:
```flask db upgrade```
5. To revert the migration, run the following command:
```flask db downgrade```