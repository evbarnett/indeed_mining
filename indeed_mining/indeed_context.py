import urllib as ul

from indeed_mining.indeed_cursor import IndeedCursor


class IndeedContext(object):
    """TODO."""

    @staticmethod
    def get_cursor(title: str, location: str, radius: int = 25) -> IndeedCursor:
        base_url = "https://www.indeed.com/jobs?"
        title_esc = ul.quote(title, safe='')
        location_esc = ul.quote(title, safe='')
        req_url = base_url + "q={}&l={}".format(title_esc, location_esc)
        return IndeedCursor(req_url)
