import re

from pip._vendor import requests
from bs4 import BeautifulSoup as bs
class HtmlScra:
    def __init__(self,url:str,headers:dict = {}):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }
        self.headers.update(headers)

    def get(self,params:dict):
        response = requests.get(self.url,headers = self.headers,params = params)
        return response.json()

class QAModel:
    def __init__(self,q:str,a:str):
        self.q = q
        self.a = a

def get_daily_hsf_service():
    scra = HtmlScra('http://hsf.alibaba.net/hsfops/envs/daily/services')
    res =scra.get({'filter':'ip','pattern':'30.5.48.31'})
    with open('a.txt','w',encoding='utf-8') as f:
        print(res,file=f)


def get_qa():
    scra = HtmlScra('https://ai-op.alibaba-inc.com/api/chat2/searchEffectEntriesByPage',{
        'cookie': 'cna=wcHBE63iZFcCASp4Su+m9UBK; UM_distinctid=1658e7db489460-07416740ad7b77-323b5b03-1fa400-1658e7db48a6e4; emplId=175162; l=AsjIptZYiql58zBvMmkfpY7/GD3acSx7; global_csrf_token=d8f152e5-8b1e-4425-a7b1-7823d4ad68af; SSO_LANG=ZH-CN; SSO_EMPID_HASH=74e5a43e84a1e2f247bc34f7652573f0; animate_date=2018911; cn_1260001221_dplus=%7B%22distinct_id%22%3A%20%221658e7db489460-07416740ad7b77-323b5b03-1fa400-1658e7db48a6e4%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201536668655%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201536668655%7D%7D; CNZZDATA1264634009=978369902-1536567667-%7C1536668488; EGG_SESS=uKc8ALaBEWs-DLyAd2mmMf5sqMCeEnn1-WI8jr6RFGxVFJVTfPfmltcCDNYsywGfy3xTrpMk2JcxBPCJoY9xfA2xXWrncNy_D30xf1Qo9r_1W6_PWiiy_RJO_ZziSa56eBLcH1zD9NUjFV6PWl4YG1A5Dz8kaFSMcxDZDznaq0lMQSkdcciDWxC1176ahgQgyz7Zo0mjAXBJylZnQRJyQTPjW4Na2w5p3Fnq6KqJ6rjyq9cOc_kdE3aMbWtjyB7bVI6JKE29q81QS8YLGeBL9AHF1dW2GeMru1ilMxdv6XUr-4tEgjvkB4BTdsCDzBQIRiZvSisSV__b3_bPpwr88Sl8yENPdUfFHRSXVbpLA5Nj-gOfyNLi-QaMsOaxey2EE0SerkAaQ8GG1Xyer0NKpsbk4aZ_-U2LyIqhJES4e-df9VH37tDG2uPIlOOB8t6WXTYfb3i56K3YTB4tY54_fFG2KICx0xyIaAKxCmHupAo5qJdTmgTDuGIZG9mbWpjruQIEOul0slwiF3HWrkiZQimwdQT-XLPNSCDlUft8R6PVIsxT1lWC2fET__0l1o9H6AWJa8-w05sXGcKfc_aMyjhW17bX4i-Y3Eptkz2Uz4-lo1IzS730w4PjMlhHRtzzUGShskG3G5f2EByzKaJn0ZGtjcIxn7eXYouHNXSAmokOrHelPiVh2KPAE7BxDJ1VlwF9_mS2MCrkiQKILOdWowppU8aFGLgeCFyu0B-HhFJuI_32B32cuTgockphM7KDCAmkv1P1PBhh4Ew4tWCs7_hAAzfHw8Zox0to79AtlEki_RdyXQilZK0A7T0Dmyq1qNhIJ5RovvP1WJ0btI1gQZ6ZVVdnpIpwBDKVwu1oXcrd_eT8NoN5PhRHDkUxuLzqmwrv0GrlNeq7bPzKi1UIviMJcsRPBGd6y_tWk03mbHSKhL-IPPt8-vnqbSW7EOft1ocPR1ahdhX86g6csC_VVFz6IDmk31znnCPpALOXlcxsCm2y3ZKzznoSmCOul3zNA_RlvtbmaU26401X0-WQPGWQiuMl159pZJwcMP4MoVYGESGV2q63MNVRZpVhW-oUQ0LytP3HAl2mmVg5UfxZmvAJN6VGT_OvkEdqaIHCm8P943btqj2BB74LVO04pl9aT-gHUVJ7yyNuzNutXx6FNTbyLs5TPAnii9gsyc1iq4TrCSnLvYbHFdong8Q-jU-rD3O2fq75wOvSZOMac_XN1LQlmoNT-VxcZ3xo1axqoWd4KXCr7mOF64Hx79k1e138KdIkAsiLNgFKaxhwVz29-e-5fMzh7A7m9EVqOcynxWFFEv7eQKj7je3jcYhkhqJLNqlmF3_gMnNbHuGo4jeOkk6dP2nVSNAydEil2inDjJ6A3htpiYycoba0PtNWp0DAQECqROrgZKYtD6DtR0AlGtJIJO2VZT4_1gvtwemY_xj3HTXxnsc35w5LcDVQX98sgHdoSpmyderw4BhlX51N-Q==; isg=BCoqiGtjBXJlAIke-rI-NTjwe5DSnpuSbeFa-LTjdX0I586hnCupBfJRc1PeFyaN'
    })
    res  = scra.get({'queryType':'FAQ_ALL_TYPE','keyword':'','topicList':'34',
                     'orderKey':'FAQ_ORDER_MODIFY_TIME','orderType':'FAQ_ORDER_DESC','pageSize':'15000','pageNo':'1'})
    ret_list = res['retValue']['entryList'] if res['code'] == 0 else []
    models = [QAModel(e['main'],e['answers'][0]) for e in ret_list]
    with open('qa.txt','w',encoding='utf-8') as f:
        for e in models:
            print('q:{}'.format(e.q),file=f)
            print('a:{}'.format(e.a),file=f)
            print('------------------------',file=f)
    return models

