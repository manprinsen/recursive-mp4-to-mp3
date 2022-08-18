from moviepy.editor import *
import os
from threading import Thread
import time

START_DIRECTORY = "/volume1/music"
CONCURRENT_JOBS = 10
changed = 0
thread_list = []
delete_list = []
current_jobs = 0

# mp4=absolute path to mp4 file as string
# mp3=absolute path to mp3 file as string
def mp4_to_mp3(mp4, mp3):
	global current_jobs
	current_jobs += 1
	mp4_without_frames = AudioFileClip(mp4)
	mp4_without_frames.write_audiofile(mp3)
	mp4_without_frames.close()
	current_jobs -= 1

for path, current_directory, files in os.walk(START_DIRECTORY):
	for file in files:
		mp4 = os.path.join(path, file)
		pre, ext = os.path.splitext(mp4)
		
		if ext == ".m4a":
			os.rename(mp4, pre + ".mp4")
			mp4 = pre + ".mp4"
			pre, ext = os.path.splitext(mp4)
		
		if ext == ".mp4":
			while current_jobs >= CONCURRENT_JOBS:
				#print("to many jobs. please wait")
				time.sleep(1)
				
			mp3 = pre + ".mp3"
			t = Thread(target=mp4_to_mp3,args=(mp4,mp3))
			thread_list.append(t)
			t.start()
			delete_list.append(mp4)
			changed += 1

for t in thread_list:
	t.join()
print(f"all {changed} files converted to mp3. starting to delete original files.")

for item in delete_list:
	os.remove(item)
print("original files deleted.")
