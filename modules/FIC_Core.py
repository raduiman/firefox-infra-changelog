import json

from modules.FIC_Github import FICGithub
from modules.FIC_Mercurial import FICMercurial
from modules.FIC_FileHandler import FICFileHandler
from modules.FIC_Logger import FICLogger


class FICCore(FICGithub, FICMercurial, FICFileHandler, FICLogger):
    def __init__(self):
        FICGithub.__init__(self)
        FICMercurial.__init__(self)
        FICFileHandler.__init__(self)
        FICLogger.__init__(self)
        self.check_tool_integrity()

    def run_fic(self, all=False, git_only=False, hg_only=False, repo_list=None, days=3, logging=False):
        # Don't forget about days!
        if all:
            # Needs to be replaced with whatever we want the script to do.
            # In this case, with a method that should run the script in all modes.
            print("Changelog has run in All mode!")
            self._run_all_behavioral()

        if git_only:
            print("Changelog has run in git only mode!")
            self._run_git_behavioral()

        if hg_only:
            print("Changelog has run in hg only mode!")
            self._run_hg_behavioral()

        if repo_list:
            print("Changelog has run with a custom list of repositories!")
            self._run_custom_repos_behavioral(repo_list)

    def _markdown(self):
        self.git_markdown()
        self.hg_markdown()
        self.main_markdown()

    def _run_all_behavioral(self):
        # Describes the behavioral of the script that runs in all mode.
        print("Testing run all behavioral...")

        for hosting_service in json.load(self.load(None, "repositories.json")):
            for repo in json.load(self.load(None, "repositories.json")).get(hosting_service):
                self.repo_name = repo
                if hosting_service == "Github":
                    self.start_git()
                else:
                    self.start_hg(repo_name=self.repo_name)

    def _run_git_behavioral(self):
        # Describes the behavioral of the script that runs in git only mode.
        print("Testing git mode behavioral...")

        for repo in json.load(self.load(None, "repositories.json")).get("Github"):
            self.repo_name = repo
            self.start_git()

    def _run_hg_behavioral(self):
        # Describes the behavioral of the script that runs in hg only mode.
        print("Testing hg mode behavioral...")

        for repo in json.load(self.load(None, "repositories.json")).get("HG"):
            self.repo_name = repo
            self.start_hg(repo_name=self.repo_name)

    def _run_custom_repos_behavioral(self, repo_list):
        # Describes the behavioral of the script that runs with custom repos mode.
        print("Testing custom repositories mode behavioral...")

        for repo in repo_list:
            self.repo_name = repo
            try:
                self.start_git()
            except TypeError:
                self.start_hg(repo_name=self.repo_name)
