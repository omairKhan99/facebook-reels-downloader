import os
import sys
import csv
import subprocess
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()  # Adjust if needed
driver.maximize_window()

# Get command-line arguments
channel = sys.argv[1]
url = sys.argv[2]
format_choice = sys.argv[3]  # e.g. "mp4", "mp3", etc.

# Open the channel reel URL
driver.get(url)

# Close any pop-ups
sleep(5)
try:
    close_button = driver.find_element(By.XPATH, "//div[@aria-label='Close']")
    close_button.click()
except Exception as e:
    print("No pop-up found or error closing pop-up:", e)

# Scroll and extract reels URLs
scroll_steps = 100
scroll_interval = 4
prev_scroll_position = 0

for _ in range(scroll_steps):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(scroll_interval)
    
    curr_scroll_position = driver.execute_script("return window.pageYOffset;")
    if curr_scroll_position == prev_scroll_position:
        break
    prev_scroll_position = curr_scroll_position

# Collect reel URLs
reel_links = driver.find_elements(By.CSS_SELECTOR, 'a')
reel_urls = []

for link in reel_links:
    href = link.get_attribute('href')
    if href and '/reel/' in href:
        reel_urls.append(href.split('/?s=')[0])

driver.quit()
output_dir = os.path.join("output", channel)
os.makedirs(output_dir, exist_ok=True)

csv_path = os.path.join("output", f"{channel}.csv")
with open(csv_path, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for url in reel_urls:
        writer.writerow([url])

#choosing popular video formats
video_formats = ["mp4", "mov", "webm", "mkv"]
audio_formats = ["mp3"]
