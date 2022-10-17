from locust import User, task, between, constant, constant_pacing


class myScript(User):
    wait_time = constant_pacing(2)

    @task
    def get_Method(self):
        print("Get Method")

    @task
    def post_Method(self):
        print("Post Method")