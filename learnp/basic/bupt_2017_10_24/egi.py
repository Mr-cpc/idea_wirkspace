from pip._vendor import requests
from bs4 import BeautifulSoup


def send_to_ysz(mat,url):
    data = ""
    for row in mat:
        data += " ".join([str(num) for num in row])
        data += "\n"
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Coefficients\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"outputFormat\"\r\n\r\nfloat\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"outputPrecision\"\r\n\r\n4\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--" %(data)
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "575258bf-5724-7191-9537-5d92fff0370d"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

def parse_egi_result(text):
    soup = BeautifulSoup(text,"html.parser")
    tables =soup.find_all("table")
    try:
        egi_vals = [float(num) for num in [ele.string.strip() for ele in tables[-2].find_all("td")][1::2]]
    except ValueError:
        raise Exception("有复数特征值")
        return
    tds = [ele.string.strip() for ele in tables[-1].find_all("td")]
    row_num = len(tables[-1].find_all("tr")) - 1
    col_num = len(tds) // (row_num+1)
    egi_vecs = [None] * col_num
    for col in range(col_num):
        egi_vecs[col] = tds[col+col_num::col_num]
    # print(egi_vecs)
    # print(tds)
    return egi_vals,[[float(egi_vecs[row][col]) for col in range(len(egi_vecs[0]))]for row in range(len(egi_vecs))]
    # for i in tables[-1]:
    #     print("``````")
    #     print(i)
    #     print("``````")
# with open("out.txt","w",encoding="utf-8") as f:
#     f.write(response.text)
# text = send_to_ysz([[1,-2,1],[-1,3,1],[4,-1,0]],"http://www.yunsuanzi.com/cgi-bin/eigen_decomp.py")
# parse_egi_result(text)