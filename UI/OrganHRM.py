from locust import HttpUser, task, between


class myUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://opensource-demo.orangehrmlive.com"

    @task
    def login(self):
        with self.client.post("/", name="login", data={"action": "process",
                                                       "userName": "Admin",
                                                       "password": "admin123",
                                                       "login.x": "41",
                                                       "login.y": "12"}) as resp:
            if "Employee Information" in resp.text:
                resp.success()
            else:
                resp.failure("failed to login")
