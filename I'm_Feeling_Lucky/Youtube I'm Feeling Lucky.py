from selenium import webdriver

query = input('Enter youtube search: ')

if query:
	PATH = "D:\Repository\Software EXE's\chromedriver_win32\chromedriver.exe"
	driver = webdriver.Chrome(PATH)
	driver.get('https://www.youtube.com/results?search_query=' + query)
	search = driver.find_element_by_id('thumbnail')
	search.click()



