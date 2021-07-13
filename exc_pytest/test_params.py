import pytest


@pytest.mark.parametrize("key, result", [
    ['python', 200],
    ['java', 302]
])
def test_url(key, result):
    url = f"http://www.baidu.com/qw={key}"
    print(url, result)