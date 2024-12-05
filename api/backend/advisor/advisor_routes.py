########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response
from backend.db_connection import db

# Create a Blueprint for Advisor routes
advisor = Blueprint('advisor', __name__)

# Get all advisors
@advisor.route('/advisors', methods=['GET'])
def get_advisors():
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM Advisor")  # Replace with your actual Advisor table
    advisors = cursor.fetchall()
    return make_response(jsonify(advisors), 200)

# Get an advisor by ID
@advisor.route('/advisors/<int:advisor_id>', methods=['GET'])
def get_advisor(advisor_id):
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM Advisor WHERE Advisor_ID = %s", (advisor_id,))
    advisor = cursor.fetchone()
    if advisor:
        return make_response(jsonify(advisor), 200)
    else:
        return make_response(jsonify({"error": "Advisor not found"}), 404)

# Add a new advisor
@advisor.route('/advisors', methods=['POST'])
def add_advisor():
    advisor_data = request.json
    query = "INSERT INTO Advisor (Name, Email, Department) VALUES (%s, %s, %s)"
    data = (advisor_data['name'], advisor_data['email'], advisor_data['department'])
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    return make_response(jsonify({"message": "Advisor added successfully!"}), 201)

# Update an advisor
@advisor.route('/advisors/<int:advisor_id>', methods=['PUT'])
def update_advisor(advisor_id):
    advisor_data = request.json
    query = """
    UPDATE Advisor
    SET Name = %s, Email = %s, Department = %s
    WHERE Advisor_ID = %s
    """
    data = (advisor_data['name'], advisor_data['email'], advisor_data['department'], advisor_id)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    return make_response(jsonify({"message": "Advisor updated successfully!"}), 200)

# Delete an advisor
@advisor.route('/advisors/<int:advisor_id>', methods=['DELETE'])
def delete_advisor(advisor_id):
    cursor = db.get_db().cursor()
    cursor.execute("DELETE FROM Advisor WHERE Advisor_ID = %s", (advisor_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Advisor deleted successfully!"}), 200)
