from flask import Flask

# Import the configuration data.
import config

# Create a flask application instance.
app = Flask(__name__)
app.config.from_object(config)
