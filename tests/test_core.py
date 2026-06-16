"""auto_easycheck 核心模块测试"""


def test_import():
    """验证模块可正常导入"""
    from auto_easycheck import core  # noqa: F811

    assert hasattr(core, "auto_click")
    assert hasattr(core, "create_driver")
    assert hasattr(core, "setup_logging")
    assert hasattr(core, "run")


def test_package_api():
    """验证 __init__.py 导出了全部公共 API"""
    from auto_easycheck import auto_click, create_driver, run, setup_logging  # noqa: F811
    from auto_easycheck import __all__

    assert set(__all__) == {"auto_click", "create_driver", "run", "setup_logging"}
