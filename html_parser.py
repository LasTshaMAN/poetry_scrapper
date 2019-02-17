import bs4

# TODO
# Write unit-test for this functionality


class HTMLParser:
    def __init__(self, html):
        self.soup = bs4.BeautifulSoup(html, "lxml")

    def title(self):
        return self.soup.find('title').get_text()

    def div_contents(self):
        divs = self.soup.find_all('div')
        div_contents = [div.get_text() for div in divs if div.find_parent('div') is None]
        return ' '.join(div_contents)
