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
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
director = Blueprint('director', __name__)


#------------------------------------------------------------
# Get all customers from the system
@director.route('/director', methods=['GET'])
def get_data_dashboard():

    query = '''
        SELECT COUNT(DISTINCT a.Application_ID) AS Total_Placements,
            AVG(f.Details) AS Avg_Feedback_Score,
            COUNT(DISTINCT e.Employer_ID) AS Employer_Count
        FROM Coop_Application a
        JOIN Employer_Feedback f ON a.Position_ID = f.Position_ID
        JOIN Employer e ON a.Position_ID = e.Employer_ID;
        '''
    
    cursor = db.get_db().cursor()

    cursor.execute(query)

    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
