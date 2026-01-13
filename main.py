import time
import datetime
import pygame


def set_alarm(alarm_set):
    print(f"Alarm set for {alarm_set}")
    sound_file="[iSongs.info] 02 - Firestorm.mp3"
    is_running=True
    while is_running:
        current_time=datetime.datetime.now().strftime("%I:%M:%S %p")
        print(current_time)
        if current_time==alarm_set:
            print("WAke up")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while  pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running=False

        time.sleep(1)


if __name__=="__main__":
    alarm_set=input("Enter the time to set(HH:MM:SS AM/pm): ")
    set_alarm(alarm_set)


