from flask import Flask, render_template, request
from chatbot import get_best_match  # Import the function from chatbot.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render the chat UI

@app.route('/get_answer', methods=['POST'])
def get_answer():
    if request.method == 'POST':
        user_input = request.form['user_input']  # Get user input from the form
        answer = get_best_match(user_input)  # Get the answer using chatbot.py's function
        return render_template('index.html', answer=answer, user_input=user_input)  # Display the answer on the web page

if __name__ == '__main__':
    app.run(debug=True)
