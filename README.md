# 🎬 SVD-Based YouTube Recommender System

A **content-based recommendation engine** powered by **Singular Value Decomposition (SVD)** that learns your unique taste from the YouTube videos you love — and even the ones you hate.
You can run it either as a **command-line tool** or a **modern full-stack web app**.

🔗 **GitHub Repository:** [YouTube-video-recommendation-model-with-SVD](https://github.com/R72279A/YouTube-video-recommendation-model-with-SVD)

---

## 🚀 Features

### 🎯 Smart Recommendations

* **Content-Based Filtering** – Analyzes video metadata (*title, description, tags, channel, category*) to discover hidden “concepts.”
* **User Taste Profiling** – Builds a *mathematical vector of your taste* by combining your liked videos and subtracting disliked ones.
* **SVD Engine** – Leverages `TfidfVectorizer` + `TruncatedSVD` from scikit-learn to uncover *latent semantic patterns* in content.

### 💻 Dual Interface

* **🧠 CLI Mode:** Simple, quick testing from the terminal.
* **🌐 Web Mode:** A responsive web UI built with **Flask + Tailwind CSS**, featuring:

  * Top-3 personalized video recommendations
  * YouTube thumbnails
  * Embedded video playback

---

## 🛠️ Tech Stack

| Layer             | Tools / Libraries               |
| :---------------- | :------------------------------ |
| **Language**      | Python 3                        |
| **Web Framework** | Flask                           |
| **Data & ML**     | pandas, numpy, scikit-learn     |
| **Scraping**      | yt-dlp                          |
| **Frontend**      | HTML5, JavaScript, Tailwind CSS |

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/R72279A/YouTube-video-recommendation-model-with-SVD.git
cd YouTube-video-recommendation-model-with-SVD

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🏃‍♂️ How to Run

### Option 1: 🌐 Web Interface (Recommended)

```bash
python app.py
```

Then open your browser at 👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

**Steps:**

1. Paste YouTube URLs of videos you **like** and **dislike (optional)**.
2. Paste a list of **candidate videos** you want recommendations for.
3. Click **“Get Recommendations”** — and watch the algorithm work its magic.

---

### Option 2: 🧠 Command-Line Interface (CLI)

```bash
python main.py
```

Follow the on-screen prompts to:

* Paste your liked/disliked video URLs
* View your **top video recommendations** right in the terminal

---

## 📂 Project Structure

```
├── app.py              # Flask backend server (Web mode)
├── main.py             # CLI entry point
├── scraper.py          # Fetches metadata via yt-dlp
├── svd_engine.py       # Core TF-IDF, SVD & cosine similarity logic
├── templates/
│   └── index.html      # Web frontend (HTML/JS)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

Read the related article on medium for free to gain more clearity [Don’t Be a “Dumb Computer”: SVD Explained Subtitle: I built a YouTube recommender to finally understand the math. Here’s how it works (using a “Subway Map” analogy).](https://medium.com/@jasrotia.yadunandan.singh584/dont-be-a-dumb-computer-svd-explained-subtitle-i-built-a-youtube-recommender-to-finally-155eabfbcbe6)

---

## 💡 Inspiration

Just like how Netflix uses SVD to understand viewing preferences, this project applies **Linear Algebra concepts** to YouTube video recommendations — bridging **MIT 18.06 theory** with **real-world machine learning practice**.
