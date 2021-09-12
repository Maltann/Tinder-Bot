from selenium import webdriver
from random import randrange
from time import sleep
import pyautogui

print("-This script has been written by Maltan-")
startProgram = str = input("Press enter for start the program \n")
swipeCount = 0
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://tinder.com/fr")
print("Tinder is launching... You need to connect yourself before launching the program")
startClicking = str = input("Press enter for start swiping \n")

while True:
    for i in range(40):
        delayAfterClicking = randrange(1, 5)
        start = driver.find_element_by_xpath('//*[@id="q-84965404"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        start.click()
        sleep(delayAfterClicking)
        pyautogui.press('escape')
        swipeCount += 1
        print("Swipe number", swipeCount, "next swipe in:", delayAfterClicking, "seconds")
    delayTime = randrange(75, 145)
    print("taking a break of", delayTime, "seconds")
    sleep(delayTime)