from flask import Flask, render_template, request
from music import *
from music_location import get_all, insert_search_all

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myspa.db'
app.register_blueprint(api_bp)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/music/play', methods=['POST'])
def click_music():
    print("test")
    print(request)
    print(request.form)
    play_music(request)
    return render_template('index.html')

if __name__ == '__main__':
    insert_search_all()
    app.run()
