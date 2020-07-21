from page.indexPage import IndexPage
from time import sleep

class TestQiYeWeiXin:

    def setup(self):
        self.index = IndexPage(reuse=True)
    def test_one(self):

        add_member = self.index.goto_add_member()
        # 添加成员
        add_member.add_member()
        sleep(2)
        # 测试是否添加
        assert "zcp" in add_member.find_title()
