print(2) #saves some time in arithmetic for higher numbers
for n in range (3,10000): #Sets the number to be tested
        prime = True
        i = 2
        while (n > i): #needs or prime == false // find a way to test sqrt(n) > i
                if (n % i == 0):
                        prime = False
                i = i + 1
        if (prime == True): 
                print (n)
