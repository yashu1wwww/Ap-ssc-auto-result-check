from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://bse.ap.gov.in/RESULTSTWT/")

reg= driver.find_element_by_name("txtHallTicketNo")
reg.send_keys("2223107605") #change which reg yoyu want

see= driver.find_element_by_name("btnSubmit").click()

