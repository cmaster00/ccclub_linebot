import requests
import json
from bs4 import BeautifulSoup


def cashback():
    global card_name
    url = 'https://rich01.com/best-only-cashback-credit-cards/'
    r = requests.get(url, verify=False)

    name = []
    feedback = []
    content = ""

    if r.status_code == requests.codes.ok:

        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table', style="border-collapse: collapse; width: 100%; height: 970px;")

        trs = table.find_all('tr')
        for tr in trs[1:6]:
            tds = tr.find_all('td')
            for td in tds[0]:
                card_name = td.text
                a = card_name.strip('\n')
                if a == '':
                    continue
                else:
                    name.append(a)
            for td in tds[1]:
                card_fdback = td.text
                feedback.append(card_fdback.strip('\n'))
        print(feedback)
        for i in range(4):
            if feedback[i] == '':
                continue
            else:
                content += "{}\n{}\n".format(name[i], feedback[i])
        print(content)


        # question = soup.find('div', id="sp-eap-accordion-section-18093").find('script',
        #                                                                       type="application/ld+json").get_text()
        # questiontojson = json.loads(question, strict=False)
        # qa_info = questiontojson['mainEntity']
        # for qa in qa_info:
        #     qa_name = qa['name']
        #     qa_answer = qa['acceptedAnswer']['text']

    else:
        print("Can't get the website")


def credit_cashback():
    url_2 = 'https://rich01.com/e-commerce-credit-card/'
    r = requests.get(url_2, verify=False)

    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.find()
        tables = soup.find_all('table')
        for table in tables[4:7]:
            trs = table.find_all('tr')
            for tr in trs[2:len(trs) - 1]:
                tds = tr.find_all('td')
                for td in tds[0]:
                    print(td.text)
                for td in tds[1]:
                    print(td.text)
    else:
        print("Can't get the website")

cashback()