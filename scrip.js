alert ("ИДИ ОТСЮДА РАЗБИЙНИК")
a=5
b=10
alert(a*b)

console.log("Привет: ",a*b)

function myfunction() 
{
n = document.getElementById("in_name").value;
a = document.getElementById("in_age").value;
response = "Имя:" + n + "Возраст" + a
alert(response)
t = document.getElementById("mytable")
var row = t.insertRow(4);
var c_name = row.insertCell(0);
var c_photo = row.insertCell(1);
var c_task = row.insertCell(2);
c_name.innerHTML = n;
c_photo.innerHTML = '<img src="./meepo.jpg">'
c_task.innerHTML = "Сотрудник"
}

