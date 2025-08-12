'''
编写一个名为 create_api_client_class 的函数。
这个函数接收一个服务名称（如 "Weather"）和一个方法列表（如 ['get_current_temp', 'get_forecast']），然后动态地创建一个 API 客户端类。
这个类应该有一个 service_name 属性，并且列表中的每个方法名都应成为该类的一个实例方法，调用时能打印出模拟的 API 请求信息。
'''

def create_api_client_class(service_name: str, method_names: list[str]):
    """
    一个动态 API 客户端类的工厂函数。
    
    Args:
        service_name: API服务的名称 (例如 "Weather", "StockPrice")
        method_names: 一个包含该服务所有方法名的字符串列表
    
    Returns:
        一个新创建的、未实例化的类。
    """
    
    # TODO: Part 1 - 准备新类的属性字典
    # 这个字典将包含新类的所有属性和方法。
    #
    # 1. 添加一个类属性 `service_name`，其值应为传入的 `service_name` 参数。
    # 2. 为 `method_names` 列表中的每个方法名，动态创建一个真实的函数，并将其添加到字典中。
    #    - 这个动态创建的函数应该接受 `self` 和 `**kwargs` 作为参数。
    #    - 当被调用时，它应该打印出类似 "正在调用 [服务名] 的 [方法名] 方法，参数为 [参数]" 的信息。
    #    - 提示: 你可能需要再写一个辅助函数或使用 lambda 来 "捕获" 正确的方法名。
    class_attributes = {'service_name': service_name}
    
    def create_method(method_name):
        def method(self, **kwargs):
            print(f"正在调用 {self.service_name} 的 {method_name} 方法，参数为 {kwargs}")
            return {'method': method_name, 'args': kwargs}
        return method

    for method_name in method_names:
        class_attributes[method_name] = create_method(method_name)

    # TODO: Part 2 - 使用 type() 创建类
    # 使用 type() 的三参数形式 `type(name, bases, dict)` 来创建你的新类。
    # - `name`: 新类的名字，应该与 `service_name` + "Client" 组合而成 (例如 "WeatherClient")。
    # - `bases`: 父类的元组。这里我们可以用一个空元组 `()` 或 `(object,)`。
    # - `dict`: 你在 Part 1 中创建的属性字典。
    name = f"{service_name}Client"
    bases = (object,)
    new_class = type(name, bases, class_attributes)
    
    
    # TODO: Part 3 - 返回新创建的类
    # 注意是返回类本身，而不是它的实例。
    return new_class


# --- 验证区 (无需修改) ---
def main():
    print("\n--- 练习 2：使用 type() 动态创建类 ---")

    # 定义我们要创建的客户端的规格
    weather_methods = ['get_current_temp', 'get_5day_forecast']
    
    # 使用工厂函数动态创建 WeatherClient 类
    WeatherApiClient = create_api_client_class("Weather", weather_methods)
    
    # 验证创建的类
    print(f"动态创建的类: {WeatherApiClient}")
    print(f"类的名字: {WeatherApiClient.__name__}")
    
    # 实例化这个动态创建的类
    weather_client_instance = WeatherApiClient()
    print(f"实例的服务名属性: {weather_client_instance.service_name}")
    
    # 调用动态创建的方法
    print("\n调用动态方法:")
    response1 = weather_client_instance.get_current_temp(city="London", units="celsius")
    response2 = weather_client_instance.get_5day_forecast(city="Paris")
    
    # 验证方法是否真的存在并可调用
    assert hasattr(weather_client_instance, 'get_current_temp')
    assert callable(weather_client_instance.get_current_temp)
    assert response1['method'] == 'get_current_temp'
    assert response2['args']['city'] == 'Paris'
    
    print("\n验证成功！动态类和其方法均按预期工作。")


if __name__ == "__main__":
    main()