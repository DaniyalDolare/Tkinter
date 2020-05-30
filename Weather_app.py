from tkinter import *
import requests
import json
root = Tk()
root.title("Weather App")
root.geometry("600x100")
#Create Zipcode lookup function
def ziplookup():
    #zip.get()
    #zip_label =Label(root,text=zip.get())
    #zip_label.grid(row=1, column=0, columnspan=2)
    try:
        api_req = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() +"&distance=5&API_KEY=F20F9194-62DD-4130-BDFF-B19E9DD2424A")
        api = json.loads(api_req.content)
        City = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealty for Sensitive Groups":
            weather_color = "#FF9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"
        root.configure(bg=weather_color)


        my_label = Label(root, text=str(City) + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 17),
                         bg=weather_color)
        my_label.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        api = "Error"
#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89101&distance=5&API_KEY=F20F9194-62DD-4130-BDFF-B19E9DD2424A

zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)
zip_btn = Button(root, text="Lookup Zipcode", command=ziplookup)
zip_btn.grid(row=0, column=1, stick=W+E+N+S)


root.mainloop()