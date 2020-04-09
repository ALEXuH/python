from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# chrome 安装chromeDriver驱动并配置环境变量
# FireFox 只需要安装FireFox浏览器

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
#driver.close()
