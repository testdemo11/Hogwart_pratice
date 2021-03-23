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
            data = json.loads(flow.response.text)
            data = self.json_travel(data)
            flow.response.text = json.dumps(data)

    def json_travel(self,data):
        if isinstance(data,dict):
            #{'test':{'tnew':[1,'hello']}}
            for key,value in data.items():
                data[key] = self.json_travel(value)
        elif isinstance(data,list):
            data = [self.json_travel(value) for value in data]
        elif isinstance(data,int) or isinstance(data,float):
            data = data
        elif isinstance(data,bool):
            data = data
        elif isinstance(data,str):
            if data == "阿里巴巴-SW":
                data += data
            elif data == "阿里巴巴":
                data = ''
            else:
                data = data

        else:
            data = data
        return data


addons = [
    Counter()
]