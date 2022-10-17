from locust import HttpUser, task, between


class myUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_method(self):
        with self.client.get("/public/v2/users", name="Get Method", catch_response=True) as response:
            if response.status_code == 200:
                print(response)
                response.success()
            else:
                response.failure("Failed")
