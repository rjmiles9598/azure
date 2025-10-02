import logging
from flask import Flask
# flask: the Flask framework package
# Flask: is a class in flask.app that represents a Flask application object
# __init__.py is the file name itself. It is a special file that tells python "this directory" is a package".
app = Flask(__name__)
# app is a module level variable - your Flask application instance (often used by servers/blueprints/decorators)
#Flask - calls the class constructor to create an instance
# __name__ is a built-in module dunder string set by python.
wsgi_app = app.wsgi_app
    # wsgi_app: variable name that gets assigned to app.wsgi_app(an attribute on the Flask app)
        # the dot (.) is attribute access - "get the wsgi_app attribute from app."
        # app.wsgi_app - Internally Flask wraps the core WSGI application with middleware
            # it is that inner WSGI callable stack
            # WSGI layer - People often do this to:
                # introspect or wrap with additional middleware
                # expose a distinct callable for servers that expect wsgi_app specifically
                # preserve the pre-wrapped callable before tinkering with it.
        
app.logger.setLevel(logging.WARNING)
    # app.logger - a logger instance Flask provides for your app
    # the . - accesses the setLevel method
    # setLevel - sets the minimum severity that this logger will process.
    # logging.WARNING - a constant for the warning level. Levels (low - high) are DEBUG(10), INFO(20), WARNING(30),
    #   ERROR(40), CRITICAL(50). 
    #Effect: only WARNING and above emitted by app.logger will be handled (unoless handlers have lower thresholds)
streamHandler = logging.StreamHandler()
    # Creates a handler that writes log records to a stream
    # StreamHandler - a logging handler class; calling it with () instantiates it.
    # Without a customer formatter, it uses the default hadler format, which is pretty bare
streamHandler.setLevel(logging.WARNING)
    # sets the handlers own filter level to WARNING.
    # Important Detail:
        # For a log record to be emitted, it must pass both the loggers level and the handlers level
app.logger.addHandler(streamHandler)
    # Attaches the streamHandler to app.logger
    # A logger can have multiple handlers. Each one decides how/where to output.
    # If you add a handler without removing Flasks default one, you can get duplicate lines. With Flask 2.X+, the 
    #   default handler is limited (and often only active in debug); your explicit setup here is predictable

import FlaskExercise.views