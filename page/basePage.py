from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = ""
    _base_url = ""
    #初始化driver
    def __init__(self,reuse=False):
        #如果等于true，则代表复用现有的浏览器
        if reuse == True:
            chrom_opt = webdriver.ChromeOptions()
            chrom_opt.debugger_address="127.0.0.1:9444"
            self._driver = webdriver.Chrome(options=chrom_opt)
        #否则重新创建浏览器
        else:
            self._driver = webdriver.Chrome()
        #如果子类重写了baseurl，则这里就打开新的地址
        if self._base_url != "":
            self._driver.get(self._base_url)
        self._driver.implicitly_wait(3)
        self._driver.maximize_window()
    #查找单个元素，返回元素对象
    def find(self,By,loc):
        return self._driver.find_element(By,loc)
    #查找多个元素，返回list列表，具有长度
    def finds(self,By,loc):
        return self._driver.find_elements(By,loc)


    #显式等待
    def wait_for(self, fun):
        # 如果fun返回了true，那么就退出显式等待
        WebDriverWait(self._driver, 10).until(fun)