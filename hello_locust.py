import time
from locust import HttpUser, task

class RunHttpUser(HttpUser):
    @task
    def ping(self):
        self.client.get("/ping")
