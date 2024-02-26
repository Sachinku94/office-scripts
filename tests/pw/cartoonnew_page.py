from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver=webdriver.Chrome
driver.get("https://www.physiciansweekly.com/category/cartoons/")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[@class='align-right secondary slidedown-button']").click()
time.sleep(3)
sie=driver.find_elements(By.XPATH,"//div [@class='post-media-container']")
for s in sie:
    ss=s.size
    
    print(ss)
    assert ss == {'height': 282, 'width': 397}
d=[]
a =700
b = "60px"
c = "Elza"
ad =[a,b,c]
cs_s=driver.find_element(By.XPATH,"//h1[@class='is_archive']")
c=['font-weight','font-size','font-family']

for i in c:
    print(cs_s.value_of_css_property(i))
    d.append(cs_s.value_of_css_property(i))
    print(d)
    
if d==['700','60px','Elza']:
        print("pass")
        
        




#c=('font-weight','font-size','font-family')
'''for cs in cs_s:
    c=('font-weight','font-size','font-family')
    print(cs.value_of_css_property(c))
    time.sleep(3)'''
