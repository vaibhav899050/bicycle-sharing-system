import numpy as np
import pandas as pd
import time
from datetime import datetime

#function for part 1 of question 1
def duration_func():
    startin_time = time.time()
    filename = "bike_data_new.csv"

    bike = pd.read_csv(filename)
    bike["duration"] = bike.apply(lambda x: (datetime.strptime(x["ended_at"], "%d-%m-%Y %H:%M")-datetime.strptime(x["started_at"], "%d-%m-%Y %H:%M")).total_seconds(), axis=1)
    bike = bike[bike["duration"]>0]
    
    max_duration = bike["duration"].max()
    min_duration = bike["duration"].min()
    number_of_min_duration = len(bike[bike["duration"]==min_duration])
    num_circular_trips = len(bike[(bike["start_lat"]==bike["end_lat"]) &(bike["start_lng"]==bike["end_lat"])])
    total_trips = len(bike)
    percent_circular_trips = num_circular_trips*100/total_trips
    print("Maximum Duration of trips(in minutes): ", max_duration/60)
    print("Minimum Duration of trips(in minutes): ", min_duration/60 )
    print("Total number of minimum duration trips: ", number_of_min_duration)
    print("Percentage of circular trips: ", percent_circular_trips)
    ending_time = time.time()
    print("Time taken by the function(in seconds): ", ending_time-startin_time)

duration_func()

#part 2 of question 1

starting = time.time()
filename = "bike_data_new.csv"

bike = pd.read_csv(filename)
bike["duration"] = bike.apply(lambda x: (datetime.strptime(x["ended_at"], "%d-%m-%Y %H:%M")-datetime.strptime(x["started_at"], "%d-%m-%Y %H:%M")).total_seconds(), axis=1)
bike = bike[bike["duration"]>0]



bike['start_hr'] = bike.apply(lambda x: int(datetime.strptime(x["started_at"], "%d-%m-%Y %H:%M").strftime("%H")), axis=1)
bike['end_hr'] = bike.apply(lambda x: int(datetime.strptime(x["ended_at"], "%d-%m-%Y %H:%M").strftime("%H")), axis=1)
bike = bike[(bike["start_hr"]>=6) & (bike["end_hr"]<=18)]
bike["started_at"] = pd.to_datetime(bike["started_at"], format="%d-%m-%Y %H:%M")
bike["ended_at"] = pd.to_datetime(bike["ended_at"], format="%d-%m-%Y %H:%M")

end_locations = bike[['trip_id', 'end_lat', 'end_lng', 'ended_at']]

end_locations = end_locations.rename(columns={'end_lat':'start_lat', 'end_lng': 'start_lng'})


merged_df = pd.merge(bike, end_locations, on=['start_lat', 'start_lng'], suffixes=('_start', '_end'))
print(merged_df)


feasible_pairs = merged_df[(merged_df['ended_at_end'] <= merged_df['started_at']) & (merged_df['trip_id_start'] != merged_df['trip_id_end'])]


total_feasible_pairs = len(feasible_pairs)
ending = time.time()
    

print(total_feasible_pairs)
print("time: ", ending-starting)


