from robot.api import logger
from github import Github



class BugReport:
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self, token, repo):
        self.token = token
        self.repo = repo

    def end_test(self, data, result):
        if result.status == 'FAIL':
            logger.console("Test FAILED - we need to report bug")
            logger.console(data.name)
            keywords_to_report = "Steps to reproduce: \n"

            for keyword in data.keywords:
                logger.console("keyword: %s" % keyword.name)
                keywords_to_report = keywords_to_report + "keyword: %s \n" % keyword.name

            # using an access token
            logger.console(keywords_to_report)
            g = Github(self.token)
            repo = g.get_repo(self.repo)
            repo.create_issue(title=data.name, body=keywords_to_report)
