from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)
    server="http://127.0.0.1:8000/"
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def view_public_posts(self):
        self.client.get(self.server+"feed/view_posts")

    @task(1)
    def view_public_notes(self):
        self.client.get(self.server+"note/get_public_note")

        