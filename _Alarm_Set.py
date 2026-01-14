import time
import datetime
import pygame

def Set_Alarm(Alarm):
    print(f"your alarm is set to {Alarm} ")

    song="[iSongs.info] 02 - Firestorm.mp3"
    is_running=True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time==Alarm:
            print("Wake Up!!")

            pygame.mixer.init()
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running=False

        time.sleep(1)









if __name__=="__main__":
    Alarm=input("Enter the time to set (%H:%M:%S): ")
    Set_Alarm(Alarm)
