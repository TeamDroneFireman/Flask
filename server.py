from flask import Flask, url_for, send_file
import os
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/screenshot')
def api_screen():
    os.system('echo LOL')
    filename = 'screenshot.png'
    return send_file(filename, mimetype='image/png')

@app.route('/get_image')
def get_image():
    # if request.args.get('type') == '1':
    #    filename = 'ok.png'
    # else:
    #    filename = 'error.png'
    filename = 'screenshot.png'
    return send_file(filename, mimetype='image/png')
# @app.route('/articles')
# def api_articles():
#     return 'List of ' + url_for('api_articles')
#
# @app.route('/articles/<articleid>')
# def api_article(articleid):
#     return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
