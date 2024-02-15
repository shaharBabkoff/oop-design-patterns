import User
import matplotlib.pyplot as plt
from enum import Enum


# this method define all the types of the post
class PostTypes(Enum):
    TextPost = "Text"
    ImagePost = "Image"
    SalePost = "Sale"


# here on the code we will use "factory" design pattern:
class PostFactory:

    # the function gets type of post and his content and return a new post
    def post_factory(self, user, post_type, content, *args):
        if post_type == PostTypes.TextPost:
            return TextPost(user, content)
        elif post_type == PostTypes.ImagePost:
            return ImagePost(user, content)
        elif post_type == PostTypes.SalePost:
            return SalePost(user, content, *args)
        else:
            raise ValueError("Invalid post type")


class Post:

    def __init__(self, user, content):
        self.content = content
        self.user = user
        self.liked_by = []
        self.comments = []
        self.observers = []
        self.notify_observers(f"{user.username} has a new post")

    # here on the code we will use "observer" design pattern:
    # the post is observable and this are the methods that need to be implemented (as we learned on class)
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
            # we want to notify obout the like only if someone else liked the post (not the owner)
            if user.username != self.user.username:
                # when someone like user's post, the user should be updated
                # So we notify the observers (in our case it is only the owner of the post)
                self.notify_observers(f"{user.username} liked your post")
                print(f"notification to {self.user.username}: {user.username} liked your post")

    def comment(self, user: User, text: str):
        self.comments.append((user, text))
        # we want to notify obout the comment only if someone else commented the post (not the owner)
        if user.username != self.user.username:
            # when someone comment user's post, the user should be updated
            # So we notify the observers (in our case it is only the owner of the post)
            self.notify_observers(f"{user.username} commented on your post")
            print(f"notification to {self.user.username}: {user.username} commented on your post: {text}")


# there are 3 types of posts. for each type we created a class.
# In which class we will define the post with his parameters
class TextPost(Post):
    def __init__(self, user, content):
        super().__init__(user, content)

    def __str__(self):
        return f"{self.user.username} published a post:\n{self.content}\n"


class ImagePost(Post):
    def __init__(self, user, content):
        super().__init__(user, content)
        self.image_path = content
        # self.notify_observers(f"{user.username} has a new post")

    def display(self):
        print(f"Shows picture")

        try:
            plt.imshow(plt.imread(self.image_path))
            plt.title(self.user.use)
            plt.show()
        except FileNotFoundError:
            print(f"Image file {self.image_path} not found.")

    def __str__(self):
        return f"{self.user.username} posted a picture\n"


class SalePost(Post):
    def __init__(self, user, content, price, location):
        super().__init__(user, content)
        self.price = price
        self.location = location
        self.is_available = True

    def __str__(self):
        if self.is_available:
            return (f"{self.user.username} posted a product for sale:\n For sale! {self.content},"
                    f" price: {self.price}, pickup from: {self.location}\n")
        else:
            return (f"{self.user.username} posted a product for sale:\nSold! {self.content},"
                    f" price: {self.price}, pickup from: {self.location}\n")

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
        print(f"{self.user.username}'s product is sold")

