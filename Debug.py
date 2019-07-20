import time
import functools


# 显示函数执行时间及其名字
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        # print('%s 开始执行' % (fn.__name__))
        start = time.time()
        result = fn(*args, **kw)
        stop = time.time()
        print('%s 执行完毕.时间： %s s' % (fn.__name__, stop - start))
        return result
    return wrapper
