'''
4. Send tweet when video is published
'''
import tweepy

consumer_key = 'consumer key'
consumer_secret = 'consumer secret key'
access_token = 'access token'
access_token_secret = 'access token secret'

def send_tweet(video_title, video_desc):
    def OAuth():
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
        except Exception as e:
            return None

    oauth = OAuth()
    api = tweepy.API(oauth)

    api.update_status('A new video has been uploaded: ' + video_title)

    print('Tweet has been successfully posted.')

#send_tweet(video_title, video_desc)
