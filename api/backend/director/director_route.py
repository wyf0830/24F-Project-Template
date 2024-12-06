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
        pr.Report_ID AS Report_ID, 
        pr.Summary AS Performance_Summary, 
        pr.Date AS Performance_Report_Date,
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
        LEFT JOIN Performance_Report pr ON pd.Director_ID = pr.Director_ID
    '''
    
    cursor = db.get_db().cursor()

    cursor.execute(query)

    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response