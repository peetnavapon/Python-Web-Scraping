#temperature.py


import songline
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
token = 'your token'
def Temperature(pvid):
    try:
        # 1 - URL
        url = 'https://www.tmd.go.th/province.php?id=' + str(pvid)
        #pvid = province id from website

        # 2 - Request URL
        webopen = req(url)
        page_html = webopen.read()
        webopen.close()

        # 3 - Convert page_html to Soup Object
        data = soup(page_html,'html.parser')

        # 4 - Find Element ( td:'strokeme' )
        temp = data.findAll('td',{'class':'strokeme'})
        province = data.findAll('span',{'class':'title'})
        pv = province[0].text.replace(' ','')

        result = temp[0].text

        print('จังหวัด:{} อุณหภูมิ:{}'.format(pv,result))
        text = 'จังหวัด:{} อุณหภูมิ:{}'.format(pv,result)
        #print(f'จังหวัด:{pv} อุณหภูมิ:{result}')
        return text
    except:
        print('No Result')
        return 'No Result'
messenger = songline.Sendline(token)

myprovince = Temperature(1) #จังหวัดที่อยากรู้
messenger.sendtext(myprovince)
    
'''
#For Multiple Result
for i in range(1,101):
    print(i)
    Temperature(i)
    print('----')
'''
