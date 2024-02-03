from apiip import apiip

api_client = apiip('d85412f9-d2b1-428c-93e6-d14c227e43d4')

info = api_client.get_location()

print(info)