import User


class SocialNetwork:
    def __init__(self, name: str):
        self.name = name
        self.users = {}
        print("The social network " + self.name + " was created!")

    def sign_up(self, username: str, password: str):
        if username in self.users:
            print("username already taken")

        elif len(password) > 8 or len(password) < 4:
            print("Invalid password")

        else:
            new_user = User.User(username, password)
            self.users[username] = new_user
            return new_user

    def log_in(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            self.users[username]['is_online'] = True #לא יודעות אם מתקמפל
        else:
            pass

    def log_out(self,username):
        if username in self.users:
            self.users[username]['is_online'] = False
        else:
            pass


