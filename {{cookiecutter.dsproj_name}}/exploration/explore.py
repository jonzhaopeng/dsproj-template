# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

from futu import *
import pandas as pd

#%%
"""获取历史成交列表
"""

trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1',
                              port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, history_df = trd_ctx.history_deal_list_query(
    start="2021-01-01", end="2022-03-20")
if ret == RET_OK:
    print(history_df)
    if history_df.shape[0] > 0:  # 如果成交列表不为空
        print(history_df['deal_id'][0])  # 获取历史成交的第一个成交号
        print(history_df['deal_id'].values.tolist())  # 转为 list
else:
    print('history_deal_list_query error: ', history_df)
trd_ctx.close()

history_df['date'] = pd.to_datetime(history_df['create_time']).dt.date
history_df['time'] = pd.to_datetime(history_df['create_time']).dt.time
history_df['day'] = pd.to_datetime(history_df['date']).dt.dayofweek

# 按周内买卖交易统计周几交易量高，周几交易量低
df_count = history_df.groupby('day').count()

#%% 获取自选股列表

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_user_security("A")
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # 如果自选股列表不为空
        print(data['code'][0])    # 取第一条的股票代码
        print(data['code'].values.tolist())   # 转为 list
else:
    print('error:', data)
quote_ctx.close()  # 结束后记得关闭当条连接，防止连接条数用尽


#%% 订阅行情数据推送

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret_sub, err_message = quote_ctx.subscribe(
    ['HK.00700'], [SubType.QUOTE], subscribe_push=False)
# 先订阅 K 线类型。订阅成功后 FutuOpenD 将持续收到服务器的推送，False 代表暂时不需要推送给脚本
if ret_sub == RET_OK:  # 订阅成功
    ret, data = quote_ctx.get_stock_quote(['HK.00700'])  # 获取订阅股票报价的实时数据
    if ret == RET_OK:
        print(data)
        print(data['code'][0])   # 取第一条的股票代码
        print(data['code'].values.tolist())   # 转为 list
    else:
        print('error:', data)
else:
    print('subscription failed', err_message)
quote_ctx.close()  # 关闭当条连接，FutuOpenD 会在1分钟后自动取消相应股票相应类型的订阅


#%% 获取持仓标的列表

trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1',
                              port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.position_list_query()
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # 如果持仓列表不为空
        print(data['stock_name'][0])  # 获取持仓第一个股票名称
        print(data['stock_name'].values.tolist())  # 转为 list
else:
    print('position_list_query error: ', data)
trd_ctx.close()  # 关闭当条连接


#%% 获取账号资金情况

trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1',
                              port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.accinfo_query()
if ret == RET_OK:
    print(data)
    print(data['power'][0])  # 取第一行的购买力
    print(data['power'].values.tolist())  # 转为 list
else:
    print('accinfo_query error: ', data)
trd_ctx.close()  # 关闭当条连接

 #TODO ：拦截下单后做二次确认
#%%
"""
拦截的策略：
1.如果该标的今天清仓，则不能买入它的相反方向！
2.如果今天清仓了，那么冷静期是5个交易日！
"""

 #TODO ：每天监控持仓做日志，用Streamlit做日志记录就
#%%
"""
1.每天晚上20:00 邮件提醒我做港股日志
2.每天中午12:00 邮件提醒我做美股日志
3.系统自动把持仓列表整理成列表，我做日志就可以
"""
