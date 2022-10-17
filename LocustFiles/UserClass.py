from locust import User, task, between, constant


class myScript(User):
    wait_time = between(1, 2)

    @task
    def get_Method(self):
        print("Get Method")

    @task
    def post_Method(self):
        print("Post Method")


class myScript1(User):
    wait_time = between(1, 2)

    @task
    def get_Method(self):
        print("Get Method1")

    @task
    def post_Method(self):
        print("Post Method1")