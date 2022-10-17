from locust import User, task, between, events


@events.test_start.add_listener
def script_start(**kwargs):
    print("before Class Start")


@events.test_stop.add_listener
def script_stop(**kwargs):
    print("before Class Stop")


class myUser(User):
    wait_time = between(1, 2)

    def on_start(self):
        print("Login Page")

    @task
    def Home_page(self):
        print("Home Page")

    def on_stop(self):
        print("Logout")
