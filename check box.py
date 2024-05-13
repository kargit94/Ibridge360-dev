import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

edge_driver_path='E:\\Ibridge automation\\edgedriver_win64\\msedgedriver.exe'
edge_service = Service(edge_driver_path)
class ibridge:
    def test_ibridge(self):

        driver = webdriver.Edge(service=edge_service)
        driver.get("http://dev.ibridge360.com")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.XPATH,'//header/div[1]/div[1]/div[6]/h5[1]/a[1]').click()
        # Login
        username_field = driver.find_element(By.NAME,'email')
        webdriver.ActionChains(driver).send_keys_to_element(username_field,'ibridge@gmail.com').perform()
        password_field = driver.find_element(By.NAME,'password')
        webdriver.ActionChains(driver).send_keys_to_element(password_field,'Ibridge@2021').perform()
        driver.implicitly_wait(10)
        # Clicking on the 'Login' button
        driver.find_element(By.CLASS_NAME,'MuiButton-label').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//div[@class="MuiListItemText-root"]//child::span[text()="Coach List"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div/div/div/div[1]/div/div[1]/button').click()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,450)", "")
        time.sleep(2)
        Preferred_days = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/form/div/div[12]').click()
        time.sleep(3)
        P_d=driver.find_elements(By.XPATH,'//span[@class="MuiTypography-root MuiListItemText-primary MuiTypography-body1 MuiTypography-displayBlock" and contains(text(),"day")]')
        time.sleep(2)
        print(len(P_d))

        # for i in range(len(P_d)):
        #     P_d[i].click()
        #     time.sleep(2)
        # for days in P_d:
        #     days.click()
        #     time.sleep(2)
        for days in P_d:
            weekname=days.text
            if weekname=='Monday' or weekname=='Wednesday':
                time.sleep(2)
                days.click()
                time.sleep(2)

        Preferred_timing=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/form/div/div[13]/div/div/div').click()
        time.sleep(2)


        P_t=driver.find_elements(By.XPATH,'//span[@class="MuiTypography-root MuiListItemText-primary MuiTypography-body1 MuiTypography-displayBlock" and contains(text(),"PM") or contains(text(),"AM")]')
        print(len(P_t))
        time.sleep(2)

iobj=ibridge()
iobj.test_ibridge()