from pip._vendor import requests


class Login:
    def __init__(self,data:dict = {"DDDDD":"2016140606","upass":"046614","0MKKey":""},login_url:str = "http://10.3.8.211",logout_url:str = "http://10.3.8.211/F.htm"):
        self.login_url = login_url
        self.data = data
        # self.data = {"DDDDD":"2016140606","upass":"046614","0MKKey":""}
        # self.cookie = {"myusername":"2016140606", "username":"2016140606", "smartdot":"046614"}
        self.login_headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded",
            "Referer":"http://10.3.8.211/"
        }
        self.logout_url = logout_url
        self.session = requests.session()
    def login(self):
        r = self.session.post(self.login_url,self.data,headers = self.login_headers)
        print(r.text)

    def logout(self):
        print(self.logout_url)
        r = self.session.get(self.logout_url,headers = self.login_headers)
        print(r.text)
