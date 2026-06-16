"""轻松夜答自动答题核心逻辑"""

import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
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


def setup_logging(name: str = "auto_easycheck") -> str:
    """配置日志"""
    log_dir = "log"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, f"{name}.log")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  [%(levelname)s]  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8", mode="w"),
            logging.StreamHandler(),
        ],
    )
    return log_file


def create_driver() -> webdriver.Edge:
    """创建 headless Edge 浏览器实例"""
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--no-sandbox")
    return webdriver.Edge(options=edge_options)


def run(url: str, log_name: str = "auto_easycheck") -> None:
    """一键启动自动答题（推荐接口）

    直接传入 url 即可开始答题循环，日志默认以 auto_easycheck 命名。

    Args:
        url: 轻松夜答网页 URL
        log_name: 日志文件名称（不含路径），默认为 "auto_easycheck"
    """
    setup_logging(log_name)
    driver = create_driver()

    try:
        while True:
            auto_click(driver, url)
            time.sleep(60)
    except KeyboardInterrupt:
        logging.info("用户手动终止")
    except Exception:
        logging.exception("运行异常")
    finally:
        time.sleep(2)
        driver.quit()
        logging.info("浏览器已关闭")
