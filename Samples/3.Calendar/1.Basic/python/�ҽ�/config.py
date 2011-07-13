# -*- coding: UTF-8 -*-

#Python에서 HTTP(S)통신을 하기위한 연결 정보입니다.
#apiServer는 API서비스를 제공하는 서버를 나타냅니다.
#apiPort는 API서비스를 제공하는서버의 서비스 포트를 나타냅니다.
#https방식(SSL)의 port는 443이며 http방식을 이용하고자 할땐 apiport를 80으로 설정합니다.
#Daum API는 SSL만 지원합니다.
api_server = 'apis.daum.net'
api_port = 443

#DaumAPI(OAuth)에 필요한 URL입니다. 
request_token_Url = 'https://apis.daum.net/oauth/requestToken'
authorization_url = 'https://apis.daum.net/oauth/authorize'
access_token_url = 'https://apis.daum.net/oauth/accessToken'

#https://apis.daum.net/oauth/consumer/input에서 발급받으신 counsumerKey, consumer_secret,callback_url을 설정합니다.
consumer_key = '발급받으신 consumer_key를 입력하세요.'
consumer_secret = '발급받으신 consumer_secret를 입력하세요.'
callback_url= '등록하신 callback_url을 입력하세요.'
oauth_file = '인증 안내 html파일의 절대경로를 입력하세요.'

consumer_key = 'b9b8045f-ed52-4c16-9173-28b6b982c33f'
consumer_secret = 'Zoa8ByqKHWABKCdScVKRqjB61SFpntmkNsHD8n-Ot-vGY2kIBlH.AA00'
callback_url= 'http://mademin.com/tutorial_python/calender/callback.py'

index_file = "/home/mademin/service/wwwroot/tutorial_python/calender/index.html"
oauth_file = "/home/mademin/service/wwwroot/tutorial_python/calender/oauth.html"

