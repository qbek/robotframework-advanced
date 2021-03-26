import requests
import uuid
import json

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword


class restapi:

    ROBOT_AUTO_KEYWORDS = False

    def __init__(self, token):
        self.your_token = token

    @keyword("Create project with name")
    def projectCreation(self, name):
        logger.console("I'm WORKING!!!")
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
        BuiltIn().should_be_equal(name, resp["name"])
        self.projectResponse = resp
        logger.info(resp, also_console=True)

    @keyword("Check if project was created with name")
    def getProjectDetails(self, name):
        logger.console(f"Project id to get: {self.projectResponse['id']}")
        resp = requests.get(
            "https://api.todoist.com/rest/v1/projects/%d" % self.projectResponse['id'],
            headers={
                "Authorization": "Bearer %s" % self.your_token
            }).json()
        logger.info(resp, also_console=True)
        BuiltIn().should_be_equal(resp, self.projectResponse)



    @keyword
    def getProjectId(self):
        logger.console(f"project_id: {self.projectResponse['id']}")
