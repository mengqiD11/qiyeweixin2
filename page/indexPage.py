from selenium.webdriver.common.by import By

from page.basePage import BasePage
from page.addMember import AddMember
from time import sleep

class IndexPage(BasePage):
    #重写baseurl
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    #跳转到添加用户页面
    def goto_add_member(self):
        #点击【通讯录】按钮
        self.find(By.ID,"menu_contacts").click()
        def wait(driver):
            ele_len = len(self.finds(By.ID, "username"))
            if ele_len < 1:
                self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member").click()
            # 如果username存在，就返回true
            return True
        self.wait_for(wait)
        # 对AddMember进行了实例化
        return AddMember(reuse=True)

