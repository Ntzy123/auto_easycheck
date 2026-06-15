# auto-easycheck

轻松夜答自动答题工具，基于 Selenium 自动完成夜答任务。

## 快速开始

```bash
# 创建虚拟环境并安装依赖
make setup

# 或者使用 pip
pip install -e .
```

## 使用方法

```bash
# 通过 CLI 运行
auto-easycheck

# 指定 URL
auto-easycheck -u "https://..."

# 指定日志名称
auto-easycheck -n "my_log"

# 或者通过 Makefile
make run
```

## 构建

```bash
make build
```

## 项目结构

```
auto-easycheck/
├── src/
│   └── auto_easycheck/
│       ├── __init__.py
│       ├── __main__.py     # CLI 入口
│       └── core.py         # 核心答题逻辑
├── tests/
│   ├── __init__.py
│   └── test_core.py
├── pyproject.toml
├── Makefile
├── requirements.txt
└── README.md
```
