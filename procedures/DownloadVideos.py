'''
1. Download daily trending TikTok clips
'''
from TikTokApi import TikTokApi
import string
import random
import os

DAILY_TRENDING_DIR = (r"directory location for downloaded tiktok videos")
verifyFp = 'use s_v_web_id cookie from tiktok.com'
did = ''.join(random.choice(string.digits) for num in range(19))

api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

tiktoks = api.trending()
video_bytes = api.get_Video_By_TikTok(tiktoks[0])

def download_tiktoks():
    os.chdir(DAILY_TRENDING_DIR)
    for tiktok in tiktoks:
        video_bytes = api.get_Video_By_TikTok(tiktok)
        author = tiktok['author']['uniqueId']
        #print(author)
        with open(str(author) + '.mp4', 'wb') as o:
            o.write(video_bytes)
        print('Downloading: ' + tiktok['author']['uniqueId'])
        
 
