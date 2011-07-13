from django.conf.urls.defaults import patterns, include, url
"""
	django에서 사용하는 url,handler 정의 모듈입니다.
	사용자 환경에 맞춰 다시 설정하셔야합니다.
"""
urlpatterns = patterns('',
    # Examples:
    url(r'oauth/main',r'django_.oauth_.views.index'),
    url(r'oauth/request_token',r'django_.oauth_.views.request_token'),
    url(r'oauth/callback',r'django_.oauth_.views.callback'),
    url(r'oauth/access_resource',r'django_.oauth_.views.access_resource')
)
