"""auto-easycheck CLI 入口"""

import argparse
from .core import run


def main():
    parser = argparse.ArgumentParser(description="auto-easycheck - 轻松夜答自动答题工具")
    parser.add_argument("-u", "--url", type=str, help="轻松夜答URL")
    parser.add_argument(
        "-n", "--name", type=str, default="auto_easycheck", help="日志文件名称"
    )
    args = parser.parse_args()

    # 输入夜答链接
    if args.url is None:
        print(
            "https://rm.vankeservice.com/api/easycheck/web/index?wkwebview=true&rurl=/nightAnswer"
        )
        easycheck_url = input("请输入轻松夜答URL：")
    else:
        easycheck_url = args.url

    run(url=easycheck_url, log_name=args.name)


if __name__ == "__main__":
    main()
