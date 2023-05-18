import random
from tkinter import *
from tkinter import messagebox

import requests
from decouple import config

cities = ['Abidjan', 'Abu Dhabi', 'Abuja', 'Accra', 'Addis Ababa', 'Ahmedabad', 'Aleppo', 'Alexandria', 'Algiers',
          'Almaty', 'Amman', 'Amsterdam', 'Anchorage', 'Andorra la Vella', 'Ankara', 'Antananarivo', 'Apia', 'Arnold',
          'Ashgabat', 'Asmara', 'Asuncion', 'Athens', 'Auckland', 'Avarua', 'Baghdad', 'Baku', 'Bamako', 'Banda Aceh',
          'Bandar Seri Begawan', 'Bandung', 'Bangkok', 'Bangui', 'Banjul', 'Barcelona', 'Barranquilla', 'Basrah',
          'Basse-Terre', 'Basseterre', 'Beijing', 'Beirut', 'Bekasi', 'Belem', 'Belgrade', 'Belmopan', 'Belo Horizonte',
          'Bengaluru', 'Berlin', 'Bern', 'Bishkek', 'Bissau', 'Bogota', 'Brasilia', 'Bratislava', 'Brazzaville',
          'Bridgetown', 'Brisbane', 'Brussels', 'Bucharest', 'Budapest', 'Buenos Aires', 'Bujumbura', 'Bursa', 'Busan',
          'Cairo', 'Cali', 'Caloocan', 'Camayenne', 'Canberra', 'Cape Town', 'Caracas', 'Casablanca', 'Castries',
          'Cayenne',
          'Charlotte Amalie', 'Chengdu', 'Chennai', 'Chicago', 'Chisinau', 'Chittagong', 'Chongqing', 'Colombo',
          'Conakry',
          'Copenhagen', 'Cordoba', 'Curitiba', 'Daegu', 'Daejeon', 'Dakar', 'Dallas', 'Damascus', 'Dar es Salaam',
          'Delhi',
          'Denver', 'Dhaka', 'Dili', 'Djibouti', 'Dodoma', 'Doha', 'Dongguan', 'Douala', 'Douglas', 'Dubai', 'Dublin',
          'Durban', 'Dushanbe', 'Faisalabad', 'Fort-de-France', 'Fortaleza', 'Freetown', 'Fukuoka', 'Funafuti',
          'Gaborone',
          'George Town', 'Georgetown', 'Gibraltar', 'Gitega', 'Giza', 'Guadalajara', 'Guangzhou', 'Guatemala City',
          'Guayaquil', 'Gujranwala', 'Gustavia', 'Gwangju', 'Hamburg', 'Hanoi', 'Harare', 'Havana', 'Helsinki',
          'Ho Chi Minh City', 'Hong Kong', 'Honiara', 'Honolulu', 'Houston', 'Hyderabad', 'Hyderabad', 'Ibadan',
          'Incheon', 'Isfahan',
          'Islamabad', 'Istanbul', 'Izmir', 'Jaipur', 'Jakarta', 'Jeddah', 'Jerusalem', 'Johannesburg', 'Juarez',
          'Juba',
          'Kabul', 'Kaduna', 'Kampala', 'Kano', 'Kanpur', 'Kaohsiung', 'Karachi', 'Karaj', 'Kathmandu', 'Kawasaki',
          'Kharkiv', 'Khartoum', 'Khulna', 'Kigali', 'Kingsburg', 'Kingston', 'Kingstown', 'Kinshasa', 'Kobe',
          'Kolkata',
          'Kota Bharu', 'Kowloon', 'Kuala Lumpur', 'Kumasi', 'Kuwait', 'Kyiv', 'Kyoto', 'La Paz', 'Lagos', 'Lahore',
          'Libreville', 'Lilongwe', 'Lima', 'Lisbon', 'Ljubljana', 'Lome', 'London', 'Los Angeles', 'Luanda',
          'Lubumbashi',
          'Lusaka', 'Luxembourg', 'Macau', 'Madrid', 'Majuro', 'Makassar', 'Malabo', 'Male', 'Mamoudzou', 'Managua',
          'Manama', 'Manaus', 'Manila', 'Maputo', 'Maracaibo', 'Maracay', 'Mariehamn', 'Marigot', 'Maseru', 'Mashhad',
          'Mbabane', 'Mecca', 'Medan', 'Medellin', 'Medina', 'Melbourne', 'Mexico City', 'Miami', 'Minsk', 'Mogadishu',
          'Monaco', 'Monrovia', 'Montevideo', 'Montreal', 'Moroni', 'Moscow', 'Mosul', 'Multan', 'Mumbai', 'Muscat',
          "N'Djamena", 'Nagoya', 'Nairobi', 'Nanchong', 'Nanjing', 'Nassau', 'Nay Pyi Taw', 'New York', 'Niamey',
          'Nicosia',
          'Nouakchott', 'Noumea', 'Novosibirsk', "Nuku'alofa", 'Nur-Sultan', 'Nuuk', 'Oranjestad', 'Osaka', 'Oslo',
          'Ottawa',
          'Ouagadougou', 'Pago Pago', 'Palembang', 'Palo Alto', 'Panama', 'Papeete', 'Paramaribo', 'Paris', 'Perth',
          'Philadelphia', 'Phnom Penh', 'Phoenix', 'Podgorica', 'Port Louis', 'Port Moresby', 'Port of Spain',
          'Port-Vila',
          'Port-au-Prince', 'Porto Alegre', 'Porto-Novo', 'Prague', 'Praia', 'Pretoria', 'Pristina', 'Puebla', 'Pune',
          'Pyongyang', 'Quezon City', 'Quito', 'Rabat', 'Rawalpindi', 'Recife', 'Reykjavik', 'Riga', 'Rio de Janeiro',
          'Riyadh', 'Road Town', 'Rome', 'Roseau', "Saint George's", 'Saint Helier', "Saint John's", 'Saint Peter Port',
          'Saint Petersburg', 'Saint-Denis', 'Saint-Pierre', 'Saipan', 'Salvador', 'San Antonio', 'San Diego',
          'San Francisco', 'San Jose', 'San Juan', 'San Marino', 'San Salvador', 'Sanaa', 'Santa Cruz de la Sierra',
          'Santiago', 'Santo Domingo', 'Sao Paulo', 'Sao Tome', 'Sapporo', 'Sarajevo', 'Seattle', 'Semarang', 'Seoul',
          'Shanghai', 'Sharjah', 'Shenzhen', 'Singapore', 'Skopje', 'Sofia', 'South Tangerang', 'Soweto', 'Stockholm',
          'Sucre', 'Surabaya', 'Surat', 'Suva', 'Sydney', 'Tabriz', 'Taipei', 'Tallinn', 'Tangerang', 'Tarawa',
          'Tashkent',
          'Tbilisi', 'Tegucigalpa', 'Tehran', 'Tel Aviv', 'Thimphu', 'Tianjin', 'Tijuana', 'Tirana', 'Tokyo', 'Toronto',
          'Torshavn', 'Tripoli', 'Tunis', 'Ulan Bator', 'Vaduz', 'Valencia', 'Valletta', 'Vancouver', 'Victoria',
          'Vienna',
          'Vientiane', 'Vilnius', 'Warsaw', 'Washington', 'Wellington', 'Willemstad', 'Windhoek', 'Wuhan', "Xi'an",
          'Yamoussoukro', 'Yangon', 'Yaounde', 'Yekaterinburg', 'Yerevan', 'Yokohama', 'Zagreb']

