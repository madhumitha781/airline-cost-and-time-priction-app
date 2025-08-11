from flask import Flask, render_template, request
import pandas as pd
from sklearn.cluster import KMeans

app = Flask(__name__)

# Load dataset
df = pd.read_csv("airlines_flights_data.csv")

# Preprocess: select numeric features for clustering
features = df[['price', 'duration', 'days_left']].copy()
features = features.fillna(features.mean())

# Apply K-means
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(features)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    state_name = request.form['state_name'].strip()

    # Filter by source city (state name)
    filtered_data = df[df['source_city'].str.lower() == state_name.lower()]

    if filtered_data.empty:
        return render_template('result.html', error="No data found for this state name.")

    # Get cluster for first matching row
    cluster_id = filtered_data.iloc[0]['cluster']
    cluster_data = df[df['cluster'] == cluster_id]

    return render_template('result.html',
                           state=state_name,
                           cluster_id=cluster_id,
                           data=cluster_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
