from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

admin = Blueprint('admin', __name__)

@admin.route('/employers', methods = ['GET'])
def get_employers():
    query = '''
        SELECT * FROM Employer
        ORDER BY Employer_ID
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

@admin.route('/employers', methods=['POST'])
def add_new_employer():
    try:
        the_data = request.json
        current_app.logger.info(f"Received data: {the_data}")

        name = the_data.get('name')
        contact_info = the_data.get('contact_info')
        industry = the_data.get('industry', None)  # Optional field
        profile_status = the_data.get('profile_status', 1)  # Defaults to 1 if not provided

        # Validate required fields
        if not name or not contact_info:
            current_app.logger.warning("Missing required fields: 'name' or 'contact_info'.")
            return make_response(jsonify({'error': 'Missing required fields: name and contact_info.'}), 400)

        # Construct the INSERT query
        query = '''
            INSERT INTO Employer (Name, Contact_Info, Industry, Profile_Status)
            VALUES (%s, %s, %s, %s)
        '''
        data = (name, contact_info, industry, profile_status)
            
        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, data)
        db.get_db().commit()
            
        # Get the ID of the newly created employer
        new_id = cursor.lastrowid
        current_app.logger.info(f'New employer added with ID: {new_id}')
            
        # Prepare the response
        response = {
            'message': 'Employer added successfully',
            'employer_id': new_id
        }
        return make_response(jsonify(response), 201)

    except Exception as e:
        current_app.logger.error(f"Error adding new employer: {e}")
        return make_response(jsonify({'error': 'Internal Server Error'}), 500)