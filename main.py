#Author: Efe Akaröz
#17/03/2022
import praw
import selenium
from selenium.webdriver.common.keys import Keys
import cv2
import requests
import numpy as np
import os
import time


memeList = []
reddit = praw.Reddit(
	client_id="V5syNiSx4_8Fi2466QKGdA",
	client_secret="KdnEiE1Iqp8pYomm8j-6aaWkccS10Q",
	user_agent="Mac OS",
	
)
getSubredditName = input("Subreddit:")
getPostNum = input("How many posts we gonna post:")
getHotNewStuff = input("hot-top-new:")
subreddit = reddit.subreddit(getSubredditName)
driver = selenium.webdriver.Chrome("./chromedriver")
driver.get("https://twitter.com")
print("[IMPORTANT] Log In and enter")
a = input("press enter when you logged in \n")

"""

driver = selenium.webdriver.Chrome("./chromedriver")
driver.get("https://twitter.com")
print("[IMPORTANT] Log In and enter")
a = input("press enter when you logged in \n")



tweet = driver.find_element_by_css_selector("br[data-text='true']")
tweet.send_keys('I am a bot, bep bop')
button = driver.find_element_by_css_selector("div[data-testid='tweetButtonInline']")
button.click()
"""
dir_path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(dir_path, "image/")
if getHotNewStuff == "hot":




	subreddit = reddit.subreddit(getSubredditName)

	print(f"Starting {getSubredditName}!")
	count = 0
	for submission in subreddit.hot(limit=int(getPostNum)):
		if "jpg" in submission.url.lower() or "png" in submission.url.lower():
			try:
				resp = requests.get(submission.url.lower(), stream=True).raw
				image = np.asarray(bytearray(resp.read()), dtype="uint8")
				image = cv2.imdecode(image, cv2.IMREAD_COLOR)

				# Could do transforms on images like resize!
				compare_image = cv2.resize(image,(224,224))

				# Get all images to ignore
				idOfTheImage = f"{image_path}{getSubredditName}-{submission.id}.png"
				data  ={
					"image":idOfTheImage,
					"title":submission.title
				}
				

				
				cv2.imwrite(idOfTheImage, image)
				memeList.insert(0,data)
					
			except Exception as e:
				print(f"Image failed. {submission.url.lower()}")
				print(e)
		print(submission.title)

	for m in memeList:
		tweet = driver.find_element_by_css_selector("br[data-text='true']")
		tweet.send_keys(m["title"])
		time.sleep(1)
		s = driver.find_element_by_xpath("//input[@type='file']")
		#file path specified with send_keys
		s.send_keys(m["image"])
		time.sleep(5)
		button = driver.find_element_by_css_selector("div[data-testid='tweetButtonInline']")
		button.click()
		time.sleep(2)

if getHotNewStuff == "new":




	subreddit = reddit.subreddit(getSubredditName)

	print(f"Starting {getSubredditName}!")
	count = 0
	for submission in subreddit.new(limit=int(getPostNum)):
		if "jpg" in submission.url.lower() or "png" in submission.url.lower():
			try:
				resp = requests.get(submission.url.lower(), stream=True).raw
				image = np.asarray(bytearray(resp.read()), dtype="uint8")
				image = cv2.imdecode(image, cv2.IMREAD_COLOR)

				# Could do transforms on images like resize!
				compare_image = cv2.resize(image,(224,224))

				# Get all images to ignore
				idOfTheImage = f"{image_path}{getSubredditName}-{submission.id}.png"
				data  ={
					"image":idOfTheImage,
					"title":submission.title
				}
				

				
				cv2.imwrite(idOfTheImage, image)
				memeList.insert(0,data)
					
			except Exception as e:
				print(f"Image failed. {submission.url.lower()}")
				print(e)
		print(submission.title)

	for m in memeList:
		tweet = driver.find_element_by_css_selector("br[data-text='true']")
		tweet.send_keys(m["title"])
		time.sleep(1)
		s = driver.find_element_by_xpath("//input[@type='file']")
		#file path specified with send_keys
		s.send_keys(m["image"])
		time.sleep(5)
		button = driver.find_element_by_css_selector("div[data-testid='tweetButtonInline']")
		button.click()
		time.sleep(2)


if getHotNewStuff == "hot":




	subreddit = reddit.subreddit(getSubredditName)

	print(f"Starting {getSubredditName}!")
	count = 0
	for submission in subreddit.top(limit=int(getPostNum)):
		if "jpg" in submission.url.lower() or "png" in submission.url.lower():
			try:
				resp = requests.get(submission.url.lower(), stream=True).raw
				image = np.asarray(bytearray(resp.read()), dtype="uint8")
				image = cv2.imdecode(image, cv2.IMREAD_COLOR)

				# Could do transforms on images like resize!
				compare_image = cv2.resize(image,(224,224))

				# Get all images to ignore
				idOfTheImage = f"{image_path}{getSubredditName}-{submission.id}.png"
				data  ={
					"image":idOfTheImage,
					"title":submission.title
				}
				

				
				cv2.imwrite(idOfTheImage, image)
				memeList.insert(0,data)
					
			except Exception as e:
				print(f"Image failed. {submission.url.lower()}")
				print(e)
		print(submission.title)

	for m in memeList:
		tweet = driver.find_element_by_css_selector("br[data-text='true']")
		tweet.send_keys(m["title"])
		time.sleep(1)
		s = driver.find_element_by_xpath("//input[@type='file']")
		#file path specified with send_keys
		s.send_keys(m["image"])
		time.sleep(5)
		button = driver.find_element_by_css_selector("div[data-testid='tweetButtonInline']")
		button.click()
		time.sleep(2)





