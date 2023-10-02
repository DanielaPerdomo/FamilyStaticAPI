"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200


@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member is None:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member), 200


@app.route('/member', methods=['POST'])
def add_member():
    new_member_data = request.get_json()
    new_member_id = new_member_data.get('id', None)
    if new_member_id is None:
        new_member_id = jackson_family._generateId()
    new_member_data['id'] = new_member_id

    jackson_family.add_member(new_member_data)

    members = jackson_family.get_all_members()
    return jsonify({"message": "Member added successfully", "count": len(members)}), 200


@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    if jackson_family.delete_member(member_id):
        members = jackson_family.get_all_members()
        return jsonify({"done": True, "count": len(members)}), 200
    else:
        return jsonify({"error": "Member not found"}), 404


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
