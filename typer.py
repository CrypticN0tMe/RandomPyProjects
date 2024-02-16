import pyautogui
import pytesseract
import time
import keyboard

#test site
#https://official-typing-test.com/test/tenkey1.html

#kickstart
time.sleep(2)
start = (326, 510, 182, 30)
startshot = pyautogui.screenshot(region=start)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
startStr = pytesseract.image_to_string(startshot, config='--oem 3 -c tessedit_char_whitelist=0123456789./-+*')
pyautogui.typewrite(startStr)


for i in range(40):
    region = [(326, 550, 182, 30), (326, 590, 182, 30), (326, 630, 182, 30)]
    index = (i * 1) % len(region)  # Use modulo to wrap around if exceeding list length

    screenshot = pyautogui.screenshot(region=region[index])

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(screenshot, config='--oem 3 -c tessedit_char_whitelist=0123456789./-+*')

    pyautogui.typewrite(text)

    print(text)