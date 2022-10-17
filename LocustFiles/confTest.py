from locust import HttpUser, between, task


class loadTest(HttpUser):
    wait_time = between(1, 2)

    def __init__(self, parent):
        super().__init__(parent)
        self.hostname = self.host

    @task
    def page(self):
        res = self.client.get("/public/v2/users", name=self.hostname, catch_response=True)
        print(res.text)
