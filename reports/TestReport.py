import requests
import uuid
import json

from robot.api import logger


class TestReport:
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, token, exclude):
        self.your_token = token
        self.exclude = exclude
        logger.console("Token: %s" % token)

    def start_suite(self, name, attributes):
        if name != self.exclude:
            resp = requests.post(
                "https://api.todoist.com/rest/v1/projects",
                data=json.dumps({
                    "name": name
                }),
                headers={
                    "Content-Type": "application/json",
                    "X-Request-Id": str(uuid.uuid4()),
                    "Authorization": "Bearer %s" % self.your_token
                }).json()
            self.project_id = resp["id"]
            logger.console("Stored project id: %d" % self.project_id)

    def end_test(self, name, attributes):

        requests.post(
            "https://api.todoist.com/rest/v1/tasks",
            data=json.dumps({
                "content": "%s : %s" % (name, attributes["status"]),
                "project_id": self.project_id
            }),
            headers={
                "Content-Type": "application/json",
                "X-Request-Id": str(uuid.uuid4()),
                "Authorization": "Bearer %s" % self.your_token
            }).json()
