from locust import User, task, between, TaskSet


class userBehavire(TaskSet):

    @task(2)
    class nestedClass(TaskSet):

        @task(1)
        def get_Method(self):
            print("Get Method")

        @task(2)
        def post_Method(self):
            print("Post Method")
            self.interrupt()

    @task(3)
    class nestedClass1(TaskSet):
        @task(1)
        def a_Method(self):
            print("a Method")

        @task(2)
        def b_Method(self):
            print("b Method")
            self.interrupt()


class myUser(User):
    wait_time = between(1, 2)
    tasks = [userBehavire]