"""auto_easycheck 核心模块测试"""


def test_import():
    """验证模块可正常导入"""
    from auto_easycheck import core  # noqa: F811

    assert hasattr(core, "auto_click")
