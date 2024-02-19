from Post import PostFactory, PostTypes, Post


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.following = []
        self.followers = []
        self.posts = []
        self.notifications = []
        self.is_online = True

    # in main when we print the object it will know how to print by this method
    def __str__(self):
        return (f"User name: {self.username}, Number of posts: {len(self.posts)}"
                f", Number of followers: {len(self.followers)}")

    # this method will be used while using "observer" design pattern.
    # it will update a user and add the notification to his notification list
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

    def notify_observers(self, notification):
        for follower in self.followers:
            follower.update(self, notification)

    # when a user follow other user, the other user is added to the user following list
    # the user is added to the other user follower list
    def follow(self, other_user):
        if other_user not in self.following:
            self.following.append(other_user)
            other_user.followers.append(self)
            print(self.username, "started following", other_user.username)

    # when a user unfollow other user, the other user is removed from the user following list
    # the user is removed from the other user follower list
    def unfollow(self, other_user: 'User'):
        if other_user in self.following:
            self.following.remove(other_user)
            other_user.followers.remove(self)
            print(self.username, "unfollowed", other_user.username)

    # in this method we will use "factory" design pattern
    # here we are actually publishing a post. we don't need to handle here which type is the post of.
    # This we are doing in PostFactory class
    def publish_post(self, post_type, content, *args):
        new_post = PostFactory()
        post = new_post.post_factory(self, PostTypes(post_type), content, *args)
        self.posts.append(post)
        post.add_observer(self)
        print(post)
        return post

    # printing the list of the notifications of the user
    def print_notifications(self):
        if self.notifications:  # Check if there are any notifications
            print(f"{self.username}'s notifications:")
            for notification in self.notifications:
                print(notification)
        else:
            print("No notifications.")




