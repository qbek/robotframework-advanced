import requests
import uuid
import json

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from requests import get

from robot.api.deco import keyword

your_token = "d469ce54eca3a7ca5b6b5e7d4c8d51ced8d4c7b1"
ROBOT_AUTO_KEYWORDS = False


@keyword("Create project with name")
def projectCreation(name):
    resp = requests.post(
        "https://api.todoist.com/rest/v1/projects",
        data=json.dumps({
            "name": name
        }),
        headers={
            "Content-Type": "application/json",
            "X-Request-Id": str(uuid.uuid4()),
            "Authorization": "Bearer %s" % your_token
        }).json()

    global project_id
    project_id = resp["id"]

    logger.console("I'm WORKING!!!")
    logger.console(resp)
    privateFunction()


@keyword("Check if project was created with name")
def getProjectDetails(name):
    logger.console("Project id to get: %d" % project_id)
    resp = requests.get(
        "https://api.todoist.com/rest/v1/projects/%d" % project_id,
        headers={
            "Authorization": "Bearer %s" % your_token
        }).json()

    logger.console(resp)
    BuiltIn().should_be_equal(name, resp["name"])


@keyword
def getProjectId():
    logger.console(f"project_id: {project_id}")


@keyword
def resetData():
    global project_id
    project_id = -1


def privateFunction():
    logger.console("I'm private!!!")
