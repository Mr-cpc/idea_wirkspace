from urllib import request
response = request.urlopen("http://www.baidu.com");
page = response.read()
page = page.decode('utf-8')
fo = open("xx.txt","a+",encoding='utf-8')
fo.write(page)
print(page)
fo.close()