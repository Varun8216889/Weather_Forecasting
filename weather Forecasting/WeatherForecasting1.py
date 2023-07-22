from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk , messagebox 
from timezonefinder import TimezoneFinder 
from datetime import *
import requests
import pytz
from PIL import Image , ImageTk


root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#87CEEB")
root.resizable(False,False)

def getWeather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()

    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #weather
    api="https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=646824f2b7b86caffec1d0b16ea77f79"
    json_data=requests.get(api).json()

    #current
    temp=json_data['current']['temp']
    humidity=json_data['current']['humidity']
    pressure=json_data['current']['pressure']
    wind=json_data['current']['wind_speed']
    description=json_data['current']['weather'][0]['description']

    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=(description))

    #1
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']
    photo1=ImageTk.PhotoImage(file=f"{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1

    tempday1= json_data['daily'][0]['temp']['day']
    tempnight1=json_data['daily'][0]['temp']['night']
    day1temp.config(text=f"Day : {tempday1}°C\n Night : {tempnight1}°C")
    
    #2
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']
    img=(Image.open(f"{seconddayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2

    tempday2= json_data['daily'][1]['temp']['day']
    tempnight2=json_data['daily'][1]['temp']['night']
    day2temp.config(text=f"Day:{tempday2}°C\n Night:{tempnight2}°C")
    
    #3
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']
    img=(Image.open(f"{thirddayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo3=ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image=photo3

    tempday3= json_data['daily'][2]['temp']['day']
    tempnight3=json_data['daily'][2]['temp']['night']
    day3temp.config(text=f"Day:{tempday3}°C\n Night:{tempnight3}°C")
    
    #4
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']
    img=(Image.open(f"{fourthdayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo4=ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image=photo4

    tempday4= json_data['daily'][3]['temp']['day']
    tempnight4=json_data['daily'][3]['temp']['night']
    day4temp.config(text=f"Day:{tempday4}°C\n Night:{tempnight4}°C")
    
    #5
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']
    img=(Image.open(f"{fifthdayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo5=ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image=photo5

    tempday5= json_data['daily'][4]['temp']['day']
    tempnight5=json_data['daily'][4]['temp']['night']
    day5temp.config(text=f"Day:{tempday5}°C\n Night:{tempnight5}°C")
    
    #6
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']
    img=(Image.open(f"{sixthdayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo6=ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image=photo6

    tempday6= json_data['daily'][5]['temp']['day']
    tempnight6=json_data['daily'][5]['temp']['night']
    day6temp.config(text=f"Day:{tempday6}°C\n Night:{tempnight6}°C")
    
    #7
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']
    img=(Image.open(f"{seventhdayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo7=ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image=photo7

    tempday7= json_data['daily'][6]['temp']['day']
    tempnight7=json_data['daily'][6]['temp']['night']
    day7temp.config(text=f"Day:{tempday7}°C\n Night:{tempnight7}°C")

    #days
    first=datetime.now()
    day1.config(text=first.strftime("%A"))
    
    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))




#icon
image_icon = PhotoImage(file ="logo1.png")
root.iconphoto(False , image_icon)

Round_box = PhotoImage(file = "rr1.png")
Label(root,image=Round_box,bg = "#87CEEB").place(x=30,y=110)

#label
label1 = Label(root,text="Temperature",font=("Helvetica",11),fg="white",bg="#203243")
label1.place(x=50,y=120)

label2 = Label(root,text="Humidity",font=("Helvetica",11),fg="white",bg="#203243")
label2.place(x=50,y=140)

label3 = Label(root,text="Pressure",font=("Helvetica",11),fg="white",bg="#203243")
label3.place(x=50,y=160)

label4 = Label(root,text="Wind Speed",font=("Helvetica",11),fg="white",bg="#203243")
label4.place(x=50,y=180)

label5 = Label(root,text="Description",font=("Helvetica",11),fg="white",bg="#203243")
label5.place(x=50,y=200)

#search box
Search_image = PhotoImage(file="rr2.png")
myimage =Label(image=Search_image,bg="#87CEEB")
myimage.place(x=270,y=120)

weat_image=PhotoImage(file ="Layer 7.png")
weatherimage = Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=290,y=127)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()

Search_icon=PhotoImage(file="Layer 6.png")
myimage_icon =Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=645,y=125)

#bottom box
frame =Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

#bottom boxes
firstbox=PhotoImage(file="rr3.png")
secondbox=PhotoImage(file="rr4.png")

Label(frame,image=firstbox,bg="#212120").place(x=30,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=300,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=400,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=500,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=600,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=700,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=800,y=30)

#clock (here we will place time)
clock=Label(root,font=("Helvetica",30,'bold'),fg="white",bg="#87CEEB")
clock.place(x=30,y=20)

#timezone
timezone=Label(root,font=("Helvetica",20),fg="white",bg="#87CEEB")
timezone.place(x=700,y=20)


long_lat=Label(root,font=("Helvetica",10),fg="white",bg="#87CEEB")
long_lat.place(x=700,y=50)

#thpwd
t=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t.place(x=150,y=120)

h=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
h.place(x=150,y=140)

p=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
p.place(x=150,y=160)

w=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
w.place(x=150,y=180)

d=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
d.place(x=150,y=200)

#frames

#1
firstframe = Frame(root,width=230,height=132,bg="black")
firstframe.place(x=35,y=315)

day1=Label(firstframe,font="arial 20",bg="black",fg="#fff")
day1.place(x=100,y=5)

firstimage=Label(firstframe,bg="black")
firstimage.place(x=1,y=15)

day1temp=Label(firstframe,bg="black",fg="#57adff",font="arial 15 bold")
day1temp.place(x=100,y=50)

#2
secondframe = Frame(root,width=70,height=115,bg="black")
secondframe.place(x=305,y=325)

day2=Label(secondframe,bg="black",fg="#fff")
day2.place(x=10,y=5)

secondimage=Label(secondframe,bg="black")
secondimage.place(x=7,y=20)

day2temp=Label(secondframe,bg="black",fg="#fff")
day2temp.place(x=1,y=70)

#3
thirdframe = Frame(root,width=70,height=115,bg="black")
thirdframe.place(x=405,y=325)

day3=Label(thirdframe,bg="black",fg="#fff")
day3.place(x=10,y=5)

thirdimage=Label(thirdframe,bg="black")
thirdimage.place(x=7,y=20)

day3temp=Label(thirdframe,bg="black",fg="#fff")
day3temp.place(x=1,y=70)

#4
fourthframe = Frame(root,width=70,height=115,bg="black")
fourthframe.place(x=505,y=325)

day4=Label(fourthframe,bg="black",fg="#fff")
day4.place(x=10,y=5)

fourthimage=Label(fourthframe,bg="black")
fourthimage.place(x=7,y=20)

day4temp=Label(fourthframe,bg="black",fg="#fff")
day4temp.place(x=10,y=70)

#5
fifthframe = Frame(root,width=70,height=115,bg="black")
fifthframe.place(x=605,y=325)

day5=Label(fifthframe,bg="black",fg="#fff")
day5.place(x=10,y=5)

fifthimage=Label(fifthframe,bg="black")
fifthimage.place(x=7,y=20)

day5temp=Label(fifthframe,bg="black",fg="#fff")
day5temp.place(x=1,y=70)

#6
sixthframe = Frame(root,width=70,height=115,bg="black")
sixthframe.place(x=705,y=325)

day6=Label(sixthframe,bg="black",fg="#fff")
day6.place(x=10,y=5)

sixthimage=Label(sixthframe,bg="black")
sixthimage.place(x=7,y=20)

day6temp=Label(sixthframe,bg="black",fg="#fff")
day6temp.place(x=1,y=70)

#7
seventhframe = Frame(root,width=70,height=115,bg="black")
seventhframe.place(x=805,y=325)

day7=Label(seventhframe,bg="black",fg="#fff")
day7.place(x=10,y=5)

seventhimage=Label(seventhframe,bg="black")
seventhimage.place(x=7,y=20)

day7temp=Label(seventhframe,bg="black",fg="#fff")
day7temp.place(x=1,y=70)
