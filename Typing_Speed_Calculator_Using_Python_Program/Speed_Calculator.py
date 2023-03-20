from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error +1
        except:
            error = error +1

    return error


def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay,2)
    speed = len(userinput)/time_r
    return round(speed)
if __name__== '__main__':
    while True:
        check = input("Ready to test : yes/no:")
        if check == "yes":
            test = ["Cricket is the national sport of England","The origin of cricket is said to be in the colonial period",
                "Gully Cricket trend is often seen in streets across India","Like other sports, Cricket also contains some time duration"]
            test_1 = r.choice(test)
            print("***** tying speed *****")
            print(test_1)
            print()
            print()
            time_1=time()
            user_test = input("Enter sentence : ")
            time_2=time()

            print('Speed : ',speed_time(time_1,time_2,user_test),"w/sec")
            print('Error:',mistake(test_1,user_test))
        elif check == "no":
            print("Thank You ")
        else:
            print("Wrong input")