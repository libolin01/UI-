import time
import unittest

from Business.Login import Login


class TestCase2(unittest.TestCase):
    def setUp(self):
        print('开始测试')

    def tearDown(self):
        print('测试结束')

    # 新增数据保存成功
    def test_001(self):
        log=Login('Firefox')
        log.login('test123','123456')
        # 传入新增的值
        log.cwgl_xz('测试1','收入3','6666','kxx','账户3')
        # 进行结果判断
        data=log.get_text('css','.messager-body > div:nth-child(2)')
        self.assertEqual('保存成功！',data)

    # 新增数据，金额为中文
    def test_002(self):
        log=Login('Firefox')
        log.login('test123','123456')
        # 传入新增的值
        log.cwgl_xz('客户1','收入3','啦啦啦','kxx','账户1')
        # 进行结果判断
        data=log.get_text('css','.messager-body > div:nth-child(2)')
        self.assertEqual('保存失败，金额只能为数字',data)

    # 删除一条数据
    def test_003(self):
        log = Login('Firefox')
        log.login('test123', '123456')
        log.cwgl_srd()
        time.sleep(1)
        log.click('css','#datagrid-row-r1-2-1 > td:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
        time.sleep(1)
        log.click('css','#deleteAccountHead > span:nth-child(1) > span:nth-child(1)')
        time.sleep(1)
        # 进行结果判断
        data=log.get_text('css','.messager-body > div:nth-child(2)')
        self.assertEqual('确定要删除选中的1条财务信息吗？', data)
        time.sleep(1)
        # 点击确定
        log.click('css','.messager-button > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)')

    # 根据单据编号查询
    def test_004(self):
        log = Login('Firefox')
        log.login('test123', '123456')
        log.cwgl_srd()
        time.sleep(1)
        log.input_data('id','searchBillNo','SR20220317232613')
        time.sleep(1)
        log.click('css','.icon-search')
        # 进行结果判断
        data=log.get_text('css','#datagrid-row-r1-2-0 > td:nth-child(5) > div:nth-child(1)')
        self.assertEqual('SR20220317232613',data)

    # 支持模糊查询
    def test_005(self):
        log = Login('Firefox')
        log.login('test123', '123456')
        log.cwgl_srd()
        time.sleep(1)
        log.input_data('id','searchBillNo','317232613')
        time.sleep(1)
        log.click('css','.icon-search')
        # 进行结果判断
        data=log.get_text('css','#datagrid-row-r1-2-0 > td:nth-child(5) > div:nth-child(1)')
        self.assertEqual('SR20220317232613',data)

    # 根据日期查询
    def test_006(self):
        log = Login('Firefox')
        log.login('test123', '123456')
        log.riqi_cx()
        data = log.get_text('css', '#datagrid-row-r1-2-0 > td:nth-child(7) > div:nth-child(1)')
        self.assertEqual('2022-03-24', data)

    # 修改数据测试
    def test_007(self):
        log = Login('Firefox')
        log.login('test123', '123456')
        log.cwgl_srd()
        log.click('xpath','/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[6]/td[2]/div/img[2]')
        time.sleep(1)
        log.click('css','.combo-arrow')
        log.click('id','_easyui_combobox_1')
        time.sleep(1)
        log.input_data('id','ChangeAmount','5533')
        time.sleep(1)
        log.xlk('id','AccountId','账户1')
        time.sleep(1)
        log.click('css','#saveAccountHead > span:nth-child(1) > span:nth-child(1)')






