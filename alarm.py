import time
import random
import winsound
alarm_time = input("Set alarm time (HH:MM in 24-hour format): ")

print("Alarm set for", alarm_time)

while True:
    current_time = time.strftime("%H:%M")
    print("Current time:", current_time)
    if current_time == alarm_time:
        print("\n ALARM RINGING!!! ")
        winsound.PlaySound('SystemAsterisk',winsound.SND_ASYNC | winsound.SND_LOOP)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2

        while True:
            try:
                user_answer = int(input(f"Solve to stop alarm: {num1} + {num2} = "))
                
                if user_answer == correct_answer:
                    print(" Correct! Alarm stopped.")
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    break
                    
                else:
                    print("Wrong answer! Try again.")
            except ValueError:
                print("Enter a valid number!")

        break

    time.sleep(10)    