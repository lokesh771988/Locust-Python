from locust import HttpUser, task, between


class myUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://opensource-demo.orangehrmlive.com"

    @task
    def launch_URL(self):
        with self.client.get("/", name="launchOrangHRM", catch_response=True) as resp1:
            if "OrangeHRM" in resp1.text:
                resp1.success()
            else:
                resp1.failure("failed to launch url")

    @task
    def login(self):
        with self.client.post("/", name="login", catch_response=True, data={"action": "process",
                                                                            "userName": "Admin",
                                                                            "password": "admin123",
                                                                            "login.x": "41",
                                                                            "login.y": "12"}) as resp:
            if "We're sorry but orangehrm doesn't work properly without JavaScript enabled. Please enable it to " \
               "continue." in resp.text:
                resp.success()
            else:
                resp.failure("failed to login")
