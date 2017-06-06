import random

first_names = ["Miklós", "Tamás", "Dániel", "Mateusz", "Attila", "Pál", "Sándor", "Prezmek", "John", "Tim", "Matthew",
               "Andy", "Giancarlo"]

last_names=["Beöthy", "Tompa", "Salamon", "Ostafil", "Molnár", "Monoczki", "Szodoray", "Ciacka", "Carrey", "Obama", "Lebron", "Hamilton", "Fisichella"]
city_list=["Budapest","Miskolc","Krakow","Barcelona","New York"]


mail_list=["gmail.com","citromail.hu","freemail.hu"]

sqlstring = ""
sqlstring+="BEGIN TRANSACTION;\n"
for i in range(0,100000):
    first_name=random.choice(first_names)
    last_name=random.choice(last_names)
    city=random.choice(city_list)
    birth=random.randint(1960,1995)
    email=first_name  + "@"+ random.choice(mail_list)
    phone_number= "+" + str(random.randint(1000000000,9999999999))
    level=random.randint(1,10)
    record='''INSERT INTO "mentor_candidates" VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s');\n''' %(first_name,last_name,phone_number,email,city,level,birth)
    sqlstring+=record
sqlstring+="COMMIT TRANSACTION;"
with open("random.txt","w") as f:
    f.write(sqlstring)