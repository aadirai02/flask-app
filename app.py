from flask import Flask, render_template, request, redirect, url_for, abort
import logging

# Create a Flask application instance
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG

# Define a route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        if name == 'Aaditya':
            return redirect(url_for('lpa', name=name))
        elif name == 'Uttam':
            return redirect(url_for('uttam', name=name))
        else:
            return redirect(url_for('greet', name=name))
    return render_template('index.html')

# Define a route for the greeting page
@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name')
    if name:
        logging.info(f"Greeting {name}")
    return render_template('greet.html', name=name)

# Define a route for the 15 LPA page
@app.route('/15lpa')
def lpa():
    name = request.args.get('name')
    if name:
        logging.info(f"15 LPA for {name}")
    return render_template('15lpa.html', name=name)

# Define a route for the Uttam page
@app.route('/uttam')
def uttam():
    name = request.args.get('name')
    if name:
        logging.info(f"{name} wants to work under Uttam Undale")
    return render_template('uttam.html', name=name)

# Define a route for internal server error (500)
@app.route('/internal-server-error')
def internal_server_error():
    error_message = "Internal Server Error - The server encountered an internal error and was unable to complete your request."
    logging.error(error_message)  # Log the error message
    abort(500)

# Define a route for bad request (400)
@app.route('/bad-request')
def bad_request():
    error_message = "Bad Request - The server cannot process the request due to a client error."
    logging.error(error_message)  # Log the error message
    abort(400)

# Define a catch-all route for handling unknown paths
@app.route('/<path:path>')
def handle_undefined_paths(path):
    error_message = f"404 Not Found - The requested URL '{request.url}' was not found on the server."
    logging.error(error_message)  # Log the error message
    return error_message, 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
