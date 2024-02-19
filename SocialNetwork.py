from User import User


class SocialNetwork:

    __instance__ = None  # for singelton design pattern

# this method create a new SocialNetwork iff it wasn't created before

    def __new__(cls, name):
        # If an instance does not exist, create one
        if cls.__instance__ is None:
            cls.__instance__ = super().__new__(cls)
            # If an instance does exist, return the instance
        return cls.__instance__

    def __init__(self, name: str):
        self.name = name
        self.users = {}
        print("The social network " + self.name + " was created!")

        # in main when we print the object it will know how to print by this method
    def __str__(self):
        users_info = [str(self.users[username]) for username in self.users]  # List comprehension to get user info
        return f"{self.name} social network:\n" + "\n".join(users_info)

    def sign_up(self, username: str, password: str):
        # check if the username is already been used
        if username in self.users:
            print("username already taken")
        # check if the password is valid
        elif len(password) > 8 or len(password) < 4:
            print("Invalid password")

        else:
            # create the new user and add him to users list of the network
            new_user = User(username, password)
            self.users[username] = new_user
            return new_user

    def log_in(self, username, password):
        # check if the username is in users list
        if username in self.users:
            user = self.users[username]
            # check if the password is correct
            if password == user.password:
                # log in successfully -> set status of user to be online
                user.is_online = True
                print(f"{username} connected")
        else:
            pass

    def log_out(self, username):
        # check if the username is in users list
        if username in self.users:
            user = self.users[username]
            # log out successfully -> set status of user to be offline
            user.is_online = False
            print(f"{username} disconnected")
        else:
            pass



