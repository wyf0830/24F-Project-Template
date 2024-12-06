from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
director = Blueprint('director', __name__)


#------------------------------------------------------------
# Get all customers from the system
@director.route('/dashboard', methods=['GET'])
def get_data_dashboard():

    query = '''
        SELECT pd.director_id AS Director_ID, 
            pd.name AS Director_Name, 
            pd.contact_info AS Director_Contact,
            ra.Allocation_ID AS Resource_Allocation_ID, 
            ra.Resource_Type AS Resource_Type,
            s.Student_ID, s.Name AS Student_Name, 
            s.Major AS Student_Major, 
            s.Program AS Student_Program,
            ef.Details AS Employer_Feedback,
            pm.Metrics_Name AS Metrics_Name
        FROM Program_Director pd
            LEFT JOIN Program_Metrics pm ON pd.Director_ID = pm.Director_ID
            LEFT JOIN Employer_Feedback ef ON pm.Metrics_ID = ef.Metrics_ID
            LEFT JOIN Student s ON pm.Metrics_ID = s.Student_ID
            LEFT JOIN Resource_Allocation ra ON pd.Director_ID = ra.Director_ID
        ORDER BY pd.director_id
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@director.route('/dashboard/<int:director_id>', methods=['PUT'])
def update_data_dashboard(director_id):
    try:
        # Extract JSON payload from the request
        data = request.get_json()

        # Validate the required fields
        if not data.get('Director_Name') or not data.get('Director_Contact'):
            return make_response(jsonify({'error': 'Missing Director Name or Contact Info'}), 400)

        # Start the database transaction
        conn = db.get_db()
        cursor = conn.cursor()

        # Update Program_Director table
        update_query_director = '''
            UPDATE Program_Director
            SET name = %s,
                contact_info = %s
            WHERE director_id = %s
        '''
        cursor.execute(update_query_director, (data['Director_Name'], data['Director_Contact'], director_id))

        # Update Resource_Allocation table using derived table
        if data.get('Resource_Type'):
            update_query_resource = '''
                UPDATE Resource_Allocation ra
                JOIN (
                    SELECT Allocation_ID
                    FROM Resource_Allocation
                    WHERE Director_ID = %s
                    LIMIT 1
                ) AS temp ON ra.Allocation_ID = temp.Allocation_ID
                SET ra.Resource_Type = %s
            '''
            cursor.execute(update_query_resource, (director_id, data['Resource_Type']))

        # Update Program_Metrics table using derived table
        if data.get('Metrics_Name'):
            update_query_metrics = '''
                UPDATE Program_Metrics pm
                JOIN (
                    SELECT Metrics_ID
                    FROM Program_Metrics
                    WHERE Director_ID = %s
                    LIMIT 1
                ) AS temp ON pm.Metrics_ID = temp.Metrics_ID
                SET pm.Metrics_Name = %s
            '''
            cursor.execute(update_query_metrics, (director_id, data['Metrics_Name']))

        # Commit the changes
        conn.commit()

        return make_response(jsonify({'message': 'Director updated successfully!'}), 200)

    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)


@director.route('/reports', methods=['GET', 'POST'])
def handle_performance_reports():
    if request.method == 'GET':
        # SQL query to fetch performance reports
        query = '''
            SELECT pd.director_id AS Director_ID, 
                pd.name AS Director_Name, 
                pd.contact_info AS Director_Contact,
                pr.Report_ID AS Report_ID, 
                pr.Summary AS Performance_Summary, 
                pr.Date AS Performance_Report_Date
            FROM Performance_Report pr
                LEFT JOIN Program_Director pd ON pd.Director_ID = pr.Director_ID
            ORDER BY pd.director_id
        '''
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()

        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    elif request.method == 'POST':
        try:
            # Extract JSON payload
            data = request.get_json()
            director_id = data.get('Director_ID')
            summary = data.get('Summary')
            date = data.get('Date')

            # Validate input
            if not director_id or not summary or not date:
                return make_response(jsonify({'error': 'Missing required fields: Director_ID, Summary, or Date'}), 400)

            # Insert into database
            query = '''
                INSERT INTO Performance_Report (Director_ID, Summary, Date)
                VALUES (%s, %s, %s)
            '''
            cursor = db.get_db().cursor()
            cursor.execute(query, (director_id, summary, date))
            db.get_db().commit()

            return make_response(jsonify({'message': 'Performance report created successfully!'}), 201)

        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)


@director.route('/reports/<int:report_id>', methods=['DELETE'])
def delete_performance_report(report_id):
    try:
        # SQL query to delete a performance report by Report_ID
        query = '''
            DELETE FROM Performance_Report
            WHERE Report_ID = %s
        '''
        cursor = db.get_db().cursor()
        cursor.execute(query, (report_id,))
        db.get_db().commit()

        if cursor.rowcount == 0:
            return make_response(jsonify({'error': 'Report not found'}), 404)

        return make_response(jsonify({'message': 'Performance report deleted successfully!'}), 200)

    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
    

@director.route('/employer', methods=['GET'])
def get_employer_data():

    query = '''
        SELECT pd.director_id AS Director_ID, 
            pd.name AS Director_Name, 
            pd.contact_info AS Director_Contact,
            s.Student_ID, s.Name AS Student_Name, 
            s.Major AS Student_Major, 
            s.Program AS Student_Program,
            ef.Details AS Employer_Feedback,
            jp.Title AS Job_Title,
            e.Name AS Employer_Name,
            e.Contact_Info AS Employer_Contact,
            e.Industry AS Industry
        FROM Program_Director pd
            LEFT JOIN Program_Metrics pm ON pd.Director_ID = pm.Director_ID
            LEFT JOIN Employer_Feedback ef ON pm.Metrics_ID = ef.Metrics_ID
            LEFT JOIN Student s ON pm.Metrics_ID = s.Student_ID
            LEFT JOIN Job_Position jp on jp.Position_ID = ef.Position_ID
            LEFT JOIN Employer e ON e.Employer_ID = jp.Employer_ID
        ORDER BY pd.director_id
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response