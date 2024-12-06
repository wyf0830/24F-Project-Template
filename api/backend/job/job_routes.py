from flask import Blueprint, jsonify

# Create a blueprint for job routes
job_routes = Blueprint('job_routes', __name__)

# Sample data for job listings
job_listings = [
    {"id": 1, "title": "Software Engineer", "location": "Boston", "type": "Full-time", "salary": 120000},
    {"id": 2, "title": "Data Scientist", "location": "New York", "type": "Part-time", "salary": 90000},
    {"id": 3, "title": "Product Manager", "location": "San Francisco", "type": "Contract", "salary": 130000},
    {"id": 4, "title": "Sales Associate", "location": "Chicago", "type": "Full-time", "salary": 60000}
]

# Endpoint to fetch job listings
@job_routes.route('/job/listings', methods=['GET'])
def get_job_listings():
    return jsonify(job_listings), 200

# Endpoint to predict job satisfaction
@job_routes.route('/job/prediction/<int:experience>/<int:salary>', methods=['GET'])
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
