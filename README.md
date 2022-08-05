# Data_Collection_CoinMarket
Data scrape of the website https://coinmarketcap.com/


###Building a Scraper 
- The package Selenium was used to open and control a webpage in Microsoft Edge to coinmarket using the code 
```python
def __init__ (self, URL: str = "https://coinmarketcap.com/"):
        self.driver = webdriver.Edge()
        self.driver.get(URL)
```
- Selenium finds specific features via xpaths, which can be found using ctrl + shift + c whilst on the webpage and hovering over elements.
- A unique xpath is preferred, or making a list of all elements found by xpath and choosing which to use.
- A common way to find unique xpaths is to obtain a parent xpath of element and set a variable equal to it called a container.
- In this container you can then refine the xpath search.
- Several methods were designed on this page to navigate it included accept cookies, change currency.
- Accept cookies waited for the element to appear on page then close the pop-up
```python
WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cmc-cookie-policy-banner"]')))
            self.accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@class="cmc-cookie-policy-banner__close"]')
            self.accept_cookies_button.click()
```
- Change currency finds and clicks option, waits for elements to load before clicking the british pound option.
```python
settings_button = self.driver.find_element(by=By.XPATH, value='//*[@class="sc-1pyr0bh-0 bSnrp sc-1g16avq-0 kBKzKs"]')
            settings_button.click()
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '//*[@class="vxp8h8-0 VMCHA"]')))
            select_currency_button = self.driver.find_element(by=By.XPATH, value='//button[@data-qa-id="button-global-currency-picker"]')
            select_currency_button.click()
            currency = self.driver.find_element(by=By.XPATH, value='//*[@class="ig8pxp-0 jaunlC"]')
            time.sleep(2)
            currency.click()
```
- Search bar method functions similarly to the above, but takes a string as parameter to input text.
- Scroll bottom finds the maximum height of the page then uses window.scrollTo() to descend by 2000
```python
max_page_height = self.driver.execute_script("return document.documentElement.scrollHeight")
        scroll_down_y_axis = 2000

        while scroll_down_y_axis < max_page_height:
            self.driver.execute_script(f"window.scrollTo(0, {scroll_down_y_axis});")
            self.get_links()
            time.sleep(3)
            scroll_down_y_axis += 2000
```            

- In the above method there was a get_links() called. This method obtains the links for each coin via their "a" tag in the main container for the table on the homepage.
- It then saves the href's from the tags to a list.
```python 
self.coin_container = self.driver.find_elements(by=By.XPATH, value='//div[@class="h7vnx2-1 bFzXgL"]//div[@class="sc-16r8icm-0 escjiH"]')
        for crypto_coin in self.coin_container:
            a_tag = crypto_coin.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            link_list.append(link)
```
- As the website had dynamic pages, the page must scroll down to obtain the all the links.
    
    
 
