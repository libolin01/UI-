import time

from Commonlib.Commonlib import Common

class Login(Common):
    def login(self,user,password):
        self.open_url('http://localhost:8080/login.html')
        self.input_data('id', 'username', user)
        self.input_data('id', 'password', password)
        self.click('id', 'btnSubmit')

    def gbts(self):
        self.driver.switch_to.alert.accept()


    def cwgl_xz(self,dw,sr,money,jbr,zh):
        self.click('text', '财务管理')
        self.click('text', '收入单')
        self.iframe('xpath', '/html/body/div[1]/div/div/div/div[2]/div[2]/iframe')
        self.click('css', '#addAccountHead > span:nth-child(1) > span:nth-child(1)')
        self.click('css', '#append > span:nth-child(1) > span:nth-child(1)')
        time.sleep(1)
        self.input_data(
            'xpath',
            '/html/body/div[2]/div[2]/div[1]/div/form/table/tbody/tr[2]/td/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div/table/tbody/tr/td/span/input[1]',
            sr)
        time.sleep(1)
        self.input_data('xpath', '//*[@id="accountHeadFM"]/table/tbody/tr[1]/td[2]/span/input[1]', dw)
        time.sleep(1)
        self.input_data('id', 'ChangeAmount', money)
        time.sleep(1)
        self.xlk('id', 'HandsPersonId', jbr)
        time.sleep(1)
        self.xlk('id', 'AccountId', zh)
        time.sleep(1)
        self.click('css', '#saveAccountHead > span:nth-child(1) > span:nth-child(1)')


    def cwgl_srd(self):
        self.click('text', '财务管理')
        self.click('text', '收入单')
        self.iframe('xpath','/html/body/div[1]/div/div/div/div[2]/div[2]/iframe')

    def riqi_cx(self):
        self.cwgl_srd()
        time.sleep(1)
        # 点击开始日期
        self.click('id', 'searchBeginTime')
        time.sleep(1)
        self.tciframe()
        # 进入日期框
        self.iframe('xpath', '/html/body/div[5]/iframe')
        time.sleep(1)
        # 点击日期
        self.click('css', '.WdayTable > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(5)')
        time.sleep(1)
        self.tciframe()
        # 进入大框
        self.iframe('xpath', '/html/body/div[1]/div/div/div/div[2]/div[2]/iframe')
        time.sleep(1)
        # 点击结尾日期
        self.click('id', 'searchEndTime')
        self.tciframe()
        # 进入日期框
        self.iframe('xpath', '/html/body/div[5]/iframe')
        time.sleep(1)
        # 点击日期
        self.click('xpath', '/html/body/div/div[3]/table/tbody/tr[5]/td[5]')
        self.tciframe()
        self.iframe('xpath', '/html/body/div[1]/div/div/div/div[2]/div[2]/iframe')
        time.sleep(1)
        self.click('css','.icon-search')








