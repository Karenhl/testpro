import requests


class TestCase:
    """
    测试用例接口模块的测试代码
    """
    def setup_class(self):
        self.base_url = "http://127.0.0.1:5000/testcase"

    def test_get(self):
        """
        测试获取用例数据
        :return:
        """
        r = requests.get(self.base_url)
        print(r.json())
        assert r.status_code == 200

    def test_post(self):
        """
        测试新增用例
        :return:
        """
        r = requests.post(self.base_url)
        print(r.json())
        assert r.status_code == 200

    def test_put(self):
        """
        测试修改用例
        :return:
        """
        r = requests.put(self.base_url)
        print(r.json())

        assert r.status_code == 200

    def test_delete(self):
        """
        测试删除用例
        :return:
        """
        r = requests.delete(self.base_url)
        print(r.json())

        assert r.status_code == 200
