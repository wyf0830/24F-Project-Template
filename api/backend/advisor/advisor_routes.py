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
    
@advisor.route('/student_data', methods=['GET'])
def get_advisor_data():
    try:
        query = '''
            SELECT ca.Advisor_ID,
                   ca.Name AS Advisor_Name,
                   ca.Contact_Info AS Advisor_Contact,
                   s.Student_ID,
                   s.Name AS Student_Name,
                   s.Major AS Student_Major,
                   s.Program AS Student_Program,
                   s.Profile_Status AS Student_Profile_Status
            FROM Career_Advisor ca
            LEFT JOIN Student s ON ca.Student_ID = s.Student_ID
            ORDER BY ca.Advisor_ID
        '''
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()

        return make_response(jsonify(theData), 200)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)

@advisor.route('/student_data', methods=['POST'])
def add_student():
    try:
        data = request.get_json()

        # Extract fields for the Student table
        student_name = data.get('Student_Name')
        student_major = data.get('Student_Major')
        student_program = data.get('Student_Program')
        student_status = data.get('Student_Profile_Status', 1)  # Default to active status

        # Validate required fields
        if not student_name or not student_major or not student_program:
            return make_response(
                jsonify({'error': 'Missing required fields: Student_Name, Student_Major, or Student_Program'}), 400
            )

        query = '''
            INSERT INTO Student (Name, Major, Program, Profile_Status)
            VALUES (%s, %s, %s, %s)
        '''
        
        cursor = db.get_db().cursor()
        cursor.execute(query, (student_name, student_major, student_program, student_status))
        db.get_db().commit()

        return make_response(jsonify({'message': 'Student added successfully'}), 201)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
    
@advisor.route('/student_data/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    try:
        data = request.get_json()

        # Extract fields for update
        student_name = data.get('Student_Name')
        student_major = data.get('Student_Major')
        student_program = data.get('Student_Program')
        student_status = data.get('Student_Profile_Status')

        # Validate required fields
        if not student_name or not student_major or not student_program or student_status is None:
            return make_response(
                jsonify({'error': 'Missing required fields: Student_Name, Student_Major, Student_Program, or Student_Profile_Status'}), 400
            )

        query = '''
            UPDATE Student
            SET Name = %s, Major = %s, Program = %s, Profile_Status = %s
            WHERE Student_ID = %s
        '''
        
        cursor = db.get_db().cursor()
        cursor.execute(query, (student_name, student_major, student_program, student_status, student_id))
        db.get_db().commit()

        if cursor.rowcount == 0:
            return make_response(jsonify({'error': 'Student not found'}), 404)

        return make_response(jsonify({'message': 'Student updated successfully'}), 200)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)

@advisor.route('/student_data/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        query = '''
            DELETE FROM Student
            WHERE Student_ID = %s
        '''
        
        cursor = db.get_db().cursor()
        cursor.execute(query, (student_id,))
        db.get_db().commit()

        if cursor.rowcount == 0:
            return make_response(jsonify({'error': 'Student not found'}), 404)

        return make_response(jsonify({'message': 'Student deleted successfully'}), 200)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