root = Tk()
api_key = config("API_KEY")
all_countries = {}
coldest_cities = {}
avg_temp = []

root.geometry("600x650")
root.config(bg='#C5E2F0')
root.title("Weather App")
font = ("MS Serif", 14)


def generate_data(idx):
    nums = random.sample(range(371), 5)
    data = {}

    url_city = f"http://api.openweathermap.org/geo/1.0/direct?q={cities[nums[idx]]}&limit=5&appid={api_key}"
    response = requests.get(url_city)

    data["name"] = response.json()[0]["name"]

    url_forecast = f"https://api.openweathermap.org/data/2.5/weather?lat={response.json()[0]['lat']}&lon={response.json()[0]['lon']}&appid={api_key}"
    forecast_data = requests.get(url_forecast)

    data["weather"] = forecast_data.json()["weather"][0]["main"]
    data["temp"] = int(forecast_data.json()["main"]["temp"] - 273.15)
    data["humidity"] = forecast_data.json()["main"]["humidity"]

    return data


def get_coldest_cities():
    sorted_dict = sorted(coldest_cities.items(), key=lambda x: x[1])

    return f"Coldest city: {sorted_dict[0][0]}, Temperature: {sorted_dict[0][1]}°C"


def get_average_temp():
    return f"Average Temperature: {sum(avg_temp) / len(avg_temp)}°C"


