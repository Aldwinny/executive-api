guest = {
    "name": "guest",
    "home_directory": "c:/",
    "isAdmin": False
}

class User:
    def __init__(self, name = guest["name"], home_directory = guest["home_directory"], isAdmin = guest["isAdmin"]):
        self.name = name
        self.home_directory = home_directory
        self.isAdmin = isAdmin

    def toString():
        return "name: {}, privileges: {}\nhome_directory: {}".format(self.name, self.home_directory, isAdmin)