from bs4 import BeautifulSoup
import requests as req
import requests
import lxml

if __name__ == '__main__':
    # input1 = input("Введите запрос для булевой модели (используя 'or', 'end' или 'not'): \n")
    input1 = 'дорога'
    map_terms = {}
    url = 'http://www.serelex.org/find/ru-patternsim-ruwac-wiki/'
    for i in input1.split():
        new_url = url + i
        mas_words = []
        r = req.get(new_url)
        s = BeautifulSoup(r.text, 'lxml')

        str = (s.find("p").text)
        mas = str.split()

        for j in range(len(mas)):
            if mas[j] == '"word":':
                mas_words.append(mas[j + 1][1:-2])
        # print(mas_words)

        map_terms = {i: mas_words}

        # if (i != "not" or i != "end" or i != "or"):
        #     map_terms = {i: mas}
    print(map_terms)