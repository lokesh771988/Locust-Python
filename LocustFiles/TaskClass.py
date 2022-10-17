from locust import User, task, between


def get_Method(UserClass):
    print("Get Method")


def post_Method(UserClass):
    print("Post Method")


class myScript(User):
    wait_time = between(1, 2)
    #tasks = [get_Method, post_Method] # List type Declare
    tasks = {get_Method: 2, post_Method: 4}
