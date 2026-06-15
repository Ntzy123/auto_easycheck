"""auto-easycheck CLI 入口"""

import os
import time
import logging
import argparse
from selenium import webdriver
from selenium.webdriver.edge.options import Options

from .core import auto_click


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


def main():
    parser = argparse.ArgumentParser(description="auto-easycheck - 轻松夜答自动答题工具")
    parser.add_argument("-u", "--url", type=str, help="轻松夜答URL")
    parser.add_argument(
        "-n", "--name", type=str, default="auto_easycheck", help="日志文件名称"
    )
    args = parser.parse_args()

    setup_logging(args.name)

    # 输入夜答链接
    if args.url is None:
        print(
            "https://rm.vankeservice.com/api/easycheck/web/index?wkwebview=true&rurl=/nightAnswer"
        )
        easycheck_url = input("请输入轻松夜答URL：")
    else:
        easycheck_url = args.url

    driver = create_driver()

    try:
        while True:
            auto_click(driver, easycheck_url)
            time.sleep(60)
    except KeyboardInterrupt:
        logging.info("用户手动终止")
    except Exception as e:
        logging.exception("运行异常")
    finally:
        time.sleep(2)
        driver.quit()
        logging.info("浏览器已关闭")


if __name__ == "__main__":
    main()
