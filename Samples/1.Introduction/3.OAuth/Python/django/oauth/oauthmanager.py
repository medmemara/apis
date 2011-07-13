# -*- coding: UTF-8 -*-
import oauthmodule
import config
"""
	oauth 단계별 모듈입니다.
        request_token는 session에 기록합니다.
"""
class OAuth_manager(object):
    def __init__(self,session):
        self.session = session
        self.oauth = oauthmodule.OAuth(config.consumer_key, config.consumer_secret, config.api_server, config.api_port, self.session)
    def check_access_token(self):
        if self.oauth.access_token_read():           
            return True
        return False
    def create_reqeust_token(self):
        request_token = self.oauth.request_token(config.request_token_url, config.callback_url)
        self.session['request_token'] = request_token.to_string()
        redirect_url = self.oauth.request_authorize_user(request_token, config.authorization_url, config.callback_url)
        return redirect_url
    def create_access_token(self,verifier_code):
        request_token_string =  self.session['request_token']
        self.oauth.request_access_token(request_token_string, verifier_code , config.access_token_url) 
    def access_resource(self,request_parameters,resource_url):
	return self.oauth.access_resource(request_parameters, resource_url)
