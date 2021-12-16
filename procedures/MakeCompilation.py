'''
2. Compile video out of clips
'''
import os
import shutil
import moviepy
from moviepy.editor import VideoFileClip, concatenate_videoclips
import random

OUTPUT_DIR = (r"directory where the compiled video will be saved")
DAILY_TRENDING_DIR = (r"directory location for downloaded tiktok videos")
TOP_TEN_VIDS_DIR = (r"directory location for top 10 videos")

def select_videos(daily_trending_videos, top_videos):
    os.chdir(daily_trending_videos)
    trending_list = os.listdir(daily_trending_videos)
    daily_vids = []
    for trend in trending_list:
        file_path = os.path.join(daily_trending_videos, trend) 
        daily_vids.append(trend)
        #print(trend)

    random.shuffle(daily_vids)
    counter = 0
    selected_vids = daily_vids[:10]
    #print(selected_vids)
    for vid in selected_vids:
        print("Copying file: " + vid)
        shutil.copy(os.path.join(daily_trending_videos, vid), top_videos)

             
    
def create_video(top_ten_vids, output_file_name):
    videos = os.listdir(top_ten_vids)
    vid_clips = []
    for vid in videos:
        file_path = os.path.join(top_ten_vids, vid)
        clip = VideoFileClip(file_path)
        vid_clips.append(clip)
        print('Loading video: ' + vid)
        #clip.close()
    
    #random.shuffle(vid_clips)
    os.chdir(OUTPUT_DIR)
    finalClip = concatenate_videoclips(vid_clips, method="compose")
    finalClip.write_videofile(str(output_file_name + '.mp4'), threads=8, remove_temp=True, codec="libx264", audio_codec="aac")

    
def create_description(hex_text):
    main_text = hex_text.encode('utf-8')
    hex_value = main_text.hex()

    return hex_value

def test_mod():
    print('Working')

#select_videos(DAILY_TRENDING_DIR, TOP_TEN_VIDS_DIR)
#create_video(DAILY_TRENDING_DIR, output_file_name)




