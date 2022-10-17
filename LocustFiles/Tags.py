from locust import User, task, between, SequentialTaskSet, tag


class myScript(SequentialTaskSet):

    @task
    @tag('get', 'sanity')
    def get_Method(self):
        print("Get Method")

    @task
    @tag('patch', 'sanity')
    def patch_Method(self):
        print("Patch Method")

    @task
    @tag('post')
    def post_Method(self):
        print("Post Method")


class myUser(User):
    wait_time = between(1, 2)
    tasks = [myScript]
