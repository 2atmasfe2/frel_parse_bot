import requests
from bs4 import BeautifulSoup
import gmail_analysis
#  import lxml
#  from selenium.webdriver.common.keys import Keys
from selenium import webdriver
#  import webbrowser

# внесение пользовательских данных
datas = {
    'email': 'def',
    'password': 'def'
}
login = input('Enter email: ')
passwd = input('Password: ')
datas['email'] = login
datas['password'] = passwd
url = '###'  #  URL для внесения данных пользователя
s = requests.Session()
loging = s.post(url, data=datas)
f = open('result.txt', 'w+')
f.write(loging.text)
f.close()


def get_html(url):
    result = requests.get(url)
    return result.text

#  получение ссылки на новый заказ
def get_data(html):
    while True:
        triggers = gmail_analysis.analize()
        if triggers:
            for trigger in triggers:
                soup = BeautifulSoup(html, 'lxml')
                article = soup.find('article')
                item = article.find('a').get('href')
                link1 = '###' + item  #  основной домен
                path = "путь до драйвера"
                driver = webdriver.Chrome(executable_path=path)
                driver.get(get_data.link1)
                field = driver.find_element_by_id('task_comment_body')
                field.send_keys('заготовленый текст')
                driver.find_element_by_partial_link_text('Откликнуться').click()


def main():
    html = get_html('###')  #  URL после ввода данных пользователя
    get_data(html)


if __name__ == '__main__':
    main()