''' Here, I write the SVD mathematical operation we need to done on the collected data, A = USV_T '''

import numpy as np # for vector maths
import pandas as pd # for data handling
import sklearn as sk
from sklearn.decomposition import TruncatedSVD # for SVD
from sklearn.feature_extraction.text import TfidfVectorizer # for TF-IDF
from sklearn.metrics.pairwise import cosine_similarity # for cosine similarity

''' 
The main idea is to first apply the SVD (A = USV_T) formula on the deta to get an one single matrix.
which will help us to get vectors of our provided vector then we are gonna apply the cosine similarity (which basically measure the angle between each vector) by that we can build the new vector which is close to each vector and boom! this is our recommendation. 
'''

''' 
<-------------------------------------------------------- Step 01 -------------------------------------------------------->
Now , I will make an function 'get_recommendations' function whose main job is simple , it take the data collected in 'recommender.py' and preform SVD (A =  U@S@V_T) operation on it.
'''

def get_recommendations(liked_videos, hated_videos, candidate_videos):
    # collecting data from recommender.py
    all_videos = liked_videos + hated_videos + candidate_videos
    df = pd.DataFrame(all_videos)

    # 1. Store lengths of original lists for safe slicing later
    num_liked = len(liked_videos)
    num_hated = len(hated_videos)
    num_candidates = len(candidate_videos)

    # TF-IDF Matrix (Create Matrix A)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['content'])
    # SVD create matrix U_k
    n_components = 5
    svd = TruncatedSVD(n_components=n_components)
    svd_matrix = svd.fit_transform(tfidf_matrix)

    # Build vector profile
    # 2. Use new variable names for the vectors
    liked_svd_vectors = svd_matrix[:num_liked]
    avg_liked_video = np.mean(liked_svd_vectors, axis=0)

    # Find the average vector for hated videos.
    hated_svd_vectors = svd_matrix[num_liked : num_liked + num_hated]
    avg_hated_video = np.mean(hated_svd_vectors, axis=0)

    # calculate the profile
    profile = avg_liked_video - avg_hated_video

    # calculate similarities
    # get the candidate vector the remaining rows.
    candidate_vectors = svd_matrix[num_liked + num_hated:]
    # Calculate cosine similarity between the user profile and all candidate vectors
    scores = cosine_similarity([profile], candidate_vectors)

    # Flatten scores to a 1D array
    scores = scores.flatten()

    # Create a list to store final results
    results = []

    # Loop through only the CANDIDATE portion of our data
    # Candidates start at index (num_liked + num_hated) in the 'all_videos' list
    start_index = num_liked + num_hated

    for i in range(num_candidates):
        # Get the original video data from our master list
        video_data = all_videos[start_index + i]
        results.append({
            'title': video_data['title'],
            'url': video_data['url'],
            'video_id': video_data.get('video_id'),
            'thumbnail': video_data.get('thumbnail'),
            'score': scores[i]
        })
    # Sort by score descending
    results.sort(key=lambda x: x['score'], reverse=True)

    return results