def process_cookie(cookie:str):
    cookie = cookie.replace(' ','')
    pairs = cookie.split(';')
    d = {}
    for pair in pairs:
        pair = pair.split('=',maxsplit=1)
        d[pair[0]] = pair[1]
    return d

def get_apps():
    scra = HtmlScra('http://code.aone.alibaba-inc.com/api/v3/projects/authorized/list',{'cookie': 'cna=wcHBE63iZFcCASp4Su+m9UBK; UM_distinctid=1658e7db489460-07416740ad7b77-323b5b03-1fa400-1658e7db48a6e4; ak_user_timezone=Asia/Shanghai; ak_user_locale=zh_CN; emplId=175162; l=AsjIptZYiql58zBvMmkfpY7/GD3acSx7; animate_date=2018912; ak_region_id=alibaba; new_openwork_feedback_animate=true; cn_1260001221_dplus=%7B%22distinct_id%22%3A%20%221658e7db489460-07416740ad7b77-323b5b03-1fa400-1658e7db48a6e4%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201536740177%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201536740177%7D%7D; hrc_sidebar=open; CODE_USER_COOKIE=39BE5D7E474D35F798333669B7F390C76FA1F502D8C02067F9167BD6EDDA88DBCC2D54E9CCE8D1EB55B7A09DAF2F25FD26FBE68C8F421571DBC12AA43FE3B1D0898FD91DB269332901C11B1ABB5FFFC6C6ED38376B38B3AE2AFD0D179AA637719222F17D9091B1B0F593D31ECBE1CB6993789834038F2379591864B02A20008D05DFE00C2D36CAE00BDC364802AEC54FBDEC9C831D6C19239D532A7FE300EFF23F46D561BF2877F060AC6B225D24E96272A91C93A5B330C1BEC0F73E35AD32EF61081E2CC003FBA7305DDED09D6C82A408E34E32268E09D9C146765548D726D45B82A3D69B9857325DF2297794AEC059D38C32B5710F0070394338E7F12563C8A6CB9522B80A7ADC56D0FFD9916E24AD794DB52948D2F0C17B3B13DA2274265BABB9F0ADBAD8CE9BD755C0008260D7179F0EFA19E50A264E4D080CD7C74294547832BA0B051ACCAC36EF0BF92E7CCDBA38D00DA0B1F6C6358817E3188129232EA63EEBC952C6F7215D6123C7AC3E9CDF16203584CEF33B522272F308373AD358AD2EC0C9E8A39B742D9DFD8CCEFC8D9DD3D4A9887B7418109C6737EF9B3FC8F2DB4B05E9D4EC409026E62F788D49E0DCA46162E29A147167B1801CB021A5801A2CFCD2BE134DF930EC80C45F15604530701A4987C97DC3FF2659909964A32F481E21CDD5CEB440CC5D21E27052D85D39; CODE_SSO_TOKEN=D92CC52CDB71F610C2EF03E79F43E11812C5377E503F722C56E2EFFED886D3E8854A4B68A9F20F7056EFB165E0EA26D5; SSO_LANG=ZH-CN; CODE_LAST_HEART_BEAT_TIME=1A82BB665A3E714947C05AA1E6712649; SSO_EMPID_HASH=e087cd97d35e40f2bb69ac42bdff1387; XSRF-TOKEN=16021679-eaad-4b0c-9807-12057a8d625b; CNZZDATA1259517254=1991557830-1536739795-%7C1536739795; isg=BDo6X9ovNS2zxbnOakIuZcgAi2BC7oo8_ZFKCEQyKU2ON99xLH3B1nQBg4NOpzZd'})
    querys = process_querystr('_input_charset=utf-8&page=1&archived=false&search=&order_by=last_activity_at')
    with open('app.txt','w',encoding='utf-8') as f:
        while True:
            res = scra.get(querys)
            if not res:
                break
            for e in res:
                print(e['name'],file=f)
                print(e['description'], file=f)
                print('-----------------',file=f)
            querys['page'] = str(int(querys['page']) + 1)
def process_querystr(query_str:str):
    pairs = query_str.split('&')
    d = {}
    for pair in pairs:
        pair = pair.split('=')
        d[pair[0]] = pair[1]
    return d
if __name__ == '__main__':
    get_qa()