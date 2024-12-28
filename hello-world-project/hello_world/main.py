from flask import Flask

app = Flask(__name__)

def get_greeting(name: str = "World") -> str:
    """
    Returns a greeting message.
    
    Args:
        name (str): Name to greet. Defaults to "World".
    
    Returns:
        str: The greeting message
    """
    return f"Hello, {name}!"

@app.route('/')
def home():
    return get_greeting()

@app.route('/<name>')
def greet_name(name):
    return get_greeting(name)

def main():
    """Main function that runs the Flask application."""
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()