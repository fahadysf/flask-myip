# Simple Flask Hello World App

from urllib.parse import urljoin
from flask import Flask, render_template, redirect

app = Flask(__name__)

app.config.update(STATIC_URL='http://cdn.fahad.link/')

@app.endpoint('static')
def static(filename):
    static_url = app.config.get('STATIC_URL')

    if static_url:
        return redirect(urljoin(static_url, filename))

    return app.send_static_file(filename)

@app.route('/')
def hello_world():
    args = {
        'main_content': "Test App",
        'page_title': "Hello World!",
        'author': "Fahad Yousuf"
    }
    return render_template('index.html', **args )

# Serve the application
if __name__ == "__main__":
    app.run(host='0.0.0.0')