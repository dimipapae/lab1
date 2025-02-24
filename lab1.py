import requests  # εισαγωγή της βιβλιοθήκης
import datetime

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break
'''
url = 'http://python.org/'  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    html = response.text
    more(html)
'''
# 1. παιρνει url απο τον χρηστη
url=input("Give url:\t")

if not url.startswith('https://'):
    url='https://' + url

print(url)

# 2.Πραγματοποιηση αιτηματος http request
with requests.get(url) as response:
    # 3. headers 
    headers=response.headers
    for key in headers:
        print(f"{key}:{headers[key]}")
    
    print(f"Software of the Server: {response.headers.get('Server')}")

    # 4. Πληροφοριες για την ιστοσελιδα
    if "set-cookie" in headers.keys():
        cookies = response.cookies
        for cookie in cookies:
            print(f"\nThe site uses cookie.\nName: {cookie.name}\nValue: {cookie.value}\nExpiration Date: {datetime.datetime.fromtimestamp(float(cookie.expires)) if cookie.expires is not None else 'Does Not Expire'}")        
    else:
        print('\nThe site does not use cookies')
