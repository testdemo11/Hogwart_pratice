用雪球迁移框架并实现黑名单操作（选用装饰器）
wrapper_decorated.py 是用函数里面套用装饰器的形式实现的，以@logit()形式装饰，要修改logfile的文件名称以logit(logfile = 'xxx.log')装饰即可
wrapper_class.py是通过类的形式实现装饰器的，以@WrapperBlack(logfile='black.log'),形式装饰；通过__call__()函数来封装装饰器的，__call__是魔法函数，该方法的功能类似于在类中重载 () 运算符，使得类实例对象可以像调用普通函数那样，以“对象名()”的形式使用。类的好处是如果打印日志并写入到文件中，可以将写到文件这个操作封装一个方法，调用即可，不用频繁with open；