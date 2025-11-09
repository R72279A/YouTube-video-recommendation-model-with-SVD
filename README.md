SVD-Based YouTube Recommender System

A content-based recommendation engine that uses Singular Value Decomposition (SVD) to understand a user's taste from their liked and hated YouTube videos. It can be run as a simple command-line tool or as a full-stack web application.

🚀 Features

Content-Based Filtering: Analyzes video metadata (title, description, tags, channel, category) to find hidden "concepts."

User Taste Profiling: Creates a unique mathematical vector for a user by combining what they like and subtracting what they hate.

SVD Engine: Uses scikit-learn's TfidfVectorizer and TruncatedSVD to perform dimensionality reduction and uncover latent patterns in video content.

Dual Interface:

CLI Mode: Quick and easy testing directly from the terminal.

Web Mode: A modern, responsive web interface built with Flask and Tailwind CSS, featuring top-3 results, video thumbnails, and embedded playback.

🛠️ Tech Stack

Language: Python 3

Web Framework: Flask

Data & ML: pandas, numpy, scikit-learn

Scraping: yt-dlp

Frontend: HTML5, JavaScript, Tailwind CSS

📦 Installation

Clone the repository:

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name


Install dependencies:
It's recommended to use a virtual environment.

pip install -r requirements.txt


🏃‍♂️ How to Run

Option 1: Web Interface (Recommended)

Run the Flask app:

python app.py


Open your browser and go to http://127.0.0.1:5000.

Paste YouTube URLs for videos you like, hate (optional), and a list of candidate videos to test.

Click "Get Recommendations" to see the magic!

Option 2: Command-Line Interface (CLI)

Run the main script:

python main.py


Follow the on-screen prompts to paste your lists of URLs.

The top recommendations will be printed directly in the terminal.

📂 Project Structure

app.py: Flask backend server for the web interface.

main.py: Entry point for the CLI version.

scraper.py: Module for fetching metadata from YouTube URLs using yt-dlp.

svd_engine.py: Core logic for TF-IDF, SVD, and cosine similarity calculations.

templates/index.html: The frontend HTML/JS for the web app.

requirements.txt: List of Python dependencies.
