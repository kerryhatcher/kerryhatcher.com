__author__ = 'khatcher'



from flask_bootstrap import Bootstrap




def init_app(app):
    app.bootstrap = Bootstrap(app)