
def recurring_cycle(d):
    
    decimal = ''
    recur = False
    dividend = 10
    
    while not recur:
        if dividend < d:
            decimal += "0"
            dividend *= 10

            
        else:
            decimal += str(int(dividend/d))
            dividend = (dividend % d) * 10
            
            if dividend == 0:
                return ""

            for i in range(int(len(decimal)/3)):
                for j in range(i+1, int(len(decimal)/3)):
                    didgits_to_check = decimal[i:j+1]

                    if (didgits_to_check ==
                        decimal[j+1:j+1+len(didgits_to_check)] and
                        didgits_to_check ==
                        decimal[j+1+len(didgits_to_check):j+1+2*len(didgits_to_check)] and
                        didgits_to_check != ''):
                        return didgits_to_check


recur_length = [0]
for i in range(1,1000):
    print(i)
    recur_length.append(len(recurring_cycle(i)))
    
longest_cycle = recur_length.index(max(recur_length))
print(recur_length)
print(longest_cycle)

                    
    
