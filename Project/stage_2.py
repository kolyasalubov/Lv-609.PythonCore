from bs4 import BeautifulSoup
from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="copart"
)

mycursor = mydb.cursor()
sql_1 = "Truncate iaai"
mycursor.execute(sql_1)
car = 1
print("start at: %s" % datetime.now().time())
#
##
####
#####
# don't forget to change range to +1 last file name

for i in range(1, 230):
    filename = str(i) + ".txt"
    with open(filename) as file:
        contents = file.read()
        soup = BeautifulSoup(contents, 'lxml')
        for item in soup.find_all("div", {"class": "table-cell--data"}):  # each car
            print(item.find_all("div", {"class": "table-cell"})[0].text.strip(),  # year make model
                  # item.find_all("div", {"class" : "table-cell"})[1].find_all("span")[1].text.strip(), # lot
                  #item.find_all("div", {"class": "table-cell"})[1].find_all("li")[1].text.strip(),  # docs
                  # item.find_all("div", {"class": "table-cell"})[1].find_all("li")[3].text.strip(), # damage
                  # item.find_all("div", {"class": "table-cell"})[1].find_all("li")[4].text.strip(), # cause
                  item.find_all("div", {"class": "table-cell"})[2].find_all("li")[0].text.strip(),  # mileage
                  # item.find_all("div", {"class": "table-cell"})[2].find_all("li")[1].text.strip(), # starts / run
                  # item.find_all("div", {"class": "table-cell"})[2].find_all("li")[2].text.strip(), # airbags
                  # item.find_all("div", {"class": "table-cell"})[2].find_all("li")[3].text.strip(), # key available
                  # item.find_all("div", {"class": "table-cell"})[3].find_all("li")[0].text.strip(), # engine
                  # item.find_all("div", {"class": "table-cell"})[3].find_all("li")[1].text.strip(), # fuel
                  # item.find_all("div", {"class": "table-cell"})[3].find_all("span")[4].text.strip(), # vin
                  # item.find_all("div", {"class": "table-cell"})[3].find_all("li")[2].text.strip(), # cylind
                  # item.find_all("div", {"class": "table-cell"})[4].find_all("li")[0].text.strip(),  # location
                  # item.find_all("div", {"class": "table-cell"})[5].find_all("li")[0].text.strip(),  # date
                  # item.find_all("div", {"class": "table-cell"})[5].find_all("li")[2].text.strip(), # buynow
                  sep="   ")

            sql = "INSERT INTO iaai (`Iaai_id`, Year, Make, Model, Engine, Fuel, `Run&drive`, Airbags, `Key`," \
                  "Damage, Buynow, Cause, Location, `Sale_doc`, `Date`, Odometer, VIN) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            try:
                eng = float(item.find_all("div", {"class": "table-cell"})[3].find_all("li")[0].text.strip()[:3])
            except:
                eng = 0
            try:
                odo = int(
                    item.find_all("div", {"class": "table-cell"})[2].find_all("li")[0].text.split("mi")[0].replace(
                        ",", "").strip())
            except:
                odo = 0
            try:
                buy = int(item.find_all("div", {"class": "table-cell"})[5].find_all("li")[2].text.strip().split("$")[
                              1].replace(",", ""))
            except:
                buy = 1000000
            val = (item.find_all("div", {"class": "table-cell"})[1].find_all("span")[1].text.strip(),  # lot
                   item.find_all("div", {"class": "table-cell"})[0].text.strip().split()[0],  # year
                   item.find_all("div", {"class": "table-cell"})[0].text.strip().split()[1],  # make
                   item.find_all("div", {"class": "table-cell"})[0].text.strip().split(" ", 2)[2],  # model
                   eng,
                   item.find_all("div", {"class": "table-cell"})[3].find_all("li")[1].text.strip(),
                   item.find_all("div", {"class": "table-cell"})[2].find_all("li")[1].text.strip(),
                   item.find_all("div", {"class": "table-cell"})[2].find_all("li")[2].text.strip(),
                   item.find_all("div", {"class": "table-cell"})[2].find_all("li")[3].text.strip(),
                   item.find_all("div", {"class": "table-cell"})[1].find_all("li")[3].text.strip(),
                   buy,
                   item.find_all("div", {"class": "table-cell"})[1].find_all("li")[4].text.strip(),
                   item.find_all("div", {"class": "table-cell"})[4].find_all("li")[0].text.strip(),
                   item.find_all("div", {"class": "table-cell"})[1].find_all("li")[1].text.strip(),
                   item.find_all("div", {"class": "table-cell"})[5].find_all("li")[0].text.strip(),
                   odo,
                   item.find_all("div", {"class": "table-cell"})[3].find_all("span")[4].text.strip(),
                   )
            mycursor.execute(sql, val)
            mydb.commit()


print("end at: %s" % datetime.now().time())