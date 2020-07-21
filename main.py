from indeed_mining import IndeedContext, IndeedJob, IndeedCursor


def main():
    test = IndeedContext.get_cursor("Software Engineer", "Santa Clara, CA")
    pass


if __name__ == '__main__':
    main()
