"""
Provide a countdown for X seconds, then print "Happy New Year! 🎉"
"""
import time

def countdown(seconds):
    
    if seconds > 0:
        while seconds != 0:
            print(seconds)
            time.sleep(1)
            seconds -= 1

        print('Happy New Year! 🎉')
    else:
        print("countdown is less than 0")


countdown(5)
countdown(7)
