from abc import ABC, abstractmethod


class Subscriber:

    @abstractmethod
    def notify(self, msg):
        pass


class User(Subscriber):
    def __init__(self, user_id):
        self.user_id = user_id

    def notify(self, msg):
        print(f"User {self.user_id} received msg {msg}")


class Group:
    def __init__(self):
        self.users = []

    def subscribe(self, user: Subscriber):
        self.users.append(user)

    def unsubscribe(self, user: Subscriber):
        self.users.remove(user)

    def notify(self, msg):
        for user in self.users:
            user.notify(msg)


if __name__ == '__main__':
    group = Group()
    user1 = User(1)
    user2 = User(2)
    user3 = User(3)

    group.subscribe(user1)
    group.subscribe(user2)
    group.subscribe(user3)

    group.notify("new msg")
    group.unsubscribe(user1)
    group.notify("new new msg")
