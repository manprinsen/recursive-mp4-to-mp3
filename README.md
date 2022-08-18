The following script will recursivly itterate over files in a given directory, convert mp4/m4a files to mp3 files and after it's done it will clean up the mp4/m4a files.

pip install moviepy

download the mp4-to-mp3.py file

edit mp4-to-mp3.py and adjust the following variables to match your needs:
START_DIRECTORY => in what folder do you want to convert mp4/m4a files to mp3?
CONCURRENT_JOBS => how many conversions of mp4/m4a to mp3 shall run at the same time?

Then run
```python mp4-to-mp3.py```

Happy hacking
