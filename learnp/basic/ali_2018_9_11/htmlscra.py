import re
from mako.template import Template
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


def bots():
    """
    :return: a list consists of dict like [{'id':1,'name':'xxx'}]
    """
    scra = HtmlScra('https://pre2-ai-op.alibaba-inc.com/api/theme/bots',{'cookie': 'cna=wcHBE63iZFcCASp4Su+m9UBK; UM_distinctid=1658e7db489460-07416740ad7b77-323b5b03-1fa400-1658e7db48a6e4; l=AsjIptZYiql58zBvMmkfpY7/GD3acSx7; new_openwork_feedback_animate=true; hrc_sidebar=open; goc_portal_locale=zh; emplId=175162; animate_date=2018918; cn_1260001221_dplus=%7B%22distinct_id%22%3A%20%221658e7db489460-07416740ad7b77-323b5b03-1fa400-1658e7db48a6e4%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201537249480%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201537249480%7D%7D; CNZZDATA1264634009=396751084-1537247032-%7C1537247032; EGG_SESS=uKc8ALaBEWs-DLyAd2mmMf5sqMCeEnn1-WI8jr6RFGxVFJVTfPfmltcCDNYsywGfy3xTrpMk2JcxBPCJoY9xfA2xXWrncNy_D30xf1Qo9r_1W6_PWiiy_RJO_ZziSa562HSCkvGXp6rYAMxLp1eF__9-PLKIcbVfep27WV6A3jL4EjgB6lUGssfCsRx1UnhEMj0CohShKkItusuTqnNeUIfsMeDAYycSBRb1rkTlmQeXzlNyG7Fm4MiL6CdpRxX6HSzT_mMYRVesncXEh01L2jWrAD9UuPeo9xBlljkM_eTg1p5StU79PMkZqVAxPUCw_OMJH65rkt3WB1d0Z9nG7XbUGa4B14lPPGWke7_5AD-ckVbQnLw4Y9eReW6hm_pZoHGxAlJUxjj64RDZR0sjCP7FPX5rIBhFolzlP_DUK_WelizK393lxSGsGFwapScFZca2-dWBgpMsjqZ4mVRelh7mHM3H_spVe-fmrGl44LMY7fo2D5y9o4-jeVdx0eHUo5nPHXuE4CbSXQ9tj8tUjSCAmgKYegl2F4mYhlwN0RplQXIHj_g_mQkQEObmDTaDe1gMP4CVdW6AHNnTm0d-bFY1EgXRF9jVwrwB3MHtDIp52w58sLBMp8oFL8_GsrvSNVRxpAEFD89qVHbSfj7Qj8idAWh7_qW9YLipWBksuArX8mfi7UCZXnV4SV-kehb_frD_u0CjulebzIqTwbnreE-knGap4OZFxxgSF08xtKxXf4SLkkvZDXVAV9fmRG1FuJSKBLOzrTUuctD_2KZeCvKzD6cW1LI_Fa08HGbuS6GcdqC_eBk2gQhbS4m0RYto0F07-pwJ43ZhChHrtafLvQuBpM9w862p91vCf7cqNfZ9qVJQT6EXDAsF_XACDghJ0DyAgxDPlxdIfcYnBiMYHmHcxJPseU8wfxWtNuxxWVQuCDpp7uih1Sq3cc_kqoiBN-TQw23GYWH2WeiTPIKlEHhV0kTUlsl1vMl0vHYOKCsCtiwidyf6KEifRVegeVJ7nYdUdy33YW5QDqt9f64BpZwwsx0T4MepoMJgu-ANryDK2dfDniuHJEHxlgXfksD2Qrp5QWRl-CCNIRwsBlA_sLk14Dbjkji6pv14rvCIQlIVjx1LY7sBIVmBURJcq16m6I4yUTVcae4yMIiV-7rH08lo3oraYQKnKfkgvCWoW7XHViXPL8_8zWYK8hZxz2IqdxPtfyDcJw46x35HodD7j_dwohH8qxrWd2SjTilkdIm8eSOaV5HuG0gVDC2Q-qywnoe1cXVVmQA8yXxfHTUiHznEXPZvSzjuidN0W_LOVkUrgTnKblRIJY6S3GLnHnHgpibvjEYJ7t1kiwkkRfD8gUJqQe5T_HwJ1dhXmtAFj3KuVY9o92Vzqq_SPM0f6ZC136cg0_adg-MCEbrfuuGkCmRB0THWMZRwhMA9Py1Zo5PW5nApK6YKBuPPfUikbR3G; isg=BPX1tXrmwhRyECaf-SsZxCtZBHGxd5lFvtj1uXcc0Gy7TjxAO8OmVK-InFJdDsE8'})
    data = scra.get({})
    if data['code'] != 0:
        return []
    bot_list = data['retValue']['botsList']
    with open('bots.txt','w',encoding='utf-8') as f:
        for i,bot in enumerate(bot_list):
            print('{}.bot_id: {},name: {}'.format(i,bot['id'],bot['name']),file=f)

    return bot_list
