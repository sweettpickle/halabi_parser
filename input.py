from bs4 import BeautifulSoup
import requests as req
import requests

FIND_ATTRIBUTES = ['property', 'name']


class MetaParser(object):
    def __init__(self, parsed_url, output_schema):
        self._url = parsed_url
        self._result = BeautifulSoup(requests.get(parsed_url).text, 'lxml')
        self._schema = output_schema

    # noinspection PyShadowingBuiltins
    @property
    def result(self):
        data = {}

        for input, output in self._schema.items():

            results = []

            for attribute in FIND_ATTRIBUTES:
                results = self._result.findAll(attrs={attribute: input})
                if len(results) != 0:
                    break

            if len(results) == 0:
                raise RuntimeError('Page {url} has not meta tag with {input} property'.format(
                    url=self._url, input=input))

            value = results[0]['content']

            if value:
                data[output] = value.strip()

        return data

def main():
    schema = {
        'og:title': 'title',
        'og:description': 'description',
        'og:image': 'image',
        'relap-image': 'url'
    }

    urls = ['https://news.mail.ru/incident/25361692/',
            'http://www.novayagazeta.ru/society/72528.html']
    data = []

    for url in urls:
        result = MetaParser(url, schema).result
        data.append(result)
    print(data)


if __name__ == '__main__':
    main()


# resp = req.get("https://www.prlib.ru/dublincore")
#
# soup = BeautifulSoup(resp.text, 'lxml')
#
# a = soup.find_all(attrs={"name": "description"})
#
# print(a)
