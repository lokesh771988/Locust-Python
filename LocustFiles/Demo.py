from locust import User, task, between


class myScript(User):
    wait_time = between(1, 2)

    @task
    def get_Method(self):
        print("Hellow")
        