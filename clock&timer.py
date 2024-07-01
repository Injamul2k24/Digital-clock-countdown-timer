import time
from playsound import playsound
def userChoice(user_input):
    if user_input == "1":
        digitalClock()
    elif user_input == "2":
        second =int(input("Enter the number of second to countdown:"))
        countdowntimer(second)
    else:
        print("Invalid Choice")
    
    
def digitalClock():
    while True:
        current_time = time.strftime("%H:%M:%S",time.localtime())
        print("\r Digital Clock: "+current_time,end='')
        time.sleep(1)
       
        
    
def countdowntimer(second):
    print("Countdown Timer startrd!")
    for i in range(second, -1, -1):
        print("\rTime remaining :  "+ str(i),end ='')
        time.sleep(1)
    playsound("music.mp3")
    print("\n Time's up!")
print("\n")


while True:
        user_input = input("""                  
        Choose an option(1 or 2):
                           1.Digital Clock   
                           2.Countdown Timer 
                           \n""")
        userChoice(user_input)












