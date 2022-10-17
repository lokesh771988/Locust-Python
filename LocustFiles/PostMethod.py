from locust import HttpUser, task, between, SequentialTaskSet
from CsvReader import CSVRead
import random


class myScript(SequentialTaskSet):

    @task
    def post_method(self):
        test_data = CSVRead("C:\\Users\\GorantlL\\PycharmProjects\\MyDemoLocust\\MyData.csv").read_data()
        print(test_data)
        pyload = {
            "name": random.choice(test_data)['name'],
            "gender": random.choice(test_data)['gender'],
            "email": random.choice(test_data)['email'],
            "status": random.choice(test_data)['status']
        }
        headers = {
            'Accept': 'Application/Json',
            'Authorization': 'Bearer 7232803c821bc49a0bd5c56d7df39c5289168e323fb17c5b6b1597d8941e33ef',
        }

        with self.client.post("/public/v2/users", name="Post Method", catch_response=True, data=pyload, headers=headers) as response:
            if response.status_code == 201:
                print(response)
                response.success()
            else:
                response.failure("Failed")


class myUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://gorest.co.in"
    tasks = [myScript]
