from locust import User, task, between


class myCLass1(User):
    # wait_time = between(1, 2)
    weight = 2

    @task
    def my1(self):
        print("my CLass 1")


class myClass2(User):
    # wait_time = between(1, 2)
    weight = 3

    @task
    def my2(self):
        print("my CLass 2")


class myClass3(User):
    # wait_time = between(1, 2)
    weight = 4

    @task
    def my3(self):
        print("my CLass 3")
