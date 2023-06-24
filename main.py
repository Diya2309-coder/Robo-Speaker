import os
import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    print("welcome to ROBO-speaker contest")
    text = input("Hello Diya, how are you?")
    engine.say(f"{text}")
    engine.runAndWait()
    # print("welcome to ROBO-speaker contest")
    # x = input("what u want me to speak :")
    # command = f"say {x}"
    # os.system(command)
