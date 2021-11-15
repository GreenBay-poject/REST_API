from locust import HttpUser, task, between
import json

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

    @task(1)
    def view_my_posts(self):
        self.client.post(
            url=self.server+"feed/view_my_posts",
            data=json.dumps({
                "email":"mashkarharis3@gmail.com"
            }),
            headers={'content-type': 'application/json',
               'Authorization': 'Bearer RYPWXPWEEYZZSGNHGIQXRSYNQ'}

        )

    @task(1)
    def get_user_info(self):
        self.client.post(
            url=self.server+"auth/get_user_info",
            data=json.dumps({
                "email":"mashkarharis3@gmail.com"
            }),
            headers={'content-type': 'application/json',
               'Authorization': 'Bearer RYPWXPWEEYZZSGNHGIQXRSYNQ'}

        )

    @task(1)
    def view_my_notes(self):
        self.client.post(
            url=self.server+"note/view_my_notes",
            data=json.dumps({
                "email":"mashkarharis3@gmail.com"
            }),
            headers={'content-type': 'application/json',
               'Authorization': 'Bearer RYPWXPWEEYZZSGNHGIQXRSYNQ'}

        )

    @task(1)
    def get_image(self):
        self.client.get(self.server+"report/get_image?lattitude=6.177856842841487&longitude=80.2139575381279&date=2019-01-01")

    @task(1)
    def get_dates(self):
        self.client.get(self.server+"report/get_dates?lattitude=6.177856842841487&longitude=80.2139575381279")
    
    @task(1)
    def view_questions(self):
        self.client.post(
            url=self.server+"questions/view_questions",
            data=json.dumps({
                "email":"mashkarharis3@gmail.com"
            }),
            headers={'content-type': 'application/json',
               'Authorization': 'Bearer RYPWXPWEEYZZSGNHGIQXRSYNQ'}

    )