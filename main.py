import json
from scrapper import scrape_video
from svd_engine import get_recommendations

def get_video_list(prompt_text, detailed_output=False):
    """
    Helper function to get a list of video URLs from the user and scrape them.
    """
    print(f'\n--- {prompt_text} ---')
    # Updated prompt as requested by user
    if "CANDIDATE" in prompt_text:
         print("In what video are you most interested in watching that is recommended by the YouTube system? (Paste URLs separated by spaces):")
    else:
        print("Paste URLs separated by spaces, then press Enter:")
        
    urls_input = input()
    urls = urls_input.split()
    
    video_data_list = []
    for i, url in enumerate(urls, 1):
        print(f"--- Scraping video #{i} ---")
        result = scrape_video(url.strip())
        
        if result['status'] == 'success':
            video_data_list.append(result)
            if detailed_output:
                # Print full JSON for liked/hated to confirm data quality
                print(json.dumps(result, indent=2))
            else:
                # Just print title for candidates to keep it clean
                print(f"Successfully scraped: {result.get('title', 'Unknown Title')}")
        else:
            print(f"Could not scrape URL: {url}")
            print(f"Reason: {result.get('status', 'Unknown error')}")
        print("-" * 30)
        
    return video_data_list

if __name__ == "__main__":
    print("============================================")
    print("   Content-Based YouTube Recommender (CLI)  ")
    print("============================================")

    # 1. Get Liked Videos
    liked_videos = get_video_list("STEP 1: LIKED VIDEOS", detailed_output=True)

    # 2. Get Hated Videos
    hated_videos = get_video_list("STEP 2: HATED VIDEOS", detailed_output=True)

    # 3. Get Candidate Videos (using your custom prompt inside the function)
    candidate_videos = get_video_list("STEP 3: CANDIDATE VIDEOS", detailed_output=False)

    print("\n\n--- Scraping Complete! Starting Recommendation Engine ---")

    # 4. Run the SVD Engine
    if not candidate_videos:
         print("Error: No candidate videos were scraped successfully. Cannot make recommendations.")
    else:
        recommendations = get_recommendations(liked_videos, hated_videos, candidate_videos)

        # 5. Display Final Results
        print("\n============================================")
        print("       FINAL RECOMMENDATIONS (Ranked)       ")
        print("============================================")
        
        for i, rec in enumerate(recommendations, 1):
            print(f"\n#{i}: {rec['title']}")
            print(f"   Score: {rec['score']:.4f}")
            print(f"   URL: {rec['url']}")

    print("\n============================================")
    print("Done!")