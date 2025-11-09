import logging
from flask import Flask, render_template, request, jsonify
# Import your existing modules. 
# Make sure the filenames match EXACTLY what you have in your folder.
try:
    from scrapper import scrape_video
    from svd_engine import get_recommendations
except ImportError as e:
    print(f"CRITICAL ERROR: Could not import your modules. {e}")
    print("Make sure 'scraper.py' and 'svd_engine.py' are in the same folder as 'app.py'.")
    exit(1)

app = Flask(__name__)

# Set up basic logging to see what's happening in the terminal
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def index():
    """Renders the main page."""
    return render_template('index.html')

@app.route('/api/recommend', methods=['POST'])
def api_recommend():
    """
    Main API endpoint.
    Receives JSON data with lists of URLs, scrapes them, runs SVD, and returns results.
    """
    try:
        data = request.json
        liked_urls = data.get('liked_urls', [])
        hated_urls = data.get('hated_urls', [])
        candidate_urls = data.get('candidate_urls', [])

        if not liked_urls or not candidate_urls:
            return jsonify({'status': 'error', 'message': 'Please provide at least one liked video and one candidate video.'}), 400

        logging.info(f"Received request: {len(liked_urls)} liked, {len(hated_urls)} hated, {len(candidate_urls)} candidates.")

        # --- STEP 1: SCRAPE DATA ---
        # We use a helper function to keep things clean and handle errors for individual videos.
        def scrape_list(url_list):
            results = []
            for url in url_list:
                if url.strip():
                    logging.info(f"Scraping: {url}")
                    # Calling YOUR scraper function here
                    video_data = scrape_video(url.strip())
                    if video_data.get('status') == 'success':
                         results.append(video_data)
                    else:
                         logging.warning(f"Failed to scrape: {url}")
            return results

        logging.info("Starting scraping process...")
        liked_data = scrape_list(liked_urls)
        hated_data = scrape_list(hated_urls)
        candidate_data = scrape_list(candidate_urls)
        logging.info("Scraping complete.")

        if not liked_data:
             return jsonify({'status': 'error', 'message': 'Could not successfully scrape any of your LIKED videos. Please check the URLs.'}), 400
        if not candidate_data:
             return jsonify({'status': 'error', 'message': 'Could not successfully scrape any CANDIDATE videos. Please check the URLs.'}), 400

        # --- STEP 2: RUN SVD ENGINE ---
        logging.info("Running SVD Recommendation Engine...")
        # Calling YOUR SVD engine function here
        recommendations = get_recommendations(liked_data, hated_data, candidate_data)
        logging.info("Recommendation complete.")

        return jsonify({'status': 'success', 'recommendations': recommendations})

    except Exception as e:
        logging.error(f"An error occurred during processing: {e}", exc_info=True)
        return jsonify({'status': 'error', 'message': f"An internal server error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # debug=True allows for auto-reloading when you change code
    app.run(debug=True, port=5000)