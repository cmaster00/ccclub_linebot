import requests
import json
from bs4 import BeautifulSoup


def cashback():
    global card_name
    url = 'https://rich01.com/best-only-cashback-credit-cards/'
    r = requests.get(url, verify=False)

    name = []
    feedback = []
    temp_dic = {}
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
                a = card_fdback.strip('\n')
                if a == '':
                    continue
                else:
                    feedback.append(a)

        sec_info ="\n".join(feedback[1:4])
        third_info = "\n".join(feedback[4:7])
        fourth_info = "\n".join(feedback[8:10])
        temp_dic[name[0]] = feedback[0]
        temp_dic[name[1]] = sec_info
        temp_dic[name[2]] = third_info
        temp_dic[name[3]] = feedback[7]
        temp_dic[name[4]] = fourth_info

        for key, value in temp_dic.items():
            content += "{}\n回饋比例如下：\n{}\n\n".format(key, value)
        print(content)
        return content
    else:
        print("Can't get the website")

def qacashback():
    qa_content = ""

    url = 'https://rich01.com/best-only-cashback-credit-cards/'
    r = requests.get(url, verify=False)

    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table', style="border-collapse: collapse; width: 100%; height: 970px;")
        question = soup.find('div', id="sp-eap-accordion-section-18093").find('script',
                                                                              type="application/ld+json").get_text()
        questiontojson = json.loads(question, strict=False)

        qa_info = questiontojson['mainEntity']
        for qa in qa_info:
            qa_name = qa['name']
            qa_answer = qa['acceptedAnswer']['text']
            qa_content = "{}\nA:{}\n".format(qa_name, qa_answer)
         return qa_content
    else:
        print("Can't get the website")


def credit_cashback():
    global credit_name, fdback
    url_2 = 'https://rich01.com/e-commerce-credit-card/'
    r = requests.get(url_2, verify=False)

    name = []
    feedback = []

    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.find()
        tables = soup.find_all('table')
        for table in tables[4:7]:
            trs = table.find_all('tr')
            for tr in trs[2:len(trs) - 1]:
                tds = tr.find_all('td')
                for td in tds[0]:
                    credit_name = td.text
                    name.append(credit_name.strip('\n'))
                    # print(credit_name)
                for td in tds[1]:
                    fdback = td.text
                    feedback.append(fdback.strip('\n'))
                    # print(fdback)
        print(name, feedback)
    else:
        print("Can't get the website")

cashback()