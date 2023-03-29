
class Settings:

	def __init__(self):
		self.active = False
		self.contacts_location = "data/contacts.json"
		self.users_location = "data/users.json"

		self.contacts = None
		self.users = None

		self.menu = """
*APLIKASI CONTACTAPP*
1. VIEW ALL CONTACTS
2. FIND CONTACT BY PHONE
3. ADD NEW CONTACT
4. UPDATE CONTACT
5. REMOVE CONTACT
Q. EXIT
"""