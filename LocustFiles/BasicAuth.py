from locust import HttpUser, task, between


class myUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://gorest.co.in"

    @task
    def get_method(self):
        headers = {
            'Accept': 'Application/Json',
            'Authorization': 'Bearer 7232803c821bc49a0bd5c56d7df39c5289168e323fb17c5b6b1597d8941e33ef',
        }
        with self.client.get("/public/v2/users", name="Auth Code", catch_response=True, headers=headers) as response:
            if response.status_code == 200:
                value = response.json()
                print(value)
                response.success()
            else:
                response.failure("Failed")
