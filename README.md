# Flask Form Handling

This is a simple Flask web application that demonstrates how to handle form submissions using the POST method.

## Features
- Accepts user input via an HTML form
- Sends data to the server using the POST method
- Displays a personalized greeting based on user input

## Prerequisites
Before running this project, ensure you have the following installed:
- Python 3
- Flask

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. Navigate into the project directory:
   ```bash
   cd your-repo-name
   ```
3. Install Flask if you haven't already:
   ```bash
   pip install flask
   ```

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```
3. Enter your name in the input field and submit the form.
4. The application will display a personalized greeting.

## Code Overview
```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']  # Get user input
        return f"Hello, {name}!"  # Display greeting
    return '''
        <form action="/" method="POST">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name">
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
```

## License
This project is licensed under the MIT License.

## Contributing
Feel free to fork this repository and submit pull requests with improvements!

---

*Happy Coding! 🚀*

