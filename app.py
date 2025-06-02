# Import necessary libraries
from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    reversed_text = None  # Initialize reversed_text to None
    if request.method == 'POST':
        text = request.form['text']  # Get the text input from the form
        reversed_text = text[::-1]  # Reverse the text
    return render_template('index.html', reversed_text=reversed_text)  # Render the template with the reversed text

# Run the app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)