'''
3. Upload video to YouTube
'''
import datetime
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from apikey import apikey

def upload_compilation(video_file, video_title, video_desc):
    CLIENT_SECRET_FILE = 'directory to client_secret.json'
    #https://www.googleapis.com/auth/youtube.upload
    #https://www.googleapis.com/auth/youtube.force-ssl
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_console()
    youtube = build('youtube', 'v3', credentials=credentials)

    upload_data_time = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, int(now.second)).isoformat() + '.000Z'

    request_body = {
        'snippet': {
            'category': 19,
            'title': 'Test Upload',
            'description': 'Test upload',
            'tags': ['Python', 'YouTube API', 'Google']
            },
        'status': {
            'privacyStatus': 'public'.
            'publishAt': upload_date_time,
            'selfDeclaredMadeForKids': False,
            },
        'notifySubscribers': False
        }
 
    mediaFile = MediaFileUpload(video_file)

    response_upload = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
        ).execute()


