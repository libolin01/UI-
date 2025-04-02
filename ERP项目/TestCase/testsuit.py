import  unittest

from Commonlib.HTMLTestRunner import HTMLTestRunner
from TestCase.testcase登录 import TestCase
from TestCase.testcase财务管理 import TestCase2


class Test(unittest.TestCase):

    def test_suit(self):
        # 创建测试套件
        mysuit=unittest.TestSuite()

        # 向测试套件添加测试用例
        case_list=['test_001','test_002','test_003','test_004','test_005','test_006','test_007']
        for case in case_list:
            mysuit.addTest(TestCase2(case))

        # 生成html的测试报告
        with open('../report1.html','wb')as f:
            HTMLTestRunner(
               # 指定写入文件
                stream=f,
               # 设定测试报告的标题
                title='企业ERP系统管理测试报告',
               # 设定测试报告的描述
                description='ERP财务管理模块验证',
                verbosity=2
            ).run(mysuit)