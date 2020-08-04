#!/usr/bin/env python3

def to_seconds(hours, minutes, seconds):
	return hours*3600+minutes*60+seconds

print("Üdvözöllek az időszámolóban.")

cont = "i"
while(cont.lower() == "i"): 
	hours = int(input("Add meg az órák számát: "))
	minutes = int(input("Add meg a percek számát: "))
	seconds = int(input("Add meg a másodpercek számát: "))

	print("A megadott idő összege {} másodperc.".format(to_seconds(hours,minutes, seconds)))
	print()

	cont = input("Szeretnél még egyet számolni? Ha igen, nyomd meg az i -t.")

print("Viszlát!")
