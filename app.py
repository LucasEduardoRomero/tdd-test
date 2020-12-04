import os

from flask import Flask, render_template

web_app = Flask('web_app')

@web_app.route('/')
def pagina_inicial():
    """
    very simple page
    """
    return render_template('home.html')


if __name__ == '__main__':
    web_app.run(host='0.0.0.0')
    # TO DO , setar debug como true para reload dos templates
