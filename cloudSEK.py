
import urllib.request
webapp=urllib.request.urlopen('https://www.github.com')

print("status code="+str(webapp.getcode()))

data=webapp.read()
print(data)

