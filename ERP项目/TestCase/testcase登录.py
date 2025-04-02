
import unittest

from Business.Login import Login


class TestCase(unittest.TestCase):
    def setUp(self):
        print('开始测试')

    def tearDown(self):
        print('测试结束')

    # 登录成功的情况
    # 输入正确账号和密码登录成功
    def test_001(self):
        log=Login('Firefox')
        log.login('test123','123456')
    # 获取一个本文信息
        data=log.get_text('css','div.pull-left:nth-child(2) > p:nth-child(1)')
        self.assertEqual('测试用户',data)

    # 输入错误账号和密码登录失败
    def test_002(self):
        log = Login('Firefox')
        log.login('text','123457')
        data=log.tswb()
        log.gbts()
        self.assertEqual('用户名不存在',data)

    # 输入错误账号和正确密码登录失败
    def test_003(self):
        log = Login('Firefox')
        log.login('text','123456')
        data = log.tswb()
        log.gbts()
        self.assertEqual('用户名不存在', data)

    # 输入正确账号、密码为空登录失败
    def test_004(self):
        log = Login('Firefox')
        log.login('test123','')
        data = log.get_text('xpath','/html/body/div/div/div[2]/div[1]/span')
        self.assertEqual('请输入密码', data)

        # 输入账号为空，正确密码登录失败
    def test_005(self):
        log = Login('Firefox')
        log.login('','123456')
        data = log.get_text('xpath','/html/body/div/div/div[2]/div[1]/span')
        self.assertEqual('请输入用户名', data)

        # 输入正确的账号，错误的密码登录失败
    def test_006(self):
        log = Login('Firefox')
        log.login('test123','123455')
        data = log.tswb()
        log.gbts()
        self.assertEqual('用户密码错误',data)

        # 输入账号为空，密码为空登录失败
    def test_007(self):
        log = Login('Firefox')
        log.login('','')
        data = log.get_text('xpath','//*[@id="username"]')
        self.assertEqual('请输入用户名', data)

if __name__ == '__main__':
    unittest.main()