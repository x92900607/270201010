age=int(input('enter your age:')
bus_ticket=3.0
if age < 6 and age > 60:
  bus_ticket=0
elif age > 6 and age < 18:
    bus_ticket-=bus_ticket*0.5
else:
  bus_ticket=3.0
print (bus_ticket)
