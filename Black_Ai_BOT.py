from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
class Black_ai:
    
    def __init__(self):
        options = Options()
        options.add_argument("headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.blackbox.ai/") 
        self.text=input("enter your question")
        self.driver.implicitly_wait(2)

    
    def send_data(self):
        
        self.Question_input = self.driver.find_element("xpath",'//*[@id="chat-input-box"]').send_keys(self.text)
        self.pushbutton=self.driver.find_element("xpath",'/html/body/div[2]/main/div/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[3]/button').click()
        print("............. Wait for Your Answer ..........................")

    def get_answer(self): 
        self.Answer = self.driver.find_element("xpath", "/html/body/div[2]/main/div[3]/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[3]").text
        print("Your Answer Is : ",self.Answer)
        
    
obj=Black_ai()
time.sleep(5)
obj.send_data()
time.sleep(7)
obj.get_answer()