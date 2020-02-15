from selenium import webdriver

# url_path = "http://localhost:3000/"
url_path = "http://10.8.33.147:3000/"

driver = webdriver.Chrome('/Users/npurushothama/naren/nodejs/node_automation/chromedriver')
# driver.maximize_window()
# driver.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")
driver.get(url_path)
driver.find_element_by_id("uname").send_keys("test")
driver.find_element_by_id("password").send_keys("12345")
driver.find_element_by_id("loginbtn").click()

checksuccess = driver.find_element_by_tag_name("H2").text
print("CHK : ", checksuccess)
# assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in driver.title
assert "SUCCESS"== checksuccess

driver.quit()