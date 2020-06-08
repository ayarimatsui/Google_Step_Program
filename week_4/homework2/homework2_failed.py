# Google STEP Program week4  homework2
# evaluate page rank of the pages linked from pages related to  Disney films
# 重すぎて計算できない

from collections import deque
import requests, bs4
import numpy as np

class Page:
    def __init__(self, name):
        self.name = name
        self.link_to = []
        self.link_from = []
        self.score = 100

    def add_link_to(self, page_id):
        self.link_to.append(page_id)

    def add_link_from(self, page_id):
        self.link_from.append(page_id)

    def get_linked_pages(self):
        return self.link_to


# return the top 10
def calculate_page_rank(wiki_page_list, initial_state):
    alpha = 0.85
    N = len(wiki_page_list)
    S = np.zeros((N, N))
    E = np.full((N, N), 1.0 / N)
    print('initialized')
    for ID, page in enumerate(wiki_page_list):
        linked_pages = page.get_linked_pages()
        M = len(linked_pages)
        for page_id in linked_pages:
            S[ID][page_id] = 1.0 / M
    
    G = alpha * S + (1 - alpha) * E
    print('G calculated')

    # とりあえず100回遷移
    page_score = initial_state.T
    for _ in range(100):
        page_score = np.dot(page_score, G)

    page_score = page_score.T
    page_rank = page_score.argsort()[::-1]

    top_10 = []
    for ID in page_rank[:10]:
        top_10.append(wiki_page_list[ID].name)

    return top_10



if __name__ == '__main__':

    # wikipedia category:ディズニーの映画作品　のurl
    url = 'https://ja.wikipedia.org/wiki/Category:%E3%83%87%E3%82%A3%E3%82%BA%E3%83%8B%E3%83%BC%E3%81%AE%E6%98%A0%E7%94%BB%E4%BD%9C%E5%93%81'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    contents = soup.select('.mw-category-group')
    # collect the page names of the pages about Disney movies
    disney_films = []
    for block in contents:
        block_text = block.getText()
        block_list = block_text.splitlines()
        for text in block_list:
            if text[0] != '►' and len(text) > 1:
                disney_films.append(text)
                
    wiki_page_list = []
    initial_state = []
    N = 0
    # read wikipedia_links/pages.txt and make a list of pages
    # also make the initial state
    with open('wikipedia_links/pages.txt') as pages_f:
        for line in pages_f:
            ID, name = line.strip().split()
            wiki_page_list.append(Page(name))
            N += 1
            if name in disney_films:
                initial_state.append(1)
            else:
                initial_state.append(0)

    # read links.txt and record follows
    # this takes a lot of time
    with open('wikipedia_links/links.txt') as links_f:
        for line in links_f:
            ID, link = map(int, line.strip().split())
            wiki_page_list[ID].add_link_to(link)
            wiki_page_list[link].add_link_from(ID)

    print('done')

    top_10 = calculate_page_rank(wiki_page_list, initial_state)

    for n, page_name in enumerate(top_10):
        print('{} : {}'.format(n + 1, page_name))