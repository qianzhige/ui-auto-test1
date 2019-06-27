
from time import sleep
import pytest
class Test_mall():

    @pytest.mark.fahuo
    def test_fahuo(self,base):
        base.driver.get("http://192.168.60.132/#/oms/order")
        base.click("点击订单状态",'''//label[contains(text(),'订单状态')]/following-sibling::div//input''')
        # 选择待发货//span[contains(text(),'待发货')]
        base.click("点击代发货",'''//span[contains(text(),'待发货')]''')
        #点击查询搜索//span[contains(text(),'查询搜索')]
        base.click("点击查询搜索",'''//span[contains(text(),'查询搜索')]''')
        #点击第一笔订单//span[contains(text(),'订单发货')][1]
        base.click("点击第一笔订单",'''//span[contains(text(),'订单发货')][1]''')
        #点击发货//span[contains(text(),'确定')]
        assert "发货列表" in base.driver.page_source
        base.click('物流公司', '''(//input[@class="el-input__inner"])[1]''')
        base.click("中通快递",'''//ul//li[@class="el-select-dropdown__item"][2]''')
        base.send_keys('物流单号', '''(//input[@class="el-input__inner"])[2]''',"888979756")
        base.click("点击发货", '''(//span[contains(text(),'确定')])[1]''')
        base.click("点击发货确定", '''(//span[contains(text(),'确定')])[2]''')
        text = base.get_text('获取提示文本', '''//div[@aria-label="提示"]/following-sibling::div//p''')
        assert '成功' in text

    @pytest.mark.tuihuo
    def test_tuihuo(self, base):
        base.driver.get("http://192.168.60.132/#/oms/returnApply")
        #点击处理状态//label[contains(text(),'处理状态')]/following-sibling::div//div//input
        base.click("处理状态",'''//label[contains(text(),'处理状态')]/following-sibling::div//div//input''')
        #点击待处理//span[contains(text(),'待处理')]
        base.click("待处理",'''//span[contains(text(),'待处理')]''')
        #点击查询搜索//span[contains(text(),'查询搜索')]
        base.click("查询搜索",'''//span[contains(text(),'查询搜索')]''')
        #点击查看详情(//span[contains(text(),'查看详情')])[1]
        base.click("查看详情",'''(//span[contains(text(),'查看详情')])[1]''')
        #滚动窗口
        base.scroll_screen("滚动窗口")
        #获取订单金额
        money = base.get_text("获取订单金额", '''//div[contains(text(),'订单金额')]/following-sibling::div''')
        money = money[1:]
        #输入退款金额
        base.send_keys("输入退款金额",'''(//input[@type="text"])[1]''',str(money))
        # #填写退款金额
        # base_ui.send_keys("退款金额",'''(//input[@type="text"])[1]''','3585')
        #点击确认退货//span[contains(text(),'确认退货')]
        base.click("确认退货",'''//span[contains(text(),'确认退货')]''')
        #点击确认//span[contains(text(),'确定')]
        base.click("确认",'''//span[contains(text(),'确定')]''')
        #获取提示文本
        text = base.get_text("获取提示文本", '''//div[@role="alert"]/p''')
        assert '操作成功' in text
        sleep(3)
