from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

students = Blueprint('students', __name__)

@students.route('/students', methods = ['GET'])
def get_students():
    query = '''
        SELECT * FROM Student
'''
    
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)

    # fetch all the data from the cursor
    # The cursor will return the data as a 
    # Python Dictionary
    theData = cursor.fetchall()

    # Create a HTTP Response object and add results of the query to it
    # after "jasonify"-ing it.
    response = make_response(jsonify(theData))
    # set the proper HTTP Status code of 200 (meaning all good)
    response.status_code = 200
    # send the response back to the client
    return response


@students.route('/student', methods=['POST'])
def add_new_student():
        # Get JSON data from the request
        student_data = request.json
        current_app.logger.info(f"Received data for new student: {student_data}")
    
        # Extract fields from the JSON data
        name = student_data.get('Name')
        major = student_data.get('Major')
        interests = student_data.get('Interests')
        program = student_data.get('Program')
        profile_status = student_data.get('Profile_Status', 1)  # Default to active
    
        # Construct the INSERT query
        query = f'''
            INSERT INTO Student (Name, Major, Interests, Program, Profile_Status)
            VALUES ('{name}', '{major}', '{interests}', '{program}', {profile_status})
        '''
        
        current_app.logger.info(f"Executing query: {query}")
    
        # Execute the INSERT query
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        
        # Get the ID of the newly created student
        new_student_id = cursor.lastrowid
    
        response = make_response(jsonify({'message': 'Successfully added student.', 'Student_ID': new_student_id}), 201)
        return response