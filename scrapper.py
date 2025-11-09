''' 
This is scrapper file used to collect video information from YouTube links. 
it uses the yt_dlp library to extract metadata without downloading the video.
and returns the information in JSON format.
'''

import yt_dlp
import json

def scrape_video(youtube_link):
    # FIXED: Removed the hardcoded URL line that was breaking the input.

    ydl_ipts = {
        'skip_download': True, # this prevents the video for being downloaded
        'quiet': True, # this suppresses the output messages
        'no_warnings': True, # this supresses the warning message.
    }

    '''
     for error handling, I am writting a try except block. 
     If any error occurs during the extraction process, it will be caught and an error message will be returned.
    '''
    try:
        with yt_dlp.YoutubeDL(ydl_ipts) as ydl:
            info = ydl.extract_info(youtube_link, download=False) 

            ''' Now let's pull out the relevent information for the model.'''

            title = info.get('title', 'video title')
            video_id = info.get('id', 'video id')
            thumbnail_url = info.get('thumbnail', 'thumbnail url')
            description = info.get('description', 'video description')
            channel = info.get('uploader', 'channel name')
            tags = info.get('tags', [])
            categories = info.get('categories', [])
            tag_string = ' '.join(tags)
            category_string = ' '.join(categories)
            
            content = f"{category_string} {channel} {title} {description} {tag_string}"

            ''' Now i am combining the content into a JSON format. '''
            return {
                "url": youtube_link,
                "video_id": video_id,
                "thumbnail": thumbnail_url,
                "title": title,
                "channel": channel,
                "category": category_string,
                "content": content,
                "status": "success"
            }

    except Exception as e:
        # FIXED: Return a dictionary even on error, so the main program doesn't crash later.
        return {
            "url": youtube_link,
            "title": None,
            "channel": None,
            "category": None,
            "content": None,
            "status": f"failed: {str(e)}"
        }

if __name__ == "__main__":
    url = ()
    print(json.dumps(scrape_video(url), indent=2))






