# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import mitmproxy
from mitmproxy import ctx, http
import json

class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

    def response(self, flow: http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.pretty_url:
            with open('data_new.json', 'r', encoding='utf-8') as f:
                #json.dump() 和 json.load() 来编码和解码JSON数据,用于处理文件
                #json.dumps，json.loads对string格式进行转换，dumps是将python对象转成str,loads是将str转成python对象（dict）
                data = json.load(f) #读取文件，将f文件中的内容读取到data中，格式为dict; json.dump(data,f1)将data里面的内容写入f1文件中,写入文件，Python不判断内容的内容格式
            flow.response.text = json.dumps(data)



addons = [
    Counter()
]