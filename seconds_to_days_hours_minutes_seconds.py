seconds = int(input("seconds "))

days = seconds //86400
hours = (seconds%86400) // 3600
minutes = (seconds%3600) // 60
seconds = seconds%60

print(days, hours, minutes, seconds, sep=":")