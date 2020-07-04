from urllib.request import urlopen
import urllib.parse

def profanity_checker(text):
    encoded_text = urllib.parse.quote(text, 'utf-8')
    with urlopen("http://www.wdylike.appspot.com/?q="+encoded_text) as url:
        output = url.read().decode("utf-8")
        if 'true' in output:
            return True
        else:
            return False


profanity_checker("shit")
profanity_checker("shot")
