
import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF")

    print("------------------")
    print(weather_data.json())



    # ------------------

    #  def weatherfun():
    #             api_key = 'e58dc3d341f97e5f8debfd63d4046202'

    #             speak("Please enter your city name")
    #             user_location = input("Enter city: ")

    #             weather_data = requests.get(
    #                     f"https://api.openweathermap.org/data/2.5/weather?q={user_location}&units=imperial&APPID={api_key}")

    #             try:
    #                 weather_json = weather_data.json()

    #     # Check if the key 'weather' exists in the JSON response
    #                 if 'weather' in weather_json and len(weather_json['weather']) > 0:
    #                     weather_description = weather_json['weather'][0]['main']
    #                     temperature = round(weather_json['main']['temp'])

    #                     speak(f"The weather in {user_location} is: {weather_description}")
    #                     speak(f"The Temperature in {user_location} is: {temperature}ºF")
    #                 else:
    #                     speak("Sorry, couldn't retrieve weather information for the specified city.")

    #             except ValueError:
    #                 speak("Error: Unable to parse JSON response.")

    #         weatherfun()