# la-rts (la minus recorded twitter space)
Simple scripts to download Twitter Recorded Space by using Selenium


# Limitations
- Support only Chrome 96
- Support only Windows (tested only in Windows 10)


# Pre-requisite
- Python 3 installed
- ffmpeg installed (https://ffmpeg.org/download.html, download from "Get packages & executable files")<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- place the `ffmpeg.exe` file into this folder
- Chrome 96 installed
- Download chromedriver version 96 (https://chromedriver.chromium.org/downloads)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- place the `chromedriver.exe` file into this folder


# How to use
1. Run this command `python la-rts.py {insert-tweet-space-url}`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;a. Example `python la-rts.py https://twitter.com/smokwi420great/status/1420691919566`
2. Wait til the download is completed.
3. You should have a new file `space.m4a` created. Rename it to however you like


# How does this tool work *(it's ok to ignore this)*
1. The script will automatically open a chrome browser
2. The script will auto-load the twitter space.
3. The script will auto-click the "Play Recording" button.
4. The script will scan for m3u8 URL in background for 10~15 seconds.
5. The script will run ffmpeg command with the m3u8 URL to download twitter space audio
6. The script will turn the downloaded audio to a m4a file and name it as `space.m4a`
<br/>
<br/>

# Disclaimer/Caveat
- Instructions written here assumed you already knew some stuffs (e.g. what is "Python")
- User Guide might not be well-explain.
- Hazue created this merely to download a certain ~~Comedian~~ celebrity's recorded twitter space.
- No thorough testing done.
- Expect errors when<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- Python version is wrong/outdated<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- ffmpeg version is different, or has a change of command<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- chrome version outdated<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- chromedriver version outdated<br/>


