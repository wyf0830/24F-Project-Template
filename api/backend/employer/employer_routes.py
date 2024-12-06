from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db  # Use the existing db_connection module

# Create a Blueprint for Employer routes
employers = Blueprint('employers', __name__)

# Get all employers
@employers.route('/employers', methods=['GET'])
def get_employers():
    try:
        cursor = db.get_db().cursor()
        cursor.execute("SELECT * FROM Employer")
        employers = cursor.fetchall()
        if not employers:
            return make_response(jsonify([]), 200)  # Return an empty list if no employers are found
        return make_response(jsonify(employers), 200)
    except Exception as e:
        current_app.logger.error(f"Error fetching employers: {e}")
        return make_response(jsonify({"error": f"Failed to fetch employers: {e}"}), 500)

# Get employer by ID
@employers.route('/employers/<int:employer_id>', methods=['GET'])
def get_employer(employer_id):
    try:
        cursor = db.get_db().cursor()
        cursor.execute("SELECT * FROM Employer WHERE Employer_ID = %s", (employer_id,))
        employer = cursor.fetchone()
        if employer:
            return make_response(jsonify(employer), 200)
        else:
            return make_response(jsonify({"error": "Employer not found"}), 404)
    except Exception as e:
        current_app.logger.error(f"Error fetching employer: {e}")
        return make_response(jsonify({"error": "Failed to fetch employer"}), 500)

# Add a new employer
@employers.route('/employers', methods=['POST'])
def add_employer():
    try:
        data = request.json
        query = "INSERT INTO Employer (Name, Contact_Info, Industry, Profile_Status) VALUES (%s, %s, %s, %s)"
        cursor = db.get_db().cursor()
        cursor.execute(query, (data['name'], data['contact_info'], data['industry'], data['profile_status']))
        db.get_db().commit()
        return make_response(jsonify({"message": "Employer added successfully!"}), 201)
    except Exception as e:
        current_app.logger.error(f"Error adding employer: {e}")
        return make_response(jsonify({"error": "Failed to add employer"}), 500)

# Update an employer
@employers.route('/employers/<int:employer_id>', methods=['PUT'])
def update_employer(employer_id):
    try:
        data = request.json
        query = (
            "UPDATE Employer "
            "SET Name = %s, Contact_Info = %s, Industry = %s, Profile_Status = %s "
            "WHERE Employer_ID = %s"
        )
        cursor = db.get_db().cursor()
        cursor.execute(query, (data['name'], data['contact_info'], data['industry'], data['profile_status'], employer_id))
        db.get_db().commit()
        return make_response(jsonify({"message": "Employer updated successfully!"}), 200)
    except Exception as e:
        current_app.logger.error(f"Error updating employer: {e}")
        return make_response(jsonify({"error": "Failed to update employer"}), 500)

# Delete an employer
@employers.route('/employers/<int:employer_id>', methods=['DELETE'])
def delete_employer(employer_id):
    try:
        cursor = db.get_db().cursor()
        cursor.execute("DELETE FROM Employer WHERE Employer_ID = %s", (employer_id,))
        db.get_db().commit()
        return make_response(jsonify({"message": "Employer deleted successfully!"}), 200)
    except Exception as e:
        current_app.logger.error(f"Error deleting employer: {e}")
        return make_response(jsonify({"error": "Failed to delete employer"}), 500)
