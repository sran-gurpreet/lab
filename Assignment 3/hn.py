import csv
import time
import random

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.window import WindowTypes

HN_WEBSITE = "https://news.ycombinator.com"

def get_top_comments(driver):
    #click list button on the bottom
    btn_list_sel = "a[href='lists']"
    btn_list = driver.find_element(by=By.CSS_SELECTOR, value=btn_list_sel)
    btn_list.click()

    #click bestcomments button
    btn_bc_sel = "a[href='bestcomments']"
    btn_bc = driver.find_element(by=By.CSS_SELECTOR, value=btn_bc_sel)
    btn_bc.click()

    #get the best comments
    comm_sel = ".commtext"
    comm_elems = driver.find_elements(by=By.CSS_SELECTOR, value=comm_sel)
    comments = []
    for comm in comm_elems:
       comment = comm.get_attribute("innerText")
       comments.append(comment.strip())

    return comments

def get_top_posts(driver):
    print("Trying to get top posts now.")

    #popup shows
    post_sel = ".titleline"
    posts = []
    post_elems = driver.find_elements(by=By.CSS_SELECTOR, value=post_sel)
    for post in post_elems:
       title = post.get_attribute("innerText")
       posts.append(title.strip())

    #to type text
    #elem.send_keys(details[0])
    return posts
    

def main():
    try:
        service = Service(executable_path="chromedriver.exe")
        opts = Options()

        #hide browser window
        #opts.add_argument("--headless")

        #change user agent
        user_agent = "Opera/9.80"
        opts.add_argument("user-agent=" + user_agent)

        #start scrapping
        driver = webdriver.Chrome(service=service, options=opts)
        print("Opening browser.")
        driver.get(HN_WEBSITE)

        
        post_titles =  get_top_posts(driver)
        print("--------------------------------")
        print("Hacker News Top Posts Now")
        for title in post_titles:
           print(title)
           
        print("-------------------------------")
        print("Hacker News Top Comment")
        comments = get_top_comments(driver)
        if len(comments) > 0:
            print(comments[0])
            
    except Exception as e:  
        print("Selenium Chrome driver must match with Chrome installed.")
   
        

if __name__ == "__main__":
    main()
        


        
