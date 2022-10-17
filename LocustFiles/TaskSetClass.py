from locust import User, task, between, TaskSet


class myScript(User):
    wait_time = between(1, 2)

    @task
    class userBehavire(TaskSet):

        @task
        def get_Method(self):
            print("Get Method")

        @task
        def post_Method(self):
            print("Post Method")

        @task
        def a_Method(self):
            print("a Method")

        @task
        def b_Method(self):
            print("b Method")