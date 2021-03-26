import requests
import uuid
import json

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn


from robot.api.deco import keyword


class restapi:

    ROBOT_AUTO_KEYWORDS = False
    your_token = "d469ce54eca3a7ca5b6b5e7d4c8d51ced8d4c7b1"

    @keyword("Create project with name")
    def projectCreation(self, name):
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
        logger.console("I'm WORKING!!!")
        logger.console(resp)
        self.privateFunction()

    @keyword("Check if project was created with name")
    def getProjectDetails(self, name):
        logger.console(f"Project id to get: {self.project_id}")
        resp = requests.get(
            "https://api.todoist.com/rest/v1/projects/%d" % self.project_id,
            headers={
                "Authorization": "Bearer %s" % self.your_token
            }).json()

        logger.console(resp)
        return "dupa"
        # BuiltIn().should_be_equal(name, resp["name"])

    @keyword
    def getProjectId(self):
        logger.console(f"project_id: {self.project_id}")

    def privateFunction(self):
        logger.console("I'm private!!!")