def show_error():
    return messagebox.showerror('Error', 'Error: Invalid city name, please try again')


def submit_output():
    city_name = entry.get()

    if city_name:
        # Forget existing if any
        TextAreaCities.place_forget()
        TextAreaAvgTemp.place_forget()
        TextAreaColdestCity.place_forget()

        url_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api_key}"
        response = requests.get(url_city)

        if response.json():
            TextAreaSingleOutput.place(relx=0.51, rely=.52, anchor=CENTER)
            TextAreaSingleOutput.configure(state=NORMAL)
            data = {"name": response.json()[0]["name"]}

            url_forecast = f"https://api.openweathermap.org/data/2.5/weather?lat={response.json()[0]['lat']}&lon={response.json()[0]['lon']}&appid={api_key}"
            forecast_data = requests.get(url_forecast)

            data["weather"] = forecast_data.json()["weather"][0]["main"]
            data["temp"] = int(forecast_data.json()["main"]["temp"] - 273.15)
            data["humidity"] = forecast_data.json()["main"]["humidity"]
            converted_json_data = f"City name: {data['name']}, Weather: {data['weather']}, Temperature: {data['temp']}°C, " \
                                  f"Humidity: {data['humidity']}%"

            TextAreaSingleOutput.delete(1.0, END)
            TextAreaSingleOutput.insert(END, converted_json_data)
            TextAreaSingleOutput.configure(state=DISABLED)
        else:
            show_error()
    else:
        show_error()


def generate_output():
    TextAreaSingleOutput.place_forget()
    TextAreaCities.place(relx=0.51, rely=.52, anchor=CENTER)
    TextAreaCities.configure(state=NORMAL)
    TextAreaCities.delete(1.0, END)

    for idx in range(5):
        data = generate_data(idx)
        name, weather, temp, humidity = data.values()
        coldest_cities[name] = temp
        avg_temp.append(temp)

        TextAreaCities.insert(END,
                              f"City: {name}, Weather: {weather}, Temperature: {temp}°C, Humidity: {humidity}%\n\n")

    TextAreaCities.configure(state=DISABLED)

    # Coldest city
    TextAreaColdestCity.place(relx=0.51, rely=.72, anchor=CENTER)
    TextAreaColdestCity.configure(state=NORMAL)
    TextAreaColdestCity.delete(1.0, END)
    TextAreaColdestCity.insert(END, str(get_coldest_cities()))
    coldest_cities.clear()
    TextAreaColdestCity.configure(state=DISABLED)

    # Average temperature
    TextAreaAvgTemp.place(relx=0.51, rely=.80, anchor=CENTER)
    TextAreaAvgTemp.configure(state=NORMAL)
    TextAreaAvgTemp.delete(1.0, END)
    TextAreaAvgTemp.insert(END, str(get_average_temp()))
    avg_temp.clear()
    TextAreaAvgTemp.configure(state=DISABLED)


Label(root, text="Weather App", font=("MS Serif bold", 42), bg="#C5E2F0", fg="black").place(relx=.5, rely=.1,
                                                                                            anchor=CENTER)

entry = Entry(root, width=39, borderwidth=5)
entry.place(relx=.5, rely=.2, anchor=CENTER)

Button(root, text="Submit", padx=16, pady=12, command=submit_output).place(relx=.37, rely=.3, anchor=CENTER)
Button(root, text="Generate", padx=16, pady=12, command=generate_output).place(relx=.65, rely=.3, anchor=CENTER)

TextAreaCities = Text(root, height=10, width=55, borderwidth=4)
TextAreaCities.configure(font=font, state=DISABLED)

TextAreaColdestCity = Text(root, height=1.1, width=55, borderwidth=4)
TextAreaColdestCity.configure(font=font, state=DISABLED)

TextAreaAvgTemp = Text(root, height=1.1, width=55, borderwidth=4)
TextAreaAvgTemp.configure(font=font, state=DISABLED)

TextAreaSingleOutput = Text(root, height=1.1, width=55, borderwidth=4)
TextAreaSingleOutput.configure(font=font, state=DISABLED)

root.mainloop()
