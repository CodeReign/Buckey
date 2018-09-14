numbersTaken = (1,3,12,20,17)

print("These are the numbers that are available")
for n in range(1, 20):
    if n in numbersTaken:
        continue
    print(n)
        
    
    