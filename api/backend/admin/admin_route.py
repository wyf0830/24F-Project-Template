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
    
# PUT Route: Update an Existing Employer
@admin.route('/employers/<int:employer_id>', methods=['PUT'])
def update_employer(employer_id):
    try:
        the_data = request.json
        name = the_data.get('name')
        contact_info = the_data.get('contact_info')
        industry = the_data.get('industry', None)
        profile_status = the_data.get('profile_status', None)

        if not name or not contact_info:
            return make_response(jsonify({'error': 'Missing required fields: name and contact_info.'}), 400)

        # Construct the UPDATE query
        query = '''
            UPDATE Employer
            SET Name = %s, Contact_Info = %s, Industry = %s, Profile_Status = %s
            WHERE Employer_ID = %s
        '''
        data = (name, contact_info, industry, profile_status, employer_id)
        cursor = db.get_db().cursor()
        rows_affected = cursor.execute(query, data)
        db.get_db().commit()

        if rows_affected == 0:
            return make_response(jsonify({'error': 'Employer not found'}), 404)

        response = {'message': 'Employer updated successfully'}
        return make_response(jsonify(response), 200)

    except Exception as e:
        current_app.logger.error(f"Error updating employer: {e}")
        return make_response(jsonify({'error': 'Internal Server Error'}), 500)

# DELETE Route: Delete an Employer
@admin.route('/employers/<int:employer_id>', methods=['DELETE'])
def delete_employer(employer_id):
    try:
        # SQL query to delete an employer by Employer_ID
        query = '''
            DELETE FROM Employer
            WHERE Employer_ID = %s
        '''
        cursor = db.get_db().cursor()
        cursor.execute(query, (employer_id,))
        db.get_db().commit()

        # Check if the deletion affected any rows
        if cursor.rowcount == 0:
            return make_response(jsonify({'error': 'Employer not found'}), 404)

        return make_response(jsonify({'message': 'Employer deleted successfully!'}), 200)

    except Exception as e:
        # Handle unexpected errors
        return make_response(jsonify({'error': str(e)}), 500)

@admin.route('/admin_data', methods=['GET'])
def get_admin_data():
    query = '''
    SELECT sl.Log_ID,
        sl.Event_Type,
        sl.Message AS Log_Message,
        sl.Time_Stamp AS Log_Time_Stamp,
        r.Report_ID,
        r.Generated_Date AS Report_Date,
        r.Content AS Report_Content,
        r.Report_Type,
        bs.Schedule_ID,
        bs.Frequency AS Backup_Frequency,
        bs.Last_Backup_Date
    FROM Admin a
        LEFT JOIN System_Logs sl ON a.Admin_ID = sl.Admin_ID
        LEFT JOIN Reports r ON a.Admin_ID = r.Admin_ID
        LEFT JOIN Backup_Schedule bs ON a.Admin_ID = bs.Admin_ID
    ORDER BY 
        sl.Time_Stamp DESC, r.Generated_Date DESC, bs.Last_Backup_Date DESC
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@admin.route('/admin_data', methods=['POST'])
def add_admin_data():
    try:
        # Extract the JSON payload from the request
        data = request.get_json()

        # Extract the required fields for each table
        admin_id = data.get('Admin_ID')
        event_type = data.get('Event_Type')
        log_message = data.get('Log_Message')
        report_content = data.get('Report_Content')
        report_type = data.get('Report_Type')
        backup_frequency = data.get('Backup_Frequency')

        # Validate that at least one field is provided
        if not (event_type or log_message or report_content or report_type or backup_frequency):
            return make_response(
                jsonify({"error": "At least one field must be provided to add data"}), 400
            )

        # Get a database connection
        conn = db.get_db()
        cursor = conn.cursor()

        # Step 1: Insert data into System_Logs table (if provided)
        if event_type and log_message:
            log_query = '''
                INSERT INTO System_Logs (Admin_ID, Event_Type, Message)
                VALUES (%s, %s, %s)
            '''
            cursor.execute(log_query, (admin_id, event_type, log_message))

        # Step 2: Insert data into Reports table (if provided)
        if report_content and report_type:
            report_query = '''
                INSERT INTO Reports (Admin_ID, Content, Report_Type)
                VALUES (%s, %s, %s)
            '''
            cursor.execute(report_query, (admin_id, report_content, report_type))

        # Step 3: Insert data into Backup_Schedule table (if provided)
        if backup_frequency:
            backup_query = '''
                INSERT INTO Backup_Schedule (Admin_ID, Frequency)
                VALUES (%s, %s)
            '''
            cursor.execute(backup_query, (admin_id, backup_frequency))

        # Commit the transaction
        conn.commit()

        # Return success response
        return make_response(
            jsonify({"message": "Admin-related data added successfully"}), 201
        )

    except Exception as e:
        # Rollback the transaction if an error occurs
        conn.rollback()
        return make_response(jsonify({"error": str(e)}), 500)
    
