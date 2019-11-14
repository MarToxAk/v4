from ..models import CasadePedraCotacao
from selenium import webdriver

def cadastra_cotação(cotação):
    CasadePedraCotacao.objects.create(author=cotação.author, name=cotação.name, tel=cotação.tel, checkin=cotação.checkin,
                                     checkout=cotação.checkout, person_num=cotação.person_num, kidquestion=cotação.kidquestion,
                                     kidyears=cotação.kidyears, discount=cotação.discount, dialy_of_price=cotação.dialy_of_price,
                                     portion=cotação.portion)

def webdrive(checkin, checkout, person_num):
    link = f'https://reservations.omnibees.com/default.aspx?q=3661&diff=false&CheckIn={checkin}&CheckOut={checkout}&Code=&group_code=&loyality_card=&NRooms=1&ad={person_num}'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(link)
    nav = browser.find_element_by_xpath("//div[@id='show_3']/table/tbody/tr/td/div/div[3]/div/h6")
    preco = str(nav.text)
    valor = preco[3:]
    return float(valor.replace(',', '.'))

