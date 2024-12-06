from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
director = Blueprint('director', __name__)

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
@director.route('/data_dashboard', methods=['GET'])
def get_data_dashboard():

    query = '''
        SELECT *
        FROM Program_Director pd
        LEFT JOIN Program_Metrics pm ON pd.Director_ID = pm.Director_ID
        LEFT JOIN Student s ON pm.Metrics_ID = s.Student_ID
        LEFT JOIN Resource_Allocation ra ON pd.Director_ID = ra.Director_ID
        LEFT JOIN Job_Position jp ON ra.Allocation_ID = jp.Position_ID
        LEFT JOIN Employer e ON jp.Employer_ID = e.Employer_ID
        LEFT JOIN Performance_Report pr ON pd.Director_ID = pr.Director_ID
        '''
    
    cursor = db.get_db().cursor()

    cursor.execute(query)

    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response