import requests
recr  = requests.get("http://www.spacejam.com/1996")
recr.content
recr.status_code   #it has to show 200



requests.post()     #post is another kind of request
