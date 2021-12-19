from selenium import webdriver
import time
import sys
import os
import logging


def validateRequiredExecutables():
    filesInThisFolder = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    if "ffmpeg.exe" not in filesInThisFolder:
        print('Cannot find ffmpeg.exe.')
        print('Please place ffmpeg.exe in the same folder as this python file.')
        quit()
        
    if "chromedriver.exe" not in filesInThisFolder:
        print('Cannot find chromedriver.exe.')
        print('Please place chromedriver.exe in the same folder as this python file.')
        quit()
        

def validateUrlKeyword(strKeyword):
    if strKeyword not in strTwitterUrl:
        print("Hmmmmm this URL has no ["+ strKeyword +"] :thonk: ")
        print("Exitting this script lol")
        exit()


if __name__ == '__main__':
    
    ###################################
    ########### Validations ###########
    ###################################
    
    # will quit() inside this function
    validateRequiredExecutables()
    
    # make is legit URL 
    strTwitterUrl = sys.argv[1]
    if len(strTwitterUrl) <= 10:
        print("Is this even a legit URL for Twitter Space? Exitting lol")
        exit()
    
    validateUrlKeyword('twitter')
    validateUrlKeyword('https')
    
    
    
    ###################################
    ########### Preparation ###########
    ###################################
    
    print("\n1. Preparing javascript to inject")
    jsfile = open("tmp-get-twitter-space-m3u8.js", "r")
    strJavaScript = jsfile.read()
    time.sleep(1)
    
    
    
    
    ###################################
    ############ Real Work ############
    ###################################
    
    # TODO: add function to auto detect chromedriver regardless of version
    print("\n2. Opening [controlled browser]")
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    time.sleep(1)
    
    print('\n3. Loading twitter space. Assume it takes 5 seconds to load')
    driver.get(strTwitterUrl)
    time.sleep(5)
    
    print("\n4. Getting m3u8 URL for ffmpeg")
    print("(Takes about 10 seconds to observe twitter's traffic)")
    driver.execute_script(strJavaScript)
    time.sleep(10)
    
    print("\n5. 10 seconds passed. hopefully we capture the m3u8 URL.")
    strUrlM3U8 = driver.execute_script('return strPlaylistm3u8')
    
    if strUrlM3U8 is None or strUrlM3U8 == '':
        print("capture the m3u8 URL D:")
        print("Hazue will debug when he's free")
        exit()
    
    print("\n6. Ayyy we got the m3u8 URL. The script will auto run ffmpeg")
    strFullCommand = 'ffmpeg -user_agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7" '
    strFullCommand += ' -i '+strUrlM3U8
    strFullCommand += ' -c copy space.m4a'

    print(strFullCommand)
    time.sleep(3)
    
    print("\n7. Running ffmpeg command in 3 seconds\n")
    os.system(strFullCommand)
    
    input("\n\nCompleted! press enter to exit")
    print("exitting... closing browser...")
    
    driver.close()
    driver.quit()
    
    