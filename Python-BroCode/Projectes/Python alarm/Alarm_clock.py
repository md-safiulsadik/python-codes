# Python alarm clock

import msvcrt
import time , datetime , pygame

MAX_HOURS = 23
MAX_MINUTES = 59
MAX_SECONDS = 59

def user_input():
    while True:
        try:
            hour = int(input("Hours : "))
            minute = int(input("Minutes : "))
            second = int(input("Seconds : "))

            if (0 <= hour <= MAX_HOURS and
                0 <= minute <= MAX_MINUTES and
                0 <= second <= MAX_SECONDS):

                return datetime.time(hour=hour , minute=minute, second=second)
            else:
                print("Please check you input")
                continue
            
        except ValueError as e:
            print("Invalid input. Please enter an integer.")


def set_alarm(alarm_time):
    
    print(f"\nYour alarm set for {alarm_time}")
    alarm_sound = "D:\\Study\\Python\\Python_BroCode\\Projectes\\Python alarm\\Alarm Clock.mp3"
    is_running = True

    while is_running:

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Wake Up !")

            pygame.mixer.init()
            pygame.mixer.music.load(alarm_sound)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)


def main() -> None:
    print("""
                                                Python Alarm Clock
                                   ---------------------------------------------
                                                Set    a     Alarm
                      """)

    alarm_time = user_input()
    set_alarm(alarm_time.strftime("%H:%M:%S"))

    
    print("Any key to exit")
    msvcrt.getch()

if __name__ == "__main__":
    main()