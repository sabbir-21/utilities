
#score = [70, 90, 60, 500, 50, 25, 65, 100]


def maximum(score): #parameter
    maximum = score[0]

    for number in score:
        if number>maximum:
            maximum = number
    print(f"Large number is {maximum}")
    
maximum([70, 90, 60, 500, 50, 25, 65, 100]) #Argument






