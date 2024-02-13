import User
import matplotlib.pyplot as plt


class Post:

    def __init__(self, user, content):
        self.content = content
        self.user = user
        self.liked_by = []
        self.comments = []
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, notification):
        for observer in self.observers:
            observer.update(self, notification)

    def like(self, user):
        if user not in self.liked_by:
            self.liked_by.append(user)
            if user.username != self.user.username:
                self.notify_observers(f"{user.username} liked your post")
                print(f"notification to {self.user.username}: {user.username} liked your post")

    def comment(self, user: User, text: str):
        self.comments.append((user, text))
        if user.username != self.user.username:
            self.notify_observers(f"{user.username} commented on your post")
            print(f"notification to {self.user.username}: {user.username} commented on your post: {text}")

    def display(self):
        pass  # Implemented in subclasses


class TextPost(Post):
    def __init__(self, user, content):
        super().__init__(user, content)

    def display(self):
        print(f"{self.user.username} published a post:\n{self.content}\n")


class ImagePost(Post):
    def __init__(self, user, content):
        super().__init__(user, content)
        self.image_path = content

    def display(self):
        print(f"{self.user.username} posted a picture\n")

        try:
            plt.imshow(plt.imread(self.image_path))
            plt.title(self.user.use)
            plt.show()
        except FileNotFoundError:
            print(f"Image file {self.image_path} not found.\n")


class SalePost(Post):
    def __init__(self, user, content, price, location):
        super().__init__(user, content)
        self.price = price
        self.location = location
        self.is_available = True

    def discount(self, percentage, password):
        if self.user.password == password:
            if self.is_available:
                self.price *= (1 - percentage / 100)
                print(f"Discount on {self.user.username} product! the new price is: {self.price}\n")
        else:
            pass

    def sold(self, password):
        if self.user.password == password:
            self.is_available = False
        print(f"{self.user.username}'s product is sold\n")

    def display(self):
        availability_status = "Available" if self.is_available else "Sold"
        print(f"{self.user.username} posted a product for sale:")
        print(f"For sale! {self.content}, price: {self.price}, pickup from: {self.location}\n")


