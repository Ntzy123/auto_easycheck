# run.py

import os, time, logging
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s  [%(levelname)s]  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("auto_easycheck.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# easycheck_url = "https://rm.vankeservice.com/easycheck/#/nightAnswer?accessToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJBQ0NFU1NfVE9LRU4iLCJjbGllbnRJZCI6ImU4YTJmOTYzOGQ2ZTRiNDY4MjdiMmY2YzM0MjRlMDc1Iiwic2NvcGUiOiJyLXN0YWZmIiwidG9rZW4iOiIxNzAyMDcxIiwiaWF0IjoxNzQ3NjcwNDU2LCJleHAiOjE3NDgyNzUyNTZ9.2iBo1XEIqyuPdLjCrDeK2KqjZk-mT-5mQpsWDsT4ISQ"


def auto_click(driver):
    # 打开网页
    driver.get(easycheck_url)
    logging.info("打开夜答网页")

    # 等待页面加载
    is_load = False
    while not is_load:
        try:
            check_box = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '//*[@class="bg-white rounded mx-3 mt-3 p-5 shadow"][1]'))
            )
            check_box.click()
            is_load = True
            logging.info("打开夜答题目")
        
        except:
            logging.info("没有夜答题目，刷新网页")
            driver.refresh()
    
    # 选择第一个选项
    select_box = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@class="adm-space-item"][1]//*[@class="adm-radio-icon"]'))
    )
    select_box.click()
    logging.info("选择第一个选项")

    # 提交
    submit_button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'adm-nav-bar-right'))
    )
    submit_button.click()
    logging.info("提交答案")

    # 返回
    back_button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'adm-nav-bar-left'))
    )
    back_button.click()
    logging.info("返回主页面")



if __name__ == '__main__':
    # 输入夜答链接
    print("https://rm.vankeservice.com/api/easycheck/web/index?wkwebview=true&rurl=/nightAnswer")
    easycheck_url = str(input("请输入轻松夜答URL："))
    
    # 初始化浏览器
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--no-sandbox")
    driver = webdriver.Edge(options=edge_options)
    os.system("clear")
    # 自动点击
    while driver:
        auto_click(driver)
        time.sleep(60)

    time.sleep(2)
    driver.quit()