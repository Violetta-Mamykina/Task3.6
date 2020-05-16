import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_exist(browser):
    browser.get(link)
    button = len(browser.find_element_by_css_selector(".btn-add-to-basket").text)
    assert button > 0, "Button not exist"