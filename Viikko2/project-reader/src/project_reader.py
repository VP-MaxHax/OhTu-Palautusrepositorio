from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = toml.loads(request.urlopen(self._url).read().decode("utf-8"))
        print(content)

        p = Project(content["tool"]["poetry"]["name"], content["tool"]["poetry"]["description"], content["tool"]["poetry"]["dependencies"], content["tool"]["poetry"]["group"]["dev"]["dependencies"], content["tool"]["poetry"]["authors"], content["tool"]["poetry"]["license"])
        return Project(p.name, p.description, p.dependencies, p.dev_dependencies, p.authors, p.license)
