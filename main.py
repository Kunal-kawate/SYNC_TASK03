import bitly_api
 
API_USER = "username"
API_KEY = "API_Key"
bitly = bitly_api.Connection(API_USER, API_KEY)

url=input("Enter your URL here: ")
response = bitly.shorten(url)
 
# Now let us print the Bitly URL
print(response)