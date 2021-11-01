# Python program to print
# median of elements
import csv

with open(r'C:\Users\bhuvi\Google Drive\WHJr\Python\Class 104 - Mean, Median, Mode\height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
# removing the list of titles using pop
file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)

n = len(new_data)
new_data.sort()

if n % 2 == 0:
	med1 = float(new_data[n//2])
	med2 = float(new_data[(n//2)+ 1])
	median = (med1 + med2)/2
else:
	median = new_data[round(n/2)]

print("Median is: " + str(median))
