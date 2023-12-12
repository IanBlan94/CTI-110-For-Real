import matplotlib.pyplot as plt
import turtle 12

'''print("How many pokeman have you caught in the past three days?")
print ("day 1:", end="")
day1 = int(input())

print ("day 2:", end="")
day2 = int(input())

print ("day 3:", end="")
day3 = int(input())

# put the data in a list

data = [day1, day2, day3]
# TODO: Graph the real data

total = sum(data)
print("The total pokemon caught was " , total)
max = max(data)
print("The maximum amount of pokemon caught between the three days is ", max)
min = min(data)
print("The minimum amount of pokemon caught between the three days is ", min)
average = total / data'''


data = []
num_days = turtle.numinput("input", "How many days did you go out? ")
num_days = int(num_days)
for day in range(num_days):
  #print("Day:", day, "", end="")
  
  label = "day #" + str(day)
  today = turtle.numinput(label, "How many pokemans were caught?")
  data.append(today)
print()

#total = sum(data)

total = 0 
for num in data:
 total += num

print("The total amount of pokemans caught was ", total)

max = max(data)
print("The max amount of pokemans caught on any day was ", max)

min = min(data)
print("The minimum amount of pokemans caught on any day was ", min)

average = total // num_days 
print("The average of all days is ", average) 

fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title("Pokemans Data")
plt.xlabel('day #')
plt.ylabel('pokemans collected')
plt.show()



