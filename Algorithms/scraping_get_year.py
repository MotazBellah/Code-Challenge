#Task: Write a function get_member_since which accepts a username from someone at Codewars
#and returns an string containing the month and year separated by a space that they joined CodeWars.
# https://www.codewars.com/kata/58ab2ed1acbab2eacc00010e/train/python
import re
import urllib.request
from bs4 import BeautifulSoup


def get_member_since(username):
    try:
        response = urllib.request.urlopen('https://www.codewars.com/users/{}'.format(username))
    except Exception as e:
        return e

    html = response.read()
    soup = BeautifulSoup(html, 'html.parser').encode("utf-8")

    member_pattern = re.compile(r'Member Since:</b>(\S+\s*\d+)')
    date_search = member_pattern.search(str(soup))
    if date_search:
        return date_search.group()[17:]
    else:
        return 'Please check the username'

print(get_member_since('MoatazBellahGH'))
