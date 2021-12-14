from selenium import webdriver
import time
import sys

if __name__ == '__main__':
    
    strTwitterUrl = sys.argv[1]
    
    print("Preparing javascript to inject")
    jsfile = open("tmp-get-twitter-space-m3u8.js", "r")
    strJavaScript = jsfile.read()
    time.sleep(1)
    
    print("Opening [controlled browser]")
    driver = webdriver.Chrome(executable_path="chromedriver_96.exe")
    time.sleep(1)
    
    print('Loading twitter space. Assume it takes 5 seconds to load')
    driver.get(strTwitterUrl)
    time.sleep(5)
    
    print("Getting m3u8 URL for ffmpeg")
    print("Takes about 10 seconds to observe twitter's traffic.")
    driver.execute_script(strJavaScript)
    time.sleep(10)
    
    print("10 seconds passed. hopefully we capture the m3u8 URL.")
    strUrlM3U8 = driver.execute_script('return strPlaylistm3u8')
    
    if strUrlM3U8 is None or strUrlM3U8 == '':
        print("capture the m3u8 URL D:")
        print("Hazue will debug when he's free")
        exit()
    
    print("Ayyy we got m3u8 URL, time to run ffmpeg")
    strFullCommand = 'ffmpeg -user_agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7" '
    strFullCommand += ' -i '+strUrlM3U8
    strFullCommand += ' -c copy space.m4a'
    
    
    print("\nCopy paste below command, run it and the downloading will begins.\n")
    print(strFullCommand)
    
    print("\n\nThis program isn't fool-proof so good luck in downloading (may the force be with you)\n")
    
    driver.close()
    driver.quit()
    
    