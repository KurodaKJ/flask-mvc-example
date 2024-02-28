from flask import render_template
from src import app


# Set up the home route
@app.route('/')
def index():
    return render_template('index.html')


# This is the entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
