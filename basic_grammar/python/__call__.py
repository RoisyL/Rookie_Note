'''
创建一个 Cache 类。这个类的实例将作为一个可调用对象，用于获取数据。
如果数据在缓存中，它就从缓存返回；
如果不在，它就调用一个慢速的 "数据库函数" 来获取数据，存入缓存，然后返回。
'''

import time

# 模拟一个非常慢的数据库查询
def slow_database_query(item_id: str) -> str:
    print(f"    >> 正在从慢速数据库查询 '{item_id}'...")
    time.sleep(1) # 模拟网络和磁盘延迟
    return f"这是 '{item_id}' 的数据"

class Cache:
    """
    一个简单的有状态缓存类。
    它应该在内部维护一个字典来存储缓存的数据。
    """
    
    # TODO: Part 1 - 初始化缓存状态
    # 在 __init__ 方法中，你需要初始化一个用于存储缓存的实例属性。
    # 思考一下，用什么数据结构来存储缓存最合适？
    def __init__(self):
        print("正在初始化缓存...")
        self._storage = {}

    # TODO: Part 2 - 实现 __call__ 方法
    # 让 Cache 的实例可以像函数一样被调用，例如：my_cache("item-1")
    #
    # 实现以下逻辑:
    # 1. 检查传入的 `item_id` 是否已经存在于你的缓存存储中。
    # 2. 如果存在，打印一条消息如 "从缓存命中！" 并立即返回缓存中的数据。
    # 3. 如果不存在，打印一条消息如 "缓存未命中！"，然后调用 `slow_database_query` 函数获取数据。
    # 4. 将获取到的新数据存入你的缓存存储中。
    # 5. 返回新获取的数据。
    def __call__(self, *args, **kwds):
        item_id = args[0]
        if item_id in self._storage:
            print("    >> 从缓存命中！")
            return self._storage[item_id]
        else:
            print("    >> 缓存未命中！")
            data = slow_database_query(item_id)
            self._storage[item_id] = data
            return data



# --- 验证区 (无需修改) ---
def main():
    print("--- 练习 1：__call__ 方法 ---")
    
    # 创建 Cache 的一个实例
    item_cache = Cache()
    
    print("\n第一次请求 'item-A':")
    data1 = item_cache("item-A") # 调用实例
    print(f"  -- 收到的数据: {data1}\n")
    # 预期输出：应该看到 "缓存未命中" 和 "慢速数据库查询" 的消息

    print("第二次请求 'item-A':")
    data2 = item_cache("item-A") # 再次调用实例
    print(f"  -- 收到的数据: {data2}\n")
    # 预期输出：应该看到 "从缓存命中！" 的消息，并且执行得非常快

    print("第一次请求 'item-B':")
    data3 = item_cache("item-B") # 调用实例
    print(f"  -- 收到的数据: {data3}\n")
    # 预期输出：应该看到 "缓存未命中" 和 "慢速数据库查询" 的消息
    
    # 验证缓存内容
    assert "item-A" in item_cache._storage
    assert "item-B" in item_cache._storage
    print("验证成功！缓存中包含了 'item-A' 和 'item-B'。")

if __name__ == "__main__":
    main()