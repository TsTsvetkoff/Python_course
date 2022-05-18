import requests as re
from flask import Flask
from bs4 import BeautifulSoup
from http import cookiejar


class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False


app = Flask(__name__)


@app.route("/")
def valutno_info():
    s = re.Session()
    s.cookies.set_policy(BlockAll())
    bnb = s.get("https://www.bnb.bg/Statistics/StInterbankForexMarket/index.htm")
    assert not s.cookies
    result = ''

    html_soup = BeautifulSoup(bnb.content, 'html.parser')

    table = html_soup.find_all('div', {"class": "table_box table_scroll"})
    # table = html_soup.find_all('table')

    for row in table[0].children:
        print(row)
        result += str(row)

    return result


if __name__ == "__main__":
    app.run(port=80)
