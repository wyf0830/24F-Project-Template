########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
advisor = Blueprint('advisor', __name__)

@advisor.route('/student/<int:student_id>', methods=['GET'])
def get_student_profile(student_id):
    try:
        query = f'''
            SELECT 
                Student_ID, 
                Name, 
                Major, 
                Interests, 
                Program, 
                Profile_Status 
            FROM 
                Student 
            WHERE 
                Student_ID = {str(student_id)} AND Profile_Status = 1
        '''

        current_app.logger.info(f'GET /student/<int:student_id> query={query}')
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()

        current_app.logger.info(f'GET /student/<int:student_id> Result of query = {theData}')

        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    except Exception as e:
        current_app.logger.error(f"Error fetching student profile: {str(e)}")
        return make_response(jsonify({"error": "Internal Server Error"}), 500)
    

@advisor.route('/schedules/<int:student_id>', methods=['GET'])
def get_schedule(student_id):

    try:
        query = f'''SELECT Details FROM Employer_Feedback WHERE Student_ID = {str(student_id)}'''
        current_app.logger.info(f'GET /feedback/<int:student_id> query={query}')
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()

        current_app.logger.info(f'GET /student/<int:student_id> Result of query = {theData}')

        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    except Exception as e:
        current_app.logger.error(f"Error fetching feedback: {str(e)}")
        return make_response(jsonify({"error": "Internal Server Error"}), 500)