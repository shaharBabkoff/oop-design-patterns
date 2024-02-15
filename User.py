import Post


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.following = []
        self.observers = []
        self.posts = []
        self.notifications = []
        self.is_online = True

    def __str__(self):
        return (f"User name: {self.username}, Number of posts: {len(self.posts)}"
                f", Number of followers: {len(self.observers)}")

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, notification):
        for observer in self.observers:
            observer.update(self, notification)

    def update(self, observable, notification: str):
        self.notifications.append(notification)

    def like(self, post):
        if self not in post.liked_by:
            post.liked_by.append(self)
        else:
            pass

    def comment(self, post):
        if self not in post.comments_by:
            post.comments_by.append(self)
        else:
            pass

    def follow(self, other_user):
        if other_user not in self.following:
            self.following.append(other_user)
            other_user.add_observer(self)
            print(self.username, "started following", other_user.username, "")

    def unfollow(self, other_user: 'User'):
        if other_user in self.following:
            self.following.remove(other_user)
            other_user.remove_observer(self)
            print(self.username, "unfollowed", other_user.username, "")

    def publish_post(self, post_type, content, *args):
            if post_type == "Text":
                post = Post.TextPost(self, content)
            elif post_type == "Image":
                post = Post.ImagePost(self, content)
            elif post_type == "Sale":
                post = Post.SalePost(self, content, *args)  # SalePost expects *args for additional info like price
            else:
                print(f"Unsupported post type: {post_type}")
                return None
            self.posts.append(post)
            post.add_observer(self)
            # self.notify_observers(f"{self.username} has a new post")
            print(post)

            return post

    def print_notifications(self):
        if self.notifications:  # Check if there are any notifications
            print(f"{self.username}'s notifications:")
            for notification in self.notifications:
                print(notification)
        else:
            print("No notifications.")




