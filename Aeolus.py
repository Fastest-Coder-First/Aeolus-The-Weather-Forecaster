import requests
import json
import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Fun comments about the weather
fun_comments = [
    "Enjoy the sunshine and have a great day!",
    "Don't forget to bring an umbrella, just in case!",
    "Time to grab a hot cup of coffee and enjoy the weather!",
    "Stay cozy and keep warm!",
    "Let the rain wash away all your worries!",
    "It's a perfect day for indoor activities!",
    "Embrace the chilly weather and bundle up!",
    "Stay cool and hydrated in this heat!",
    "The weather is as unpredictable as life itself!",
    "Let the wind blow away all your stress!",
    "Weather forecast: 100% chance of awesomeness!",
    "Don't let the weather rain on your parade!",
    "Make the most of the weather and seize the day!",
    "When it rains, it pours, but don't let that dampen your spirits!",
    "The weather may change, but your positive attitude is always in season!",
    "Thunder or shine, every day is a chance to shine!",
    "No matter the weather, you're always bringing sunshine to the world!",
    "Cloudy days are just opportunities for your inner light to shine brighter!",
    "Remember, storms pass, and rainbows follow!",
    "Just like the weather, life has its ups and downs, but it's all part of the journey!",
    "You're a ray of sunshine, even on the cloudiest of days!",
    "Whether it's hot or cold, your positive energy is always in high demand!"
]

print(f'{Fore.GREEN}Welcome to the Weather App! Based on the OpenWeatherMap API.')
city_input = input("Enter the name of the city/cities: ")
cities = [city.strip() for city in city_input.split(',')]

# API key
api_key = 'dd37eb692bbeaaab504e057fee45f061'

for city in cities:
    url = f'http://api.openweathermap.org/data/2.5/find?q={city}&appid={api_key}'

    # Sending HTTP request
    response = requests.get(url)
    data = response.json()

    if data['cod'] == '404' or len(data['list']) == 0:
        print(f'{Fore.RED}Error: No matching cities found for "{city}"')
    else:
        unique_cities = set()
        cities_data = data['list']
        for city_data in cities_data:
            city_name = city_data['name']
            country = city_data['sys']['country']
            city_info = f'{city_name}, {country}'
            unique_cities.add(city_info)

        if len(unique_cities) == 1:
            selected_city = unique_cities.pop()
        else:
            print(f'{Fore.YELLOW}Multiple cities found for "{city}":')
            for index, city_info in enumerate(unique_cities, start=1):
                print(f'{Fore.CYAN}{index}. {city_info}')

            while True:
                choice = input(f'{Fore.CYAN}Please enter the number corresponding to the desired city: ')
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(unique_cities):
                        selected_city = list(unique_cities)[choice - 1]
                        break
                    else:
                        print(f'{Fore.RED}Invalid choice. Please try again.')
                except ValueError:
                    print(f'{Fore.RED}Invalid choice. Please enter a number.')

        city_name, country = selected_city.split(', ')

        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name},{country}&appid={api_key}'
        weather_response = requests.get(url)
        weather_data = weather_response.json()

        if 'main' not in weather_data:
            print(f'{Fore.RED}Error: Weather data not found for {city_name}, {country}')
        else:
            temperature_kelvin = weather_data['main']['temp']
            temperature_celsius = round(temperature_kelvin - 273.15, 2)
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']

            print(f'\n{Fore.GREEN}Current Weather for {city_name}, {country}:')
            print(f'{Fore.YELLOW}Temperature: {temperature_celsius}°C')
            print(f'{Fore.MAGENTA}Description: {description}')
            print(f'{Fore.CYAN}Humidity: {humidity}%')
            # Additional if-else conditions for specific weather descriptions
            if description == 'clear sky':
                print(f'{Fore.YELLOW}It\'s a clear sky! Go out and enjoy!')
            elif description == 'few clouds':
                print(f'{Fore.YELLOW}It\'s a few clouds! Go out and enjoy!')
            elif description == 'scattered clouds':
                print(f'{Fore.YELLOW}It\'s scattered clouds! Go out and enjoy!')
            elif description == 'broken clouds':
                print(f'{Fore.YELLOW}It\'s broken clouds! Let\'s go for a picnic!')
            elif description == 'shower rain':
                print(f'{Fore.BLUE}It\'s shower rain! Get an umbrella!')
            elif description == 'rain':
                print(f'{Fore.BLUE}It\'s raining! Get a raincoat!')
            elif description == 'thunderstorm':
                print(f'{Fore.RED}It\'s about to thunderstorm! Avoid going out!!')
            elif description == 'snow':
                print(f'{Fore.BLUE}It\'s snowing! Get a hot drink!')
            elif description == 'mist':
                print(f'{Fore.BLUE}It\'s misty! Unable to see the weather!')
            elif description == 'smoke':
                print(f'{Fore.BLUE}It\'s smoky! Avoid going out!!')
            elif description == 'haze':
                print(f'{Fore.BLUE}It\'s hazy! Avoid going out!!')
            elif description == 'dust':
                print(f'{Fore.BLUE}It\'s dusty! My allergies are acting up!!')
            elif description == 'fog':
                print(f'{Fore.BLUE}It\'s foggy! Unable to see!')
            elif description == 'sand':
                print(f'{Fore.BLUE}It\'s sandy! Get a camel!!')
            elif description == 'ash':
                print(f'{Fore.BLUE}It\'s ashy! Avoid going out!!')
            elif description == 'squall':
                print(f'{Fore.BLUE}It\'s squally! What is that?!!')
            elif description == 'tornado':
                print(f'{Fore.RED}It\'s a tornado! Don\'t be blown away!!')
            elif description == 'overcast clouds':
                print(f'{Fore.BLUE}It\'s overcast! Avoid going out!!')
            elif description == 'volcanic ash':
                print(f'{Fore.RED}It\'s volcanic ash! Stay safe!!')
            elif description == 'moderate rain':
                print(f'{Fore.BLUE}It\'s moderate rain! It will be fine, no need for a raincoat!')
            elif description == 'heavy intensity rain':
                print(f'{Fore.RED}It\'s heavy intensity rain! Don\'t go outside!')
            elif description == 'very heavy rain':
                print(f'{Fore.RED}It\'s very heavy rain! Better get a boat!')
            elif description == 'extreme rain':
                print(f'{Fore.RED}It\'s extreme rain! Better get a boat!')
            elif description == 'light rain':
                print(f'{Fore.BLUE}It\'s light rain! Better get wet!')

            

            # Select random fun comment about the weather
            random_comment = random.choice(fun_comments)
            print(f'{Fore.YELLOW}{random_comment}')
