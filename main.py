from flask import Flask
import os  # Import the 'os' module

app = Flask(__name__)

@app.route("/")
def hello():
    return "indumathi"

if __name__ == '__main__':
    print("Starting the Flask server...")  # Add this line
    port = int(os.environ.get('PORT', 8080)) #Get port from environment and default to 8080 if not set.
    app.run(debug=True, host='0.0.0.0', port=8080)
