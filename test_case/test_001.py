import pytest
import os
import allure

# 1、定义函数类型
# def test_01():
#     assert 1 + 1 == 2#断言
#
#
# def test_02():
#     assert 1 + 1 == 3

#添加一级标题
@allure.feature('一级标签')
# 2、封装测试类
class TestLogin:
    # 该测试类前置条件--初始化
    def setup_class(self):
        print('执行测试用例之前执行的方法')

    # 单个变量
    # @pytest.mark.parametrize('a',[1,2,3,2])
    # def test_log01(self,a):
    #     assert 1 + 1 == a  # 断言

    #添加二级标签
    @allure.story('二级标签')
    #添加标题
    @allure.title('标题')
    # 多个变量
    @pytest.mark.parametrize('a,b', [(1, 1), (1, 2), (1, 3), (1, 2)])
    def test_log02(self, a, b):
        assert a + b == 3

    def teardown_class(self):
        print('执行测试用例之后执行的方法')


if __name__ == '__main__':
    # 添加allure 报告
    # 1、--alluredir  存放目录
    pytest.main(['test_001.py', '-s', '--alluredir', '../report/tmp'])
    # 2、allure generate allure 报告  cmd指令 os.system()
    # os.system('allure generate 报告生成数据 -o 报告存放目录 --clean')
    os.system('allure generate ../report/tmp -o ../report/report --clean')
    # 3、

