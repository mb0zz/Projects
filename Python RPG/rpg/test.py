#importing modules
import os, time, winsound
def fake_crash():
	cycle = 0
	while cycle < 50:
		os.system("color 7")
		time.sleep(.3)
		print("Error\nError\nError")
		winsound.Beep(700, 200)
		os.system("color 4")
		cycle += 1
		time.sleep(.3)
		print("Error\nError\nError")
fake_crash()

