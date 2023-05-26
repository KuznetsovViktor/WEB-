from flask import Flask, render_template,request
from json import dumps as jsonstring

app = Flask(__name__)

class Driver(object):
    def __init__(self, name, surname, salary, experience,image):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.experience = experience
        self.image = image
        
    def __str__(self, name,drivers, salary):
        return("Имя: ",name,
                " Зарплата:",salary,
                " Стаж:",experience,
                " картинка:", self.image)
                

class Autopark(object):
    def __init__(self, name, drivers, foundation):
        self.name = name
        self.drivers = drivers
        self.foundation = foundation

    def __str__(self, name, drivers, foundation):
        return("Название: ",name,
                " Количество водителей:",drivers,
                " Год основания:",foundation)

driver_Popov = Driver("Петр","Попов",30000,15,"quin.jpg")
driver_Ivanov = Driver("Иван","Иванов",50000,25,"crip1.jpg")
driver_Smirnov = Driver("Сергей","Смирнов",150000,40,"crip2.jpg")

drivers = [driver_Popov,driver_Ivanov,driver_Smirnov]

autopark_Uber = Autopark("Uber",drivers,2000)

@app.route("/")
def hello_world():
    return render_template('index.html',Autopark = autopark_Uber)

@app.route("/new_driver")
def adding():
    name = request.args.get('name')
    surname = request.args.get('surname')
    salary = request.args.get('salary')
    experience = request.args.get('experience')
    new_driver = Driver(name, surname, salary, experience,"lanay.jpg")
    autopark_Uber.drivers.append(new_driver)
    return "Добавил"