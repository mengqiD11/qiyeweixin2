from selenium.webdriver.common.by import By

from page.basePage import BasePage

class AddMember(BasePage):
    def add_member(self):
        self.find(By.ID,"username").send_keys("zcp")
        self.find(By.ID,"memberAdd_acctid").send_keys("zcp")
        self.find(By.ID,"memberAdd_phone").send_keys("13266676767")
        self.find(By.CSS_SELECTOR,".js_btn_save").click()

    #获取添加人员的title列值
    def find_title(self):
        #获取所有添加人员信息
        elems = self.finds(By.CSS_SELECTOR,"#member_list td:nth-child(2)")
        arrs = []
        #循环取所有人员title列值，放到列表中
        for i in elems:
            arrs.append(i.get_attribute("title"))
        return arrs





