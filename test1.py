### 好 写个装饰器吧

# def get_name(text):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(text + func.__name__)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @get_name("fuckin")
# def vanessa(age):  ## vanessa = get_name(vanessa) || vanessa = get_name("fuckin")(vanessa)
#     print(age)
#
# if __name__ == '__main__':
#     vanessa(18)


###  好 学下lazyproperty
###  https://segmentfault.com/a/1190000005818249


###  好 学习下super()的用法
###  http://python.jobbole.com/86787/

###  好 学习下单例模式
###  http://python.jobbole.com/87294/

# import os
# print(os.path.split(os.path.realpath(__file__))[0])  # 拆成路径和文件名两部分
# print(os.pardir)  # 上一级

# if any(f in html.content for f in retry_flag):  # 写法