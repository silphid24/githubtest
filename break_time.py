
import time
import webbrowser


total_breaks = 3
break_count = 0

print("this program started on "+ time.ctime())
while(break_count < total_breaks):
	time.sleep(3)
	webbrowser.open("https://youtu.be/T7dhKmR_q-0")
	break_count = break_count + 1

