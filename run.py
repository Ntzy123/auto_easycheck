# run.py

import os, time, logging, argparse
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", type=str, help="轻松夜答URL")
parser.add_argument("-n", "--name", type=str, default="auto_easycheck", help="日志文件名称")
args = parser.parse_args()

log_dir = "log"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, f"{args.name}.log")
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s  [%(levelname)s]  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8", mode="w"),
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
        
        except Exception as e:
            logging.info(f"没有夜答题目，刷新网页: {e}")
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
    time.sleep(1)

    """# 返回
    back_button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'adm-nav-bar-left'))
    )
    back_button.click()
    logging.info("返回主页面")
    time.sleep(1200)"""



if __name__ == '__main__':
    # 输入夜答链接
    if args.url == None:
        print("https://rm.vankeservice.com/api/easycheck/web/index?wkwebview=true&rurl=/nightAnswer")
        easycheck_url = input("请输入轻松夜答URL：")
    else:
        easycheck_url = args.url

    # 初始化浏览器
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--no-sandbox")
    driver = webdriver.Edge(options=edge_options)
    
    try:
        # 自动点击
        while True:
            auto_click(driver)
            time.sleep(60)
    except KeyboardInterrupt:
        logging.info("用户手动终止")
    except Exception as e:
        logging.exception("运行异常")
    finally:
        time.sleep(2)
        driver.quit()
        logging.info("浏览器已关闭")