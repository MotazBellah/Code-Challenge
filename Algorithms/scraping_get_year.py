#Task: Write a function get_member_since which accepts a username from someone at Codewars
#and returns an string containing the month and year separated by a space that they joined CodeWars.
# https://www.codewars.com/kata/58ab2ed1acbab2eacc00010e/train/python
import urllib.request
from bs4 import BeautifulSoup
response = urllib.request.urlopen('https://www.codewars.com/users/MoatazBellahGH')
html = response.read()
soup = BeautifulSoup(html, 'html.parser').encode("utf-8")

print(soup)

def get_member_since(username):
    pass
