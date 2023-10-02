"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
"""
1) Crear API de una Familia
2) Agregar miembros a una Familia
3) Actualizar miembros de una Familia
4) Borrar miembros de una Familia
5) Obtener miembros de un Familia
"""

from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)
    
    def add_member(self, member):
        self._members.append(member)

    def delete_member(self, member_id):
        for member in self._members:
            if member['id'] == member_id:
                self._members.remove(member)
                return True
        return False

    def get_member(self, member_id):
        for member in self._members:
            if member['id'] == member_id:
                return member
        return None

    def get_all_members(self):
        return self._members  

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