def topics(bot_id:int):
    scra = HtmlScra('https://pre2-ai-op.alibaba-inc.com/api/theme/topicBybots',{'cookie': 'cna=wcHBE63iZFcCASp4Su+m9UBK; UM_distinctid=1658e7db489460-07416740ad7b77-323b5b03-1fa400-1658e7db48a6e4; l=AsjIptZYiql58zBvMmkfpY7/GD3acSx7; new_openwork_feedback_animate=true; hrc_sidebar=open; goc_portal_locale=zh; emplId=175162; animate_date=2018918; cn_1260001221_dplus=%7B%22distinct_id%22%3A%20%221658e7db489460-07416740ad7b77-323b5b03-1fa400-1658e7db48a6e4%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201537249480%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201537249480%7D%7D; CNZZDATA1264634009=396751084-1537247032-%7C1537247032; EGG_SESS=uKc8ALaBEWs-DLyAd2mmMf5sqMCeEnn1-WI8jr6RFGxVFJVTfPfmltcCDNYsywGfy3xTrpMk2JcxBPCJoY9xfA2xXWrncNy_D30xf1Qo9r_1W6_PWiiy_RJO_ZziSa562HSCkvGXp6rYAMxLp1eF__9-PLKIcbVfep27WV6A3jL4EjgB6lUGssfCsRx1UnhEMj0CohShKkItusuTqnNeUIfsMeDAYycSBRb1rkTlmQeXzlNyG7Fm4MiL6CdpRxX6HSzT_mMYRVesncXEh01L2jWrAD9UuPeo9xBlljkM_eTg1p5StU79PMkZqVAxPUCw_OMJH65rkt3WB1d0Z9nG7XbUGa4B14lPPGWke7_5AD-ckVbQnLw4Y9eReW6hm_pZoHGxAlJUxjj64RDZR0sjCP7FPX5rIBhFolzlP_DUK_WelizK393lxSGsGFwapScFZca2-dWBgpMsjqZ4mVRelh7mHM3H_spVe-fmrGl44LMY7fo2D5y9o4-jeVdx0eHUo5nPHXuE4CbSXQ9tj8tUjSCAmgKYegl2F4mYhlwN0RplQXIHj_g_mQkQEObmDTaDe1gMP4CVdW6AHNnTm0d-bFY1EgXRF9jVwrwB3MHtDIp52w58sLBMp8oFL8_GsrvSNVRxpAEFD89qVHbSfj7Qj8idAWh7_qW9YLipWBksuArX8mfi7UCZXnV4SV-kehb_frD_u0CjulebzIqTwbnreE-knGap4OZFxxgSF08xtKxXf4SLkkvZDXVAV9fmRG1FuJSKBLOzrTUuctD_2KZeCvKzD6cW1LI_Fa08HGbuS6GcdqC_eBk2gQhbS4m0RYto0F07-pwJ43ZhChHrtafLvQuBpM9w862p91vCf7cqNfZ9qVJQT6EXDAsF_XACDghJ0DyAgxDPlxdIfcYnBiMYHmHcxJPseU8wfxWtNuxxWVQuCDpp7uih1Sq3cc_kqoiBN-TQw23GYWH2WeiTPIKlEHhV0kTUlsl1vMl0vHYOKCsCtiwidyf6KEifRVegeVJ7nYdUdy33YW5QDqt9f64BpZwwsx0T4MepoMJgu-ANryDK2dfDniuHJEHxlgXfksD2Qrp5QWRl-CCNIRwsBlA_sLk14Dbjkji6pv14rvCIQlIVjx1LY7sBIVmBURJcq16m6I4yUTVcae4yMIiV-7rH08lo3oraYQKnKfkgvCWoW7XHViXPL8_8zWYK8hZxz2IqdxPtfyDcJw46x35HodD7j_dwohH8qxrWd2SjTilkdIm8eSOaV5HuG0gVDC2Q-qywnoe1cXVVmQA8yXxfHTUiHznEXPZvSzjuidN0W_LOVkUrgTnKblRIJY6S3GLnHnHgpibvjEYJ7t1kiwkkRfD8gUJqQe5T_HwJ1dhXmtAFj3KuVY9o92Vzqq_SPM0f6ZC136cg0_adg-MCEbrfuuGkCmRB0THWMZRwhMA9Py1Zo5PW5nApK6YKBuPPfUikbR3G; isg=BPX1tXrmwhRyECaf-SsZxCtZBHGxd5lFvtj1uXcc0Gy7TjxAO8OmVK-InFJdDsE8'})
    data = scra.get({'botId': bot_id})
    if data['code'] != 0:
        return []
    topic_list = data['retValue']['topicList']
    with open('{}_topics.txt'.format(bot_id),'w',encoding='utf-8') as f:
        for topic in topic_list:
            print('topic_id: {},name: {}'.format(topic['id'], topic['name']),file=f)

    return topic_list

