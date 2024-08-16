from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the string from the form
        user_string = request.form['user_string']
        
        # Define the file name
        file_name = 'output.txt'
        
        # Save the string to the file
        with open(file_name, 'w') as f:
            f.write(user_string)
        
        # Return a success message
        return f'String saved successfully to {file_name}!'
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
