#Question 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
for i in range(600851474142,29,-1):
    if 600851474143%i == 0:
        largest_factor = i
        break
print(largest_factor) 
