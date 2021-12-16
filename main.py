'''
1. Download clips
2. Compile video out of clips
3. Upload video to YouTube
4. Send tweet when video is published
'''
import sys
import os
import shutil
import datetime
import random
import string
import procedures.DownloadVideos as download_tiktok
import procedures.MakeCompilation as make_compilation
import procedures.UploadCompilation as upload_compilation
import procedures.SendNotification as send_notification

MAIN_DIR = (r"directory to hold other directories")
DAILY_TRENDING_DIR = (r"directory location for downloaded tiktok videos")
TOP_TEN_VIDS_DIR = (r"directory location for top 10 videos")

output_file_text = "This file was uploaded on: "
todays_date = datetime.date.today()
output_file_name = output_file_text + str(todays_date)


def remove_videos(file_dir):
    vid_dir = file_dir
    for file in os.listdir(vid_dir):
        os.remove(os.path.join(vid_dir, file))

def generate_title():
    cur_date = datetime.date.today()
    title = 'Video Compilation for ' + str(cur_date)

    return title

title = generate_title()
#print(title)

def main():

    #Change directory to MAIN_DIR
    try:
        os.chdir(DAILY_TRENDING_DIR)
        #print('Directory changed.')
    except FileNotFoundError:
        print('Video directory not found.')
        dir_name = 'Daily Trending Videoss'
        new_dir_path = os.path.join(MAIN_DIR, dir_name)
        print('Creating video directory...')
        os.mkdir(new_dir_path)

    isdir = os.path.isdir(DAILY_TRENDING_DIR)
    #print(isdir)
    
    #Download TikTok source videos
    title = generate_title()
    print('Downloading TikTok videos...')
    download_tiktok.download_tiktoks()
    print('TIkTok vidoes successfully downloaded.')

    #Create video compilation
    print('Selecting videos for compilation...')
    make_compilation.select_videos(DAILY_TRENDING_DIR, TOP_TEN_VIDS_DIR)
    print('Videos selected.')
    
    video_desc = make_compilation.create_description(output_file_name)
    print(video_desc)

    print('Creating video compilation...')
    make_compilation.create_video(TOP_TEN_VIDS_DIR, title)
    print('Video compilation created.')
    #make_compilation.test_mod()
    
    #Upload video compilation to YouTube
    upload_compilation.upload_compilation(output_file_name, title, video_desc)
    print('Video uploaded to YouTube.')
    
    #Send notification tweet when video is uploaded
    send_notification.send_tweet(title, video_desc)
    print('Notification tweet sent out.')
    
    #Remove compliation source videos
    print('Removing TikTok source videos...')
    remove_videos(DAILY_TRENDING_DIR)
    print('Videos sources removed.')
       

if __name__ == '__main__':
    main()
