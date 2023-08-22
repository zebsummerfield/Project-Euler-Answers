
coins = [0.00, 0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00]
combinations = [[1,0,0,0,0,0,0,0],
                [0,2,0,0,0,0,0,0],
                [0,0,4,0,0,0,0,0],
                [0,0,0,10,0,0,0,0],
                [0,0,0,0,20,0,0,0],
                [0,0,0,0,0,40,0,0],
                [0,0,0,0,0,0,100,0],
                [0,0,0,0,0,0,0,200]]

for count_200 in range(1):
    for count_100 in range(2):
        for count_50 in range(4):
            for count_20 in range(10):
                print(".")
                for count_10 in range(20):
                    for count_5 in range(40):
                        for count_2 in range(100):
                            for count_1 in range(200):
                                if (200*count_200+
                                    100*count_100+
                                    50*count_50+
                                    20*count_20+
                                    10*count_10+
                                    5*count_5+
                                    2*count_2+
                                    1*count_1) == 200:
                                    combination = [count_200,
                                                   count_100,
                                                   count_50,
                                                   count_20,
                                                   count_10,
                                                   count_5,
                                                   count_2,
                                                   count_1]
                                    if combination not in combinations:
                                        combinations.append(combination)
                                    

print(len(combinations))
