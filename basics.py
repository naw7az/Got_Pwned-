import requests
"""requests module allows us to connect to the url, it is like a 
   browser without interface."""

"""sir will talk about API in web dev section, later.
   API stands for Application Programming Interface. An API is a 
   software intermediary that allows two applications to talk to each other."""

url = 'https://api.pwnedpasswords.com/range/' + 'password123'
res = requests.get(url)
print(res)  # response 400 means it is bad request, and something wrong with API(we need 200)

# giving SHA1 hashed of the same password, still insecure
url1 = 'https://api.pwnedpasswords.com/range/' + 'CBFDAC6008F9CAB4083784CBD1874F76618D2A97'
res1 = requests.get(url1)
print(res1)

"""K-anonymity might be described as a ‘hiding in the crowd’ guarantee.
   Our password shares the first 5 character of the hashed format with other passwords in the data base
   so that we will get a list of password starting with this 5 characters and from that we can pick ours
   without telling the API what is our complete password."""

url2 = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res2 = requests.get(url2)
print(res2)  # response 200 is good request