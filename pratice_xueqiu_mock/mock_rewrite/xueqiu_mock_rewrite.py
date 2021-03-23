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
            # for i in range(4):
            #     data['data']['items'][i]['quote']['name'] = 'tnew_test'
            data['data']['items'][1]['quote']['name'] += data['data']['items'][1]['quote']['name']
            data['data']['items'][2]['quote']['name'] = ''
            flow.response.text = json.dumps(data)


addons = [
    Counter()
]