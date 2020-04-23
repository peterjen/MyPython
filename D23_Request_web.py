import requests
# https://www.youtube.com/watch?v=tb8gHvYlCFs&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=23
# http://httpbin.org/

r = requests.get('https://xkcd.com/353/')
#print(r.text)   # get html content in JSON response

r = requests.get('https://imgs.xkcd.com/comics/python.png')
#print(r.content)
# with open('test.png','wb') as wf:
#     wf.write(r.content)
# print(r.status_code)
# print(r.ok)
# print(r.headers)


payload = {'page':2,'count':25}
# https://httpbin.org/get?page=2&count=25
r = requests.get('https://httpbin.org/get',params=payload) 
#print(r.url)
#print(r.text)

payload = {'username':'peter','password':'password123'}
r = requests.post('https://httpbin.org/post',data=payload) 
print(r.url)
r_dict = r.json()  # Return Python Dictionary from Json response
print(r_dict['form']) # {'password': 'password123', 'username': 'peter'}








