from flask import Flask, render_template, request
from music import *
import music_location
from shedule import *

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myspa.db'
app.register_blueprint(api_music_bp)
app.register_blueprint(api_schedule_bp)

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

@app.route('/music/stop', methods=['POST'])
def request_stop_music():
    print("test")
    stop_music()
    return render_template('index.html')

@app.route('/scadule/add', methods=['POST'])
def click_add_schedule():
    print("test")
    print(request)
    print(request.form)
    add_schedule(request)
    return render_template('index.html')


if __name__ == '__main__':
    music_location.insert_search_all()
    app.run()
