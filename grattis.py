import facebook
import urllib
import subprocess
import warnings
import os

FACEBOOK_APP_ID     = os.environ['app_id']
FACEBOOK_APP_SECRET = os.environ['app_secret']
FACEBOOK_PROFILE_ID = os.environ['user']

oauth_args = dict(client_id     = FACEBOOK_APP_ID,
                  client_secret = FACEBOOK_APP_SECRET,
                  grant_type    = 'client_credentials')
oauth_curl_cmd = ['curl',
                  'https://graph.facebook.com/oauth/access_token?' + urllib.parse.urlencode(oauth_args)]
oauth_response = subprocess.Popen(oauth_curl_cmd,
                                  stdout = subprocess.PIPE,
                                  stderr = subprocess.PIPE).communicate()[0]

try:
  oauth_access_token = urllib.parse.parse_qs(str(oauth_response)[2:-1])['access_token'][0]
except KeyError:
  print('Unable to grab an access token!')
  exit()
facebook_graph = facebook.GraphAPI(oauth_access_token)


try:
    fb_response = facebook_graph.put_wall_post('Hello from Bot', \
                                               profile_id = FACEBOOK_PROFILE_ID)
    print(fb_response)
except facebook.GraphAPIError as e:
    print('Something went wrong:', e.type, e.message)
