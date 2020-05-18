# Homework2の発展課題  自動化したもの
# i can haz wordz で高得点取れる文字列を返すプログラム

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pyperclip
import time
import collections

# ファイル'dictionary_words.txt'を読み込み、 全て大文字にしてリストdictionaryに格納
with open('dictionary_words.txt') as f:
    dictionary = [s.strip().upper() for s in f.readlines()]

def make_new_dic():
    # 辞書中の各単語ごとに、各文字がいくつずつあるのか数えて、新しい辞書を作る
    new_dictionary = []
    for word in dictionary:
        word_count = collections.Counter(word)
        if 'QU' in word:
            qu_count = word.count('QU')
            word_count['Q'] -= qu_count
            word_count['U'] -= qu_count
            word_count['QU'] += qu_count
            if word_count['Q'] == 0:
                word_count.pop('Q')
            if word_count['U'] == 0:
                word_count.pop('U')

        # 各単語の得点を計算しておく
        score = 0
        for i in range(len(word)):
            if word[i] in ['A', 'B', 'D', 'E', 'G', 'I', 'N', 'O', 'R', 'S', 'T', 'U']:
                score += 1
                # i - 1文字目が'Q', i文字目が'U'の時は'U'で足してしまった1をscoreから引く
                if i > 0:
                    if [word[i - 1], word[i]] == ['Q', 'U']:
                        score -= 1
            elif word[i] in ['C', 'F', 'H', 'L', 'M', 'P', 'V', 'W', 'Y']:
                score += 2
            else:
                score += 3
        score = (score + 1) ** 2
        new_dictionary.append([word, word_count, score])

    new_dictionary.sort(key=lambda x: x[2], reverse=True)

    return new_dictionary



def find_word(input_str, new_dictionary):
    # 各文字がいくつずつあるのか辞書にまとめる
    input_count = collections.Counter(input_str)

    best_word = None
    best_score = 0
    # 新しく作った辞書の単語について前から一つずつ調べていく
    for i in range(len(new_dictionary)):
        flag = True
        '''辞書中の単語が引数の文字列に使われている文字しか使っておらず、かつそれぞれの文字の登場回数が
        　　元々の文字列以下の時のみ、flag = True のままになるようにする
        '''
        for k, v in new_dictionary[i][1].items():
            if (k not in input_count.keys()) or (v > input_count[k]):
                flag = False
                break
        if flag:
            score = new_dictionary[i][2]
            best_score = score
            best_word = new_dictionary[i][0]
            break
            '''
            if score > best_score:
                best_score = score
                best_word = new_dictionary[i][0]'''

    return best_score, best_word


if __name__ == '__main__':
    new_dictionary = make_new_dic()

    # ブラウザのオプションを格納する変数をもらってきます。
    options = Options()

    # Headlessモードを有効にする（コメントアウトするとブラウザがz
    options.set_headless(True)

    webdriver = webdriver.Chrome(chrome_options=options)
    '''
    # 現在1位のスコアを獲得する
    webdriver.get("https://icanhazwordz.appspot.com/highscores")
    record_selector = "body > table.pure-table.pure-table-bordered > tbody > tr:nth-child(1) > td:nth-child(2)"
    record_list = webdriver.find_elements_by_css_selector(record_selector)
    for r in record_list:
        record = int(r.text)
    print(record)'''

    record = 2200

    time.sleep(3)

    # 自分のスコアを格納するための変数
    total_score = 0

    while total_score <= record:
        time.sleep(0.5)
        webdriver.get("https://icanhazwordz.appspot.com/")

        total_score = 0
        for n in range(10):
            input_list =[]
            selector_base = "body > table:nth-child(2) > tbody > tr > td:nth-child(1) > table > tbody > "
            soup = BeautifulSoup(webdriver.page_source, "html.parser")
            alphabets = soup.findAll('div',{'class':['letter p1','letter p2','letter p3']})
            for s in alphabets:
                input_list.append(s.text.upper())

            best_score, best_word = find_word(input_list, new_dictionary)
            total_score += best_score
            # あとで消す
            if best_score <= 100:
                break
            if best_word is None:
                print('PASS')
                pass_selector = "body > table:nth-child(2) > tbody > tr > td:nth-child(1) > form > input[type=submit]:nth-child(" + str(n + 7) + ")"
                webdriver.find_element_by_css_selector(pass_selector).click()
            else:
                print(best_word)
                print(best_score)
                pyperclip.copy(best_word)
                webdriver.find_element_by_xpath('//*[@id="MoveField"]').send_keys(pyperclip.paste())
                submit_selector = "body > table:nth-child(2) > tbody > tr > td:nth-child(1) > form > input[type=submit]:nth-child(" + str(n + 6) + ")"
                webdriver.find_element_by_css_selector(submit_selector).click()

            #time.sleep(0.1)

        if total_score > record:
            pyperclip.copy("Ayari Matsui")
            webdriver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/form/table/tbody/tr[1]/td[2]/input').send_keys(pyperclip.paste())
            webdriver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/form/table/tbody/tr[7]/td[2]/input').send_keys(pyperclip.paste())
            pyperclip.copy("https://gist.github.com/ayarimatsui/680338b328db2a9b3dda8dd3ebd4bbe4")
            webdriver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/form/table/tbody/tr[2]/td[2]/input').send_keys(pyperclip.paste())
            github_check = webdriver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/form/table/tbody/tr[3]/td[2]/input')
            if not github_check.is_selected():
                github_check.click()
            robot_btn = webdriver.find_element_by_xpath('//*[@id="AgentRobot"]')
            robot_btn.click()
            pyperclip.copy("ayanapo9846@gmail.com")
            webdriver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/form/table/tbody/tr[8]/td[2]/input').send_keys(pyperclip.paste())
            webdriver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/form/input[13]').click()
            print('recorded')
            break


    '''
    出力例:

    SECULARIZING
    289
    FRECKLED
    196
    JAYWALKING
    324
    RHAPSODIZED
    256
    CULTIVATING
    225
    BOMBARDIER
    144
    FLUKY
    121
    FOXHOUND
    169
    MIDDLEBROW
    196
    GRATEFULLY
    225

    '''
