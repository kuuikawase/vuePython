from flask import Blueprint
from flask_restful import Api, Resource
import music_location

api_bp = Blueprint('music', __name__, url_prefix='/music')

class Music_Location(Resource):
    def get(self):
        return [{'id': x[0], 'musicname': x[1], 'path': x[2]} for x in music_location.get_all()]

api = Api(api_bp)
api.add_resource(Music_Location, '/location')

import propertiesUtil
import propertiesContents
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
PLAY_STATUS_FILE = propertiesUtil.read_properties(propertiesContents.MUSIC_PLAY_STATUS)
PLAY_MUSIC_FOLDER = propertiesUtil.read_properties(propertiesContents.MUSIC_FOLDER)
BREAK = "break"
RETURN_TEXT = ["end", "now", BREAK]


def stop_music():
    with open(PLAY_STATUS_FILE, mode='w', encoding="utf-8") as f:
        f.write(BREAK)


def play_music(request):
    path = request.form['path']
    name = request.form['name']
    with open(PLAY_STATUS_FILE, mode='w', encoding="utf-8") as f:
        f.write(path)
    return

