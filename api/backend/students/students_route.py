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


@students.route('/students', methods=['POST'])
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
        query = '''
            INSERT INTO Student (Name, Major, Interests, Program, Profile_Status)
            VALUES (%s, %s, %s, %s, %s)
        '''
        data = (name, major, interests, program, profile_status)

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, data)
        db.get_db().commit()
            
        # Get the ID of the newly created employer
        new_id = cursor.lastrowid
        current_app.logger.info(f'New student added with ID: {new_id}')
            
        # Prepare the response
        response = {
            'message': 'Student added successfully',
            'student_id': new_id
        }
        return make_response(jsonify(response), 201)

# PUT Route: Update an Existing Student
@students.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    try:
        the_data = request.json
        name = the_data.get('name')
        major = the_data.get('major')
        interests = the_data.get('interests')
        program = the_data.get('program')
        profile_status = the_data.get('profile_status', None)

        # Construct the UPDATE query
        query = '''
            UPDATE Student
            SET Name = %s, Major = %s, Interests = %s, Program = %s, Profile_Status = %s
            WHERE Student_ID = %s
        '''
        data = (name, major, interests, program, profile_status, student_id)
        cursor = db.get_db().cursor()
        rows_affected = cursor.execute(query, data)
        db.get_db().commit()

        if rows_affected == 0:
            return make_response(jsonify({'error': 'Student not found'}), 404)

        response = {'message': 'Student updated successfully'}
        return make_response(jsonify(response), 200)

    except Exception as e:
        current_app.logger.error(f"Error updating student: {e}")
        return make_response(jsonify({'error': 'Internal Server Error'}), 500)
    
# DELETE Route: Delete an Student
@students.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        # SQL query to delete an student by Student_ID
        query = '''
            DELETE FROM Student
            WHERE Student_ID = %s
        '''
        cursor = db.get_db().cursor()
        cursor.execute(query, (student_id,))
        db.get_db().commit()

        # Check if the deletion affected any rows
        if cursor.rowcount == 0:
            return make_response(jsonify({'error': 'Student not found'}), 404)

        return make_response(jsonify({'message': 'Student deleted successfully!'}), 200)

    except Exception as e:
        # Handle unexpected errors
        return make_response(jsonify({'error': str(e)}), 500)


# Endpoint to fetch job listings
@students.route('/job_listings', methods=['GET'])
def get_job_listings():
    query = '''
        SELECT * FROM Job_Position
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

# Endpoint to predict job satisfaction
@students.route('/job_prediction/<int:experience>/<int:salary>', methods=['GET'])
def predict_job_satisfaction(experience, salary):
    # Simple satisfaction formula for demonstration purposes
    satisfaction_score = max(0, min(10, (experience * 2 + salary / 20000) / 2))
    response = {
        "experience": experience,
        "salary": salary,
        "satisfaction_score": satisfaction_score,
        "interpretation": "Highly satisfied" if satisfaction_score >= 7 else "Moderately satisfied" if satisfaction_score >= 4 else "Not satisfied"
    }
    return jsonify(response), 200