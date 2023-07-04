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
                    name.append(a.replace("\n",""))
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

# def qacashback():
#     qa_content = ""
#
#     url = 'https://rich01.com/best-only-cashback-credit-cards/'
#     r = requests.get(url, verify=False)
#
#     if r.status_code == requests.codes.ok:
#         soup = BeautifulSoup(r.text, 'html.parser')
#         table = soup.find('table', style="border-collapse: collapse; width: 100%; height: 970px;")
#         question = soup.find('div', id="sp-eap-accordion-section-18093").find('script',
#                                                                               type="application/ld+json").get_text()
#         questiontojson = json.loads(question, strict=False)
#
#         qa_info = questiontojson['mainEntity']
#         for qa in qa_info:
#             qa_name = qa['name']
#             qa_answer = qa['acceptedAnswer']['text']
#             qa_content = "{}\nA:{}\n".format(qa_name, qa_answer)
#          return qa_content
#     else:
#         print("Can't get the website")


def credit_cashback():
    global credit_name, fdback
    url_2 = 'https://rich01.com/e-commerce-credit-card/'
    r = requests.get(url_2, verify=False)

    name = []
    feedback = []
    list1, list2, list3 = [[] for x in range(3)]
    fdlist1, fdlist2, fdlist3 = [[] for x in range(3)]
    dom_dic = {}
    abor_dic = {}
    dig_dic = {}
    content1, content2, content3 = ["" for x in range(3)]



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
                    a = credit_name.strip('\n')
                    if a == "":
                        continue
                    else:
                        name.append(a.replace("\n", ""))
                for td in tds[1]:
                    fdback = td.text
                    a = fdback.strip('\n')
                    if a == "":
                        continue
                    else:
                        feedback.append(a.replace("\n", ""))
        # print(name, feedback)
        list1 = name[0:5]
        list2 = name[5:8]
        list3 = name[8:12]
        fdlist1 = feedback[0:10]
        fdlist2 = feedback[10:17]
        fdlist3 = feedback[17:]

        info1 = "\n".join(fdlist1[0:2])
        info2 = "\n".join(fdlist1[2:4])
        info3 = "".join(fdlist1[4:7])
        info4 = fdlist1[7]
        info5 = "\n".join(fdlist1[8:])
        dom_dic[list1[0]] = info1
        dom_dic[list1[1]] = info2
        dom_dic[list1[2]] = info3
        dom_dic[list1[3]] = info4
        dom_dic[list1[4]] = info5

        ab_info1 = "".join(fdlist2[0:2])
        ab_info2 = "".join(fdlist2[2:4])
        ab_info3 = "".join(fdlist2[4:])
        abor_dic[list2[0]] = ab_info1
        abor_dic[list2[1]] = ab_info2
        abor_dic[list2[2]] = ab_info3

        dg_info1 = "".join(fdlist3[0:2])
        dg_info2 = "".join(fdlist3[2:4])
        dg_info3 = "".join(fdlist3[4:6])
        dg_info4 = "".join(fdlist3[6:])
        dig_dic[list3[0]] = dg_info1
        dig_dic[list3[1]] = dg_info2
        dig_dic[list3[2]] = dg_info3
        dig_dic[list3[3]] = dg_info4

        for key, value in dom_dic.items():
            content1 += "\n\n{}\n回饋比例如下：\n{}\n".format(key, value)
        output1 = "國內網購聯名信用卡" + content1

        for key, value in abor_dic.items():
            content2 += "\n\n{}\n回饋比例如下：\n{}\n".format(key, value)
        output2 = "海外網購聯名信用卡" + content2

        for key, value in dig_dic.items():
            content3 += "\n\n{}\n回饋比例如下：\n{}\n".format(key, value)
        output3 = "數位通路聯名信用卡" + content3

        output = output1 + output2 + output3

        return output

    else:
        print("Can't get the website")

credit_cashback()