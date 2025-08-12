✈️ Airline Flights Clustering Web App
📌 Overview
This project is a Flask-based web application that uses the K-Means clustering algorithm to group airline flights based on price, duration, and days left before departure.

Users can search by source city (state name) to find flights that belong to the same cluster, helping them compare similar flight options.

✨ Features
📂 Preloaded Flights Dataset – Uses airlines_flights_data.csv for clustering.

🤖 K-Means Clustering – Groups flights into 3 clusters based on:

Price

Duration

Days left until departure

🔄 Automatic Preprocessing – Handles missing values by filling them with the mean.

🌐 Web Interface – Search by source city and view all flights in the same cluster.

🛠️ Tech Stack
Backend: Python, Flask

ML & Data Processing: pandas, scikit-learn

Clustering Algorithm: K-Means

Frontend: HTML templates (Flask render_template)

📦 Installation
1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/airline-flights-clustering.git
cd airline-flights-clustering
2️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Add dataset
Place the dataset file airlines_flights_data.csv in the project folder.
It should contain columns like:

Copy
Edit
source_city, price, duration, days_left, ...
🚀 Usage
1️⃣ Run the Flask app
bash
Copy
Edit
python app.py
The app will be available at http://127.0.0.1:5000.

2️⃣ Search for flights
Enter a source city (state name) in the search box.

The app finds the cluster of that city’s flights and shows all flights in the same cluster.

📂 File Structure
bash
Copy
Edit
airline-flights-clustering/
                  │── app.py                     # Main Flask application
                  │── airlines_flights_data.csv  # Flight dataset
                  │── templates/
                  │   ├── index.html              # Search form
              │   ├── result.html             # Cluster results page
                  │── requirements.txt            # Python dependencies
⚠️ Notes
The model uses 3 clusters by default; adjust n_clusters in app.py to change.

Missing numeric values are automatically replaced with the column mean.

Input city names are case-insensitive.

📜 License
This project is licensed under the MIT License – you are free to use, modify, and distribute.
<img width="1366" height="426" alt="Screenshot (56)" src="https://github.com/user-attachments/assets/c3e5783c-a970-4cc4-b217-6d96744513ee" />
<img width="1366" height="768" alt="Screenshot (58)" src="https://github.com/user-attachments/assets/1ef4c2f6-d22d-4ed0-927a-d2d15a183e1e" />

