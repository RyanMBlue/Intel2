# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from selenium import webdriver
from bs4 import BeautifulSoup

# initiate
driver = webdriver.Firefox() # initiate a driver, in this case Firefox
driver.get("http://utopia-game.com/shared/login/") # go to the url

# log in
username_field = driver.find_element_by_name("username") # get the username field
password_field = driver.find_element_by_name("password") # get the password field
username_field.send_keys("ryanmblue") # enter in your username
password_field.send_keys("Blue5791") # enter in your password
password_field.submit() # submit it

driver.get("http://utopia-game.com/wol/game/kingdom_intel/5/8") # go to the url
# print HTML
html = driver.page_source
print "yay"

soup = BeautifulSoup(html, "html.parser")
#print soup
table = soup.find('table', attrs={'class':'tablesorter'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    print "ROW IS -"
    print row
    print "-"
    cells = row.findAll("td")
    if len(cells) == 9:
        pname = cells[1].find(text=True)
        pname = pname.strip('\n')
        runes = cells[3].find(text=True)
        runes = runes.strip('\n')
        gold = cells[4].find(text=True)
        gold = gold.strip('\n')
        food = cells[5].find(text=True)
        food = food.strip('\n')
        defense = cells[6].find(text=True)
        defense = defense.strip('\n')
        ops = cells[8].find(text=True)
        ops = ops.strip('\n')
        print pname + "-" + runes + "-" + gold + "-" + food + "-" + defense + "-" + ops