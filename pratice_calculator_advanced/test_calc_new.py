import allure
import pytest
import yaml

with open("./data/calc.yaml") as f:
    # #获取yaml文件中add对应的数值
    # data_add = yaml.safe_load(f)["add"]
    data = yaml.safe_load(f)
    data_add = data["add"]
    add_datas = data_add['adddata']

    data_div = data["div"]
    div_datas = data_div['divdata']

    data_sub = data["sub"]
    sub_datas = data_sub["subdata"]

    data_mul = data["mul"]
    mul_datas = data_mul["muldata"]


# 获取加法数据
@pytest.fixture(params=add_datas)
def get_datas_add(request):
    # data = request.param
    # print(f"测试数据为{data}")
    yield request.param


# 获取除法数据
@pytest.fixture(params=div_datas)
def get_datas_div(request):
    # data = request.param
    # print(f"测试数据为{data}")
    yield request.param


# 获取减法数据
@pytest.fixture(params=sub_datas)
def get_datas_sub(request):
    # data = request.param
    # print(f"测试数据为{data}")
    yield request.param


# 获取乘法数据
@pytest.fixture(params=mul_datas)
def get_datas_mul(request):
    # data = request.param
    # print(f"测试数据为{data}")
    yield request.param


@allure.feature("测试计算器")
class TestCalculator:
    """
     1 把setup 和teardown换成fixture方法get_calc
     2 把get_calc放到conftest.py
     3 把参数化换成了fixture参数化方式
     4 测试用例中的数据需要通过get_datas获取
      get_datas 返回了一个列表[0.1,0.2,0.3] 分别代表了a,b expect
    """

    # @pytest.mark.parametrize("a,b,expect",add_datas)
    @allure.story("计算器的加法测试")
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_datas_add):
        # 假设最大能输入999999999
        if get_datas_add[0] > 999999999 or get_datas_add[1] > 999999999:
            print("超出最大数值999999999，不允许输出")
            assert False
        # 假设最小能输入-999999999
        elif get_datas_add[0] < -999999999 or get_datas_add[1] < -999999999:
            print("超出最小数值-999999999，不允许输出")
            assert False
        else:
            # 调用add方法
            result = get_calc.add(get_datas_add[0], get_datas_add[1])
            # 假设result最大能输入999999999
            if result > 999999999:
                print("超出最大数值999999999，不允许输出")
                assert False
            # 假设result最小能输入-999999999
            elif result < -999999999:
                print("超出最小数值-999999999，不允许输出")
                assert False
            else:
                if isinstance(result, float):
                    # 浮点型的计算，是二进制运算，可能会丢位，所以可以使用round方法处理浮点数，强制保留2位数
                    result = round(result, 2)
                # 断言判断
                assert result == get_datas_add[2]

    # @pytest.mark.parametrize("a,b,expect",div_datas,ids= div_id)
    # @pytest.mark.parametrize("a,b,expect", div_datas)
    @allure.story("计算器的除法测试")
    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_datas_div):
        # 假设最大能输入999999999
        if get_datas_div[0] > 999999999 or get_datas_div[1] > 999999999:
            print("超出最大数值999999999，不允许输出")
            assert False
        # 假设最小能输入-999999999
        elif get_datas_div[0] < -999999999 or get_datas_div[1] < -999999999:
            print("超出最小数值-999999999，不允许输出")
            assert False
        # 判断除数是否为0，为0不能除
        elif get_datas_div[1] == 0:
            print("b为除数，不可以为0")
            assert False
        # 判断被除数是否为0，为0，除数任意数都是为0（除数0除外）
        elif get_datas_div[0] == 0:
            result = get_calc.div(get_datas_div[0], get_datas_div[1])
            assert result == 0
        # 判断a和b是否相等，相等，任意数除完结果都是1（除数0除外）
        elif get_datas_div[0] == get_datas_div[1]:
            # 调用div方法
            result = get_calc.div(get_datas_div[0], get_datas_div[1])
            # result = int(result)
            assert result == 1
        else:
            result = get_calc.div(get_datas_div[0], get_datas_div[1])
            # 假设result最大能输出999999999
            if result > 999999999:
                print("超出最大数值999999999，不允许输出")
                assert False
            # 假设result最小能输出-999999999
            elif result < -999999999:
                print("超出最小数值-999999999，不允许输出")
                assert False
            else:
                if isinstance(result, float):
                    result = round(result, 2)
                assert result == get_datas_div[2]

    @allure.story("计算器的减法测试")
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_datas_sub):
        if get_datas_sub[0] > 999999999 or get_datas_sub[1] > 999999999:
            print("超出最大数值999999999，不允许输出")
            assert False
        # 假设最小能输入-999999999
        elif get_datas_sub[0] < -999999999 or get_datas_sub[1] < -999999999:
            print("超出最小数值-999999999，不允许输出")
            assert False
        # 判断两个数是否相等
        elif get_datas_sub[0] == get_datas_sub[1]:
            result = get_calc.sub(get_datas_sub[0], get_datas_sub[1])
            assert result == 0
        else:
            result = get_calc.sub(get_datas_sub[0], get_datas_sub[1])
            # 假设result最大能输出999999999
            if result > 999999999:
                print("超出最大数值999999999，不允许输出")
                assert False
            # 假设result最小能输出-999999999
            elif result < -999999999:
                print("超出最小数值-999999999，不允许输出")
                assert False
            else:
                if isinstance(result, float):
                    result = round(result, 2)
                assert result == get_datas_sub[2]

    @allure.story("计算器的乘法测试")
    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, get_datas_mul):
        if get_datas_mul[0] > 999999999 or get_datas_mul[1] > 999999999:
            print("超出最大数值999999999，不允许输出")
            assert False
        # 假设最小能输入-999999999
        elif get_datas_mul[0] < -999999999 or get_datas_mul[1] < -999999999:
            print("超出最小数值-999999999，不允许输出")
            assert False
        # 判断其中一个数是否为0
        elif get_datas_mul[0] == 0 or get_datas_mul[1] == 0:
            result = get_calc.mul(get_datas_mul[0], get_datas_mul[1])
            assert result == 0
        else:
            result = get_calc.mul(get_datas_mul[0], get_datas_mul[1])
            # 假设result最大能输出999999999
            if result > 999999999:
                print("超出最大数值999999999，不允许输出")
                assert False
            # 假设result最小能输出-999999999
            elif result < -999999999:
                print("超出最小数值-999999999，不允许输出")
                assert False
            else:
                if isinstance(result, float):
                    result = round(result, 2)
                assert result == get_datas_mul[2]
