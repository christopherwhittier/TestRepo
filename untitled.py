import csv
from datetime import datetime

from dateutil import parser
from github import Github
import pytz


g = Github("de9c704043596ad37b52983a804354b92906d21f")
repo = g.get_user('christopherwhittier').get_repo('IntuitiveWebSolutions/BriteCore')

with open('github-prs.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['head user', 'base repo', 'PR updated at', 'last commit modified', 'title'])

    for pull in repo.get_pulls():
        last_date = datetime(1900, 1, 1, 0, 0, 0, 0, pytz.UTC)
        for commit in pull.get_commits():
            commit_date = parser.parse(commit.last_modified)
            if commit_date > last_date:
                last_date = commit_date
        writer.writerow([pull.head.user.login, pull.base.label, pull.updated_at, last_date, pull.title])