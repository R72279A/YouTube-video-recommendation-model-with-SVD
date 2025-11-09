from scrapper import scrape_video
import os
import json
from svd_engine import get_recommendations as gr

if __name__ == "__main__" :
    ''' ---Liked videos list--- '''
    print("Enter the URLs for Liked YouTube Videos, separated by spaces:")
    urls_input = input()
    urls = urls_input.split()

    liked_videos = []
    for i, url in enumerate(urls, 1):
        print(f"--- Scraping video #{i} ---")
        result = scrape_video(url.strip())
        if result['status'] == 'success':
            liked_videos.append(result)
            print(json.dumps(result, indent=2))
        else:
            print(f"Could not scrape URL: {url}")
            print(f"Reason: {result['status']}")
        print("-" * 30) # Prints a separator line

    print("\nScraping complete!")

    # --- Hated videos list ---
    print('\n--- Enter HATED Videos ---')
    print("Enter the URLs for HATED YouTube Videos, separated by spaces:")
    hated_urls_input = input()
    hated_urls = hated_urls_input.split()

    hated_videos = []
    for i, url in enumerate(hated_urls, 1):
        print(f"--- Scraping hated video #{i} ---")
        result = scrape_video(url.strip())
        if result['status'] == 'success':
            hated_videos.append(result)
            print(json.dumps(result, indent=2))
        else:
            print(f"Could not scrape URL: {url}")
            print(f"Reason: {result['status']}")
        print("-" * 30) # Prints a separator line

    print("\nScraping complete for all videos!")

    print("\nScraping complete for hated videos!")

    # --- CANDIDATE VIDEOS LIST ---
    print('\n--- Enter CANDIDATE Videos ---')
    print("what video your are most intrusted in watching are recommended by YouTube system you in the botton of the Liked videos : ")
    candidate_urls_input = input()
    candidate_urls = candidate_urls_input.split()

    candidate_videos = []
    for i, url in enumerate(candidate_urls, 1):
        print(f"--- Scraping candidate video #{i} ---")
        result = scrape_video(url.strip())
        if result['status'] == 'success':
            candidate_videos.append(result)
            print(f"Successfully scraped: {result.get('title', 'Unknown Title')}")
        else:
            print(f"Could not scrape URL: {url}")
            
    print("\nScraping complete for all videos! Starting Recommendation Engine...")

    recommendations = gr(liked_videos, hated_videos, candidate_videos)
    print(recommendations)


