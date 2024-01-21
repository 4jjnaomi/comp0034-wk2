from flask import current_app as app
from markupsafe import escape

@app.route('/')
def hello():
    return f"Hello!"
