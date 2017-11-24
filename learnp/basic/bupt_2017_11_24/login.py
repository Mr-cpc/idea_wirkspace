from pip._vendor import requests


class Login:
    def __init__(self,login_url,**kwargs):
        self.login_url = login_url
        # self.data = {kwargs["uname_name"]:kwargs["uname_val"],kwargs["passwd_name"]:kwargs["passwd_val"]}
        self.data = {"DDDDD":"2016140606","upass":"046614"}
        self.cookie = {"myusername":"2016140606", "username":"2016140606", "smartdot":"046614"}
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
             "Content-Type":"application/x-www-form-urlencoded"
        }
    def login(self):
        sesssion = requests.session()
        # requests.post(self.login_url,)
        sesssion.post(self.login_url,self.data,cookies = self.cookie,headers = self.headers)
        r = sesssion.get(self.login_url)
        print(r.text)


lg = Login("http://10.3.8.211/",**{"uname_name":"DDDDD","passwd_name":"upass","uname_val":"2016140606","passwd_val":"046614"})
lg.login()
