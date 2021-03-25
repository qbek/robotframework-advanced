from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
import sys

ROBOT_LISTENER_API_VERSION = 2

logger.console("Hello world!")


def start_keyword(name, attr):
    logger.console("Keyword: %s" % name)
    logger.console("Our test variable value before keyword:")
    logger.console(BuiltIn().get_variable_value("${test_var}"))


def end_keyword(name, attr):
    logger.console("Our test variable value after keyword:")
    logger.console(BuiltIn().get_variable_value("${test_var}"))

    answer = input(": contine? (enter=yes, n=stop)?")
    if answer == "n":
        sys.exit("Execution stoped")
