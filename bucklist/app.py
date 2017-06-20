from flask import Flask

# Import the configuration data.
from config import Configuration

# Create a flask application instance.
app = Flask(__name__)
app.config.from_object(Configuration)

if __name__ == '__main__':
    app.run()