def get_note():
    scra = HtmlScra('https://note.alibaba-inc.com/note/listNotes.json',
                    {'cookie': 'cna=wcHBE63iZFcCASp4Su+m9UBK; UM_distinctid=1658e7db489460-07416740ad7b77-323b5b03-1fa400-1658e7db48a6e4; l=AsjIptZYiql58zBvMmkfpY7/GD3acSx7; new_openwork_feedback_animate=true; hrc_sidebar=open; goc_portal_locale=zh; emplId=175162; animate_date=2018919; alidocs-note_USER_COOKIE=AA7A1B3B7CECEB463BA90DE430EE704125E60D51DA617CBB9B32601F01CCC27300586F3D53D86E167451D517E9544AC40A18E55B5BEED6A4FF65C76CCC1FF04B8908B93A8661129CF26A67579D0588C88CC1335EC73C8DEDBC16D65C15CB9B9058D7D0F18A1A7BB5DE0A23FA57B1B04158300FF118597A076ECEB08C0851450CD05C855B6A1004EC28A63C918D7D99D5DA499B1B3EA41B5C0FA3D4E506E6EE562CD821332E76735D8539FEE7DFFDCB6822960781A845145F223452416409118E; SSO_LANG=ZH-CN; SSO_EMPID_HASH=8be487f58a9f53583743e742ca8dc011; emplId=175162; _csrf_token=23223656-b707-45f9-8317-4fa02bd2d5b2; cn_1260001221_dplus=%7B%22distinct_id%22%3A%20%221658e7db489460-07416740ad7b77-323b5b03-1fa400-1658e7db48a6e4%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201537251569%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201537251569%7D%7D; alidocs-note_SSO_TOKEN=EC87B4D74BB1369B8C82D9E62C947B6E05C7FC8C8C0A9918968203A34D0C96536FC5F110FB2746AD2EA5A01EF250779F; alidocs-note_LAST_HEART_BEAT_TIME=90183F69E112EFCA8EA3E3A8AB6724FE; isg=BKmpB5eu1nnJmur7pa-tGD9luFUdc6luypS5XUuaKhAXEsckk8bLeF5k0PaBijXg'})
    data = scra.get(process_querystr('_api=AliDocList.listNotes&_mock=false&_csrf=23223656-b707-45f9-8317-4fa02bd2d5b2&accessToken=&client=&pageSize=1000&lastId=&lastModifiedAt=&noteBookId=149332&sortCol=gmt_modified&sortOrder=desc&_stamp=1537323900377'))
    if not data['success']:
        return
    notes = data['content']['items']
    for note in notes:
        get_note_detail(note)
def get_note_detail(note):
    query = {'_api': 'Note.viewNote',
             '_mock': 'false',
             '_csrf': '23223656-b707-45f9-8317-4fa02bd2d5b2',
             'accessToken': '',
             'client': '',
             'noteId': str(note['id']),
             '_stamp': '1537326720873'}
    scra = HtmlScra('https://note.alibaba-inc.com/note/viewNote.json',{
        'cookie': 'cna=wcHBE63iZFcCASp4Su+m9UBK; UM_distinctid=1658e7db489460-07416740ad7b77-323b5b03-1fa400-1658e7db48a6e4; l=AsjIptZYiql58zBvMmkfpY7/GD3acSx7; new_openwork_feedback_animate=true; hrc_sidebar=open; goc_portal_locale=zh; emplId=175162; animate_date=2018919; alidocs-note_USER_COOKIE=AA7A1B3B7CECEB463BA90DE430EE704125E60D51DA617CBB9B32601F01CCC27300586F3D53D86E167451D517E9544AC40A18E55B5BEED6A4FF65C76CCC1FF04B8908B93A8661129CF26A67579D0588C88CC1335EC73C8DEDBC16D65C15CB9B9058D7D0F18A1A7BB5DE0A23FA57B1B04158300FF118597A076ECEB08C0851450CD05C855B6A1004EC28A63C918D7D99D5DA499B1B3EA41B5C0FA3D4E506E6EE562CD821332E76735D8539FEE7DFFDCB6822960781A845145F223452416409118E; SSO_LANG=ZH-CN; SSO_EMPID_HASH=8be487f58a9f53583743e742ca8dc011; emplId=175162; _csrf_token=23223656-b707-45f9-8317-4fa02bd2d5b2; cn_1260001221_dplus=%7B%22distinct_id%22%3A%20%221658e7db489460-07416740ad7b77-323b5b03-1fa400-1658e7db48a6e4%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201537251569%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201537251569%7D%7D; alidocs-note_SSO_TOKEN=EC87B4D74BB1369B8C82D9E62C947B6E05C7FC8C8C0A9918968203A34D0C96536FC5F110FB2746AD2EA5A01EF250779F; alidocs-note_LAST_HEART_BEAT_TIME=90183F69E112EFCA8EA3E3A8AB6724FE; isg=BOLiKZArzZx1vtH2QgoGnTDIM2haNtKLVcmiECx55tW8_4p5FMISXCoZK3umb17l'
    })
    data = scra.get(query)
    if not data['success']:
        return
    template = Template(filename='html.tpl')
    with open('{}.html'.format(note['title']),'w',encoding='utf-8') as f:
        print(template.render(body = data['content']['content'],title = data['content']['title']), file=f)
if __name__ == '__main__':
    get_note()
    # get_apps()
    # get_qa()