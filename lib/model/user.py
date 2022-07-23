GUEST = {
    "name": "guest",
    "home_directory": "c:/",
    "isAdmin": False,
    "pass": "guest"
}

class User:
    def __init__(self, name, home_directory, isAdmin, guest = False):
        self.name = name
        self.home_directory = home_directory
        self.isAdmin = isAdmin
        self.guest = guest

    def db_format(self):
        return (self.name, self.home_directory, self.isAdmin) if not self.guest else (self.name, self.home_directory, self.isAdmin, GUEST["pass"])

        

    @staticmethod
    def get_guest_account():
        return User(GUEST["name"], GUEST["home_directory"], GUEST["isAdmin"], True)

    def __str__(self):
        return "name: {}, privileges: {}\nhome_directory: {}".format(self.name, self.isAdmin, self.home_directory)
        
    def __repr__(self):
        return "User (\"{}\", \"{}\", {})".format(self.name, self.home_directory, self.isAdmin)

    