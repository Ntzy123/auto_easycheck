"""轻松夜答自动答题核心逻辑"""

import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def auto_click(driver, url: str):
    """打开夜答网页并自动答题"""
    # 打开网页
    driver.get(url)
    logging.info("打开夜答网页")

    # 等待页面加载
    is_load = False
    while not is_load:
        try:
            check_box = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@class="bg-white rounded mx-3 mt-3 p-5 shadow"][1]')
                )
            )
            check_box.click()
            is_load = True
            logging.info("打开夜答题目")

        except Exception as e:
            logging.info(f"没有夜答题目，刷新网页: {e}")
            driver.refresh()

    # 选择第一个选项
    select_box = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@class="adm-space-item"][1]//*[@class="adm-radio-icon"]')
        )
    )
    select_box.click()
    logging.info("选择第一个选项")

    # 提交
    submit_button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "adm-nav-bar-right"))
    )
    submit_button.click()
    logging.info("提交答案")
    time.sleep(1)
