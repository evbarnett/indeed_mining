import json


class IndeedJob(object):
    """TODO."""

    def __init__(self, title: str, location: str, is_ad: bool):
        self.title = title
        self.location = location
        self.is_ad = is_ad

    def get_content(self) -> str:
        pass
