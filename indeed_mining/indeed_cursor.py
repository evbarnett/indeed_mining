from typing import List
from indeed_mining.indeed_job import IndeedJob


class IndeedCursor(object):
    """TODO."""

    def __init__(self, req_url: str):
        self.req_url = req_url

    def get_next_jobs(self) -> List[IndeedJob]:
        """TODO.

        Returns: List[IndeedJob]. List can be empty.
        """
        pass
