from flask import Blueprint
from flask_restful import Api, Resource
import schedule_db
import propertiesUtil
import propertiesContents
from flask import Flask, render_template, request

SCHEDULE_ADD_TASK_PATH = propertiesUtil.read_properties(propertiesContents.SCHEDULE_ADD_TASK_PATH)

def add_schedule(request):
    title_text = request.form['title_text']
    description_text = request.form['description_text']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    print(start_date)
    
    print(title_text + ":" + description_text + ":" + start_date + ":" + end_date)
    with open(SCHEDULE_ADD_TASK_PATH, mode='w', encoding="utf-8") as f:
        f.write(title_text + ":" + description_text + ":" + start_date + ":" + end_date)
    return


api_bp = Blueprint('schedule', __name__, url_prefix='/schedule')

class Schedule_Task(Resource):
    def get(self):
        return [{'id': x[0], 'alldate_flg': x[1],\
            'start_date': x[2], 'end_date': x[3],\
            'summary': x[4], 'description': x[5]} for x in schedule_db.get_all()]

api = Api(api_bp)
api.add_resource(Music_Location, '/task')