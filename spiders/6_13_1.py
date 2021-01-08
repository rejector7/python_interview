import requests
import urllib
import re
from bs4 import BeautifulSoup


if __name__ == "__main__":
    # session = requests.session()
    response = requests.get(url="https://en.wikipedia.org/wiki/Machine_translation")
    # response.encoding = 'utf-8'
    # with open("mt.html", 'w', encoding='utf-8') as f:

    # with open("mt.html", 'wb') as f:
    #     f.write(response.content)

    soup = BeautifulSoup(response.text, features="lxml")
    tag2 = soup.find_all(name="p")
    list_p = []
    for tag in tag2:
        list_p.append(tag.get_text())

    str_p = ' '.join(list_p)
    word_dict = {}
    for word in str_p.split():
        word = word.strip(',()"";/\' ')
        word_count = word_dict.get(word, 0)
        word_dict[word] = word_count + 1

    sorted_word_dict_list = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

    with open("word_counts.txt", 'w') as f:
        for word_count in sorted_word_dict_list:
            line = word_count[0] + '\t' + str(word_count[1]) + "\n"
            f.write(line)

    # year = re.compile(r'\d{4}')
    # year_list = re.findall(year, response.text)
    # sorted_year_list = sorted(list(set(year_list)))
    # with open("year.txt", 'w') as f:
    #     for year in sorted_year_list:
    #         f.write(year + "\n")








