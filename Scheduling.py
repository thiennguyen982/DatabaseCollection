from flask import Flask, request, Response
from concurrent.futures import ThreadPoolExecutor
import threading
import asyncio
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os

class SchedulingApp:
    def __init__(self):
        self.app = Flask(__name__)

        # Define a Job class to represent jobs
        class Job:
            def __init__(self, start, finish, weight):
                self.start = start
                self.finish = finish
                self.weight = weight

        # Function to solve the scheduling problem (Updated Weighted Interval Scheduling Problem)
        def find_max_weight(jobs):
            jobs.sort(key=lambda job: job.finish)
            n = len(jobs)
            max_weights = [0] * n

            def find_previous_non_overlapping_job(current_job_index):
                low, high = 0, current_job_index - 1
                while low <= high:
                    mid = (low + high) // 2
                    if jobs[mid].finish <= jobs[current_job_index].start:
                        if jobs[mid + 1].finish <= jobs[current_job_index].start:
                            low = mid + 1
                        else:
                            return mid
                    else:
                        high = mid - 1
                return -1

            def dp(i):
                if i == 0:
                    return jobs[0].weight
                if max_weights[i] != 0:
                    return max_weights[i]

                include_weight = jobs[i].weight
                prev_job_index = find_previous_non_overlapping_job(i)
                if prev_job_index != -1:
                    include_weight += dp(prev_job_index)

                exclude_weight = dp(i - 1) if i > 0 else 0

                max_weights[i] = max(include_weight, exclude_weight)
                return max_weights[i]

            return dp(n - 1)

        def generate_schedule_image():
            # Replace 'your_connection_string' with your SQL Server connection string
            engine = create_engine('your_connection_string')
            query = "SELECT start, finish, weight FROM scheduling_data"
            df = pd.read_sql(query, engine)

            # Your existing find_max_weight function here
            max_weight = find_max_weight(df)

            # Create a simple bar plot
            plt.figure(figsize=(8, 6))
            plt.bar(df.index, df['weight'], label='Job Weights')
            plt.xlabel('Job Index')
            plt.ylabel('Weight')
            plt.title('Job Scheduling')
            plt.legend()

            # Convert the plot to an image
            image_stream = BytesIO()
            plt.savefig(image_stream, format='png')
            image_stream.seek(0)
            plt.close()

            return image_stream

        @self.app.route('/schedule/', methods=['POST'])
        async def schedule():
            try:
                # Check if a CSV file was uploaded
                if 'file' not in request.files:
                    return jsonify({"error": "No file part"}), 400

                file = request.files['file']
                if file.filename == '':
                    return jsonify({"error": "No selected file"}), 400

                if file:
                    # Save the uploaded CSV file to a temporary location
                    csv_filename = os.path.join('temp', 'uploaded_schedule.csv')
                    file.save(csv_filename)

                    # Load the CSV data using Pandas
                    df = pd.read_csv(csv_filename)

                    # Your existing find_max_weight function here
                    max_weight = find_max_weight(df)

                    # Generate the schedule image
                    image_stream = generate_schedule_image()

                    # Save the image in SQL Server (adjust your SQL query accordingly)
                    engine = create_engine('your_connection_string')
                    with engine.connect() as connection:
                        connection.execute("INSERT INTO scheduling_images (image_data) VALUES (?)", image_stream.read())

                    # Create an XML response
                    xml_response = f'<result>{max_weight}</result>'

                    return Response(xml_response, content_type='application/xml')

            except Exception as e:
                return jsonify({"error": str(e)}), 500

    def run(self):
        if __name__ == '__main__':
            self.app.run(threaded=True, host='0.0.0.0', port=5000, ssl_context=('your_cert.pem', 'your_key.pem'))

if __name__ == '__main__':
    scheduling_app = SchedulingApp()
    scheduling_app.run()