__author__ = 'khatcher'
# Set the path
import sys

import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server

from  personal_site import create_app

app = create_app('config.py')

manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = 'test.kerryhatcher.com')
)

if __name__ == "__main__":
    manager.run()
