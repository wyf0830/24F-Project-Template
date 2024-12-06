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
        SELECT * FROM Coop_Application
        '''
    
    cursor = db.get_db().cursor()

    cursor.execute(query)

    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response