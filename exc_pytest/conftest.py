import pytest


def pytest_collection_modifyitems(session, config, items):
    print("这是收集所有测试用例的方法")
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
