# import requests
# import os
# from pprint import pprint
# # from dotenv import load_dotenv

# # load_dotenv()
# api=os.environ.get('api')

# url = ('https://newsapi.org/v2/everything?'
#        'q=Apple&'
#        'from=2024-02-03&'
#        'sortBy=popularity&'
#        'apiKey=bb31751c01cf4b3bbd6709d79ee51d38')
# response = requests.get(url)
# # print r.json
# print(response.json())
# pprint(response.text)



# ---------------------------------------------

# data = response.json()
# title = data.get('articles')
# print(title)



# from newsapi import NewsApiClient

# # Init
# newsapi = NewsApiClient(api_key='bb31751c01cf4b3bbd6709d79ee51d38')

# # /v2/top-headlines
# # top_headlines = newsapi.get_top_headlines(q='bitcoin',
# #                                           sources='bbc-news,the-verge',
# #                                           category='business',
# #                                           language='en',
# #                                           country='us')

# # /v2/everything
# # all_articles = newsapi.get_everything(q='bitcoin',
# #                                       sources='bbc-news,the-verge',
# #                                       domains='bbc.co.uk,techcrunch.com',
# #                                       from_param='2017-12-01',
# #                                       to='2017-12-12',
# #                                       language='en',
# #                                       sort_by='relevancy',
# #                                       page=2)

# # /v2/top-headlines/sources
# sources = newsapi.get_sources()



# ----------------------------------
# chatgpt 
# import requests
# from pprint import pprint
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Load your News API key from the environment variable
# api_key = os.environ.get('api_key')

# # Specify the News API endpoint for the "everything" endpoint
# url = 'https://newsapi.org/v2/everything'

# # Specify the parameters for your request (you can customize these)
# params = {
#     'q': 'Python',         # Query term
#     'sortBy': 'popularity', # Sort articles by popularity
#     'apiKey': api_key       # Your News API key
# }

# # Make the request to the News API
# response = requests.get(url, params=params)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()

#     # Get the articles from the response
#     articles = data.get('articles')

#     # Print the articles or perform further processing
#     pprint(articles)
# else:
#     print(f"Error: {response.status_code} - {response.text}")



# --------------------------------


 def news():
                # # select 
                # # api_key ='bb31751c01cf4b3bbd6709d79ee51d38'
                # # base_url= "https://newsapi.org/v2/"
                # # pageSize = 100
                # # country = "us"
                # # category = "general"
                # api_key = os.environ.get('api_key')
                # url = 'https://newsapi.org/v2/everything'
                # params = {
                #     'q': 'Python',         # Query term
                #     'sortBy': 'popularity', # Sort articles by popularity
                #     'apiKey': api_key       # Your News API key
                # }

                # response = requests.get(url, params=params)
                # if response.status_code == 200:
                #     data = response.json()
                #     articles = data.get('articles')
                #     title = data.get('title')
                #     content = data.get('content')
                #     publish = data.get('publishedAt')
                #     speak(title)
                    
                # else:
                #     print(f"Error:{response.status_code}-{response.text}")

                # # url = f"{base_url}top-headlines?country={country}&category={category}&pageSize={pageSize}&apiKey={api_key}"
                # # url = f"{base_url}top-headlines?country={country}&category={category}&pageSize={pageSize}&apiKey={api_key}"
                # # url = f"{base_url}top-headlines?country={country}&category={category}&pageSize={pageSize}&apiKey={api_key}"
                # # url = f"{base_url}top-headlines?country={country}&category={category}&pageSize={pageSize}&apiKey={api_key}"
                # # url = f"{base_url}top-headlines?country={country}&category={category}&pageSize={pageSize}&apiKey={api_key}"
                # # url = f"{base_url}top-headlines?country={country}&category={category}&pageSize={pageSize}&apiKey={api_key}"
                # # url = f"{base_url}top-headlines?country={country}&category={category}&pageSize={pageSize}&apiKey={api_key}"
                # # url = f"{base_url}top-headlines?country={country}&category={category}&pageSize={pageSize}&apiKey={api_key}"
                # # url = f"{base_url}top-headlines?country={country}&category={category}&pageSize={pageSize}&apiKey={api_key}"
                # # url = f"{base_url}top-headlines?country={country}&category={category}&pageSize={pageSize}&apiKey={api_key}"
                # # url = f"{base_url}top-headlines?country={country}&category={category}&pageSize={pageSize}&apiKey={api_key}"                
                
                # 
                api_key = os.environ.get('api_key')  # Correct the variable name

                # Check if the API key is present
                if api_key is None:
                    raise ValueError("NEWS_API_KEY is not set in the environment variables")
                
                # Specify the News API endpoint for the "everything" endpoint
                url = 'https://newsapi.org/v2/everything'
                
                # Specify the parameters for your request (you can customize these)
                params = {
                    'q': 'Python',         # Query term
                    'sortBy': 'popularity', # Sort articles by popularity
                    'apiKey': api_key       # Your News API key
                }
                
                # Make the request to the News API
                response = requests.get(url, params=params)
                
                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Parse the JSON response
                    data = response.json()
                
                    # Get the articles from the response
                    articles = data.get('articles')
                    # title = data.get('title')
                    # title = data.get
                
                    # Print the articles or perform further processing
                    # pprint(articles)
                    # speak(title)
                    for title in articles:
                        speak(title['title'])
                else:
                    print(f"Error: {response.status_code} - {response.text}")
            news()