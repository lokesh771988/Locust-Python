from locust import User, task, between, SequentialTaskSet


class myScript(SequentialTaskSet):

    @task
    def get_Method(self):
        print("Get Method")

    @task
    def post_Method(self):
        print("Post Method")


class myUser(User):
    wait_time = between(1, 2)
    tasks = [myScript]