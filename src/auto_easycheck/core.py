"""轻松夜答自动答题核心逻辑"""

import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

_loggers: dict[str, logging.Logger] = {}


def _get_logger(name: str) -> logging.Logger:
    """获取或创建一个按名称隔离的 logger，同时输出到文件和控制台"""
    if name in _loggers:
        return _loggers[name]

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # 避免重复添加 handler
    if not logger.handlers:
        log_dir = "log"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # 文件 handler
        fh = logging.FileHandler(
            os.path.join(log_dir, f"{name}.log"), encoding="utf-8", mode="a"
        )
        fh.setLevel(logging.INFO)

        # 终端 handler
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s  [%(levelname)s]  %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(sh)

    _loggers[name] = logger
    return logger


def auto_click(driver, url: str, log_name: str = "auto_easycheck"):
    """打开夜答网页并自动答题

    Args:
        driver: Edge WebDriver 实例
        url: 轻松夜答网页 URL
        log_name: 日志名称，每个名称对应独立日志文件 ./log/<log_name>.log
    """
    logger = _get_logger(log_name)

    # 打开网页
    driver.get(url)
    logger.info("打开夜答网页")

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
            logger.info("打开夜答题目")

        except Exception as e:
            logger.info("没有夜答题目，刷新网页")
            driver.refresh()

    # 选择第一个选项
    select_box = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@class="adm-space-item"][1]//*[@class="adm-radio-icon"]')
        )
    )
    select_box.click()
    logger.info("选择第一个选项")

    # 提交
    submit_button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "adm-nav-bar-right"))
    )
    submit_button.click()
    logger.info("提交答案")
    time.sleep(1)


def create_driver() -> webdriver.Edge:
    """创建 headless Edge 浏览器实例"""
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--no-sandbox")
    return webdriver.Edge(options=edge_options)


def run(url: str, log_name: str = "auto_easycheck") -> None:
    """一键启动自动答题（推荐接口）

    Args:
        url: 轻松夜答网页 URL
        log_name: 日志名称，对应日志文件 ./log/<log_name>.log
    """
    logger = _get_logger(log_name)
    driver = create_driver()

    try:
        while True:
            auto_click(driver, url, log_name)
            time.sleep(60)
    except KeyboardInterrupt:
        logger.info("用户手动终止")
    except Exception:
        logger.exception("运行异常")
    finally:
        time.sleep(2)
        driver.quit()
        logger.info("浏览器已关闭")
