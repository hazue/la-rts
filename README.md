# la-rts (la minus recorded twitter space)
Simple scripts to download Twitter Recorded Space by using Selenium

# Limitations
- Support only Chrome 96
- Support only Windows (tested only in Windows 10)

# Pre-requisite
- Python 3 installed
- ffmpeg installed (https://ffmpeg.org/download.html, download from "Get packages & executable files")
- Chrome 96 installed
- Download chromedriver (https://chromedriver.chromium.org/downloads)

# User Guide
1. For first time user<br/>
&nbsp;&nbsp;&nbsp;&nbsp;a. After you have downloaded ffmpeg, place the `ffmpeg.exe` file into this folder<br/>
&nbsp;&nbsp;&nbsp;&nbsp;b. After you have downloaded chromedriver version 96, place the `chromedriver.exe` file into this folder
2. Run below command `python la-rts.py {insert-tweet-space-url}`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;a. Example `python la-rts.py https://twitter.com/LaplusDarknesss/status/1420691919566`
3. What will happen (it's ok to ignore this step)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;a. The script will automatically opened a chrome browser<br/>
&nbsp;&nbsp;&nbsp;&nbsp;b. The script will auto-load the twitter space.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;c. The script will auto-click the "Play Recording" in twitter.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;d. The script will scan for m3u8 URL in background.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;e. The script will run ffmpeg command with the m3u8 URL to download twitter space audio
4. Wait til the download is completed.
5. You should have a new file `space.m4a` created. Rename it to however you like


# TODO for Developer
- add validation to make sure relevant exe exists
- add function to auto detect chromedriver regardless of version


# Notes
- Instructions written here assumed you already knew some stuffs (e.g. what is "Python")
- User Guide might not be well-explain.
- Hazue created this merely to download a certain ~~Comedian~~ celebrity's recorded twitter space.
- No thorough testing done.
- Expect errors when
&nbsp;&nbsp;&nbsp;&nbsp;- Python version is wrong/outdated<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- ffmpeg version is different, or has a change of command<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- chrome version outdated<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- chromedriver version outdated<br/>
