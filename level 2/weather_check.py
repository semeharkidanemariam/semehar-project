phrase = "weather generater"
print(phrase.upper())    
  

def weather_checker():

    print("sorry but only available for 2 country\n "\
          "1. Addis Ababa\n"\
           " 2.London\n" )
    

    choose = input("choose your country:")
    if choose == "1":
        country_name = "Addis Ababa"
        country_temprature =22
    elif choose == "2":
        country_name ="London"
        country_temprature =10
    else:
        print("its not valid yet")
        return 
    print("The temprature in "+ country_name  +  str(country_temprature)  + " clicious")
    if country_temprature > 27:
        print("today's suuny day mak sur to put sunscreen")  
    elif  country_temprature <= 10:
        print("its rainy day make sure to hand an umberella")     
    else:
        print("its th weather njoy you day")

weather_checker()              