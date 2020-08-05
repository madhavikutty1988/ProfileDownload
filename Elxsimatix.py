from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import Config

chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory":"D:\Tools\Jenkins\Downloads"})

driver=webdriver.Chrome(executable_path="D:\Tools\Python\Driver\Chrome\chromedriver.exe",chrome_options=chromeOptions)
driver.get("https://www.elxsimatix.net/")
driver.maximize_window()
driver.implicitly_wait(15)
#Login to Elxsimatix
username=driver.find_element_by_name("portlet_2_1{actionForm.username}")
username.send_keys(Config.loginidStr)
password=driver.find_element_by_name("portlet_2_1{actionForm.password}")
password.send_keys(Config.passwordStr)

driver.find_element_by_xpath("//*[@id='loginForm']/table[1]/tbody/tr[6]/td[2]/input").click()

#Parent window handle value
parent_window=driver.window_handles[0]
print(parent_window)
parent_window_title=driver.title
print(parent_window_title)
#Open Skill Center Page
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/span/div/table/tbody/tr/td[1]/div/table/tbody/tr[1]/td/div/div/div[2]/table/tbody/tr/td/ul/li[32]/a").click()
child_window=driver.window_handles[1]
print(child_window)

#Switch to Skill Center Page
driver.switch_to.window(child_window)
time.sleep(5)
#Child window handle value
child_window_title=driver.title
print(child_window_title)

driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[2]/a").click()
driver.find_element_by_xpath("//*[@id='profile']/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/ul/li[3]/div/button").click()
#Download Profile
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/ul/li[3]/div/ul/li[2]/a[2]").click()



