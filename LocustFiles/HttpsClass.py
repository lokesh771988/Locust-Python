from locust import HttpUser, task, between


class myScript(HttpUser):
    wait_time = between(1, 2)
    host = "https://locust.io/"

    @task
    def get_Method(self):
        print("Get Method")
        res = self.client.get("", name="Get Method")
        print(res.text)