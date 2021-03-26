from robot.api import logger
import docker


class WebServer:

    def __init__(self, name):
        client = docker.from_env()
        self.container = client.containers.get(name)

    def startContainer(self):
        self.container.start()

    def stopContainer(self):
        self.container.stop()

    def modifyFile(self):
        self.container.exec_run("sed -i 's/80;/90;/' default.conf", workdir="/etc/nginx/conf.d")

    def restartContainer(self):
        self.container.restart()
