# Libraries
import pandas as pd
from geopy.distance import geodesic

# Weights and constants
age_weight = 0.1
distance_weight = 0.1
accepted_offers_weight = 0.3
cancelled_offers_weight = 0.3
average_reply_time_weight = 0.2

office_location = (19.3797208, -99.1940332) # Change if necessary


# main function
def main():
    # Reading data
    global df
    df = read_data()
    
    # Once is loaded we can iterate over it
    iterate_data()


def read_data():
    # Load the JSON file into a DataFrame and return
    return pd.read_json('./sample-data/taxpayers.json')


def iterate_data():
    # Create normalized variables for all the values

    # Adding distances to df to get min and max values
    df['distance_to_office'] = df.apply(calculate_distances, axis=1) # Apply calculate_distances function to the dataframe

    # Create score column
    df['score'] = None

    # Age min and max
    age_max = df['age'].max()
    age_min = df['age'].min()

    # Acepted offers min and max
    accepted_offers_max = df['accepted_offers'].max()
    accepted_offers_min = df['accepted_offers'].min()

    # Canceled offers min and max
    canceled_offers_max = df['canceled_offers'].max()
    canceled_offers_min = df['canceled_offers'].min()

    # Average reply min and max
    average_reply_time_max = df['average_reply_time'].max()
    average_reply_time_min = df['average_reply_time'].min()

    # Distance min and max
    distance_max = df['distance_to_office'].max()
    distance_min = df['distance_to_office'].min()
    
    for index,row in df.iterrows():
        # Access row columns using row['column_name'] and pass the row and min and max to the normalize_data function to get the normalized value
        age_normalized = normalize_data(row['age'], age_min, age_max)
        accepted_offers_normalized = normalize_data(row['accepted_offers'], accepted_offers_min, accepted_offers_max)
        canceled_offers_normalized = normalize_data(row['canceled_offers'], canceled_offers_min, canceled_offers_max)
        average_reply_time_normalized = normalize_data(row['average_reply_time'], average_reply_time_min, average_reply_time_max)
        distance_normalized = normalize_data(row['distance_to_office'], distance_min, distance_max)

        score = (age_normalized * age_weight + 
                 accepted_offers_normalized * accepted_offers_weight + 
                 canceled_offers_normalized * cancelled_offers_weight + 
                 average_reply_time_normalized * average_reply_time_weight + 
                 distance_normalized * distance_weight) * 10
        
        df.at[index, 'score'] = score

    # Sort Dataframe and export it to JSON
    sort_and_make_json()


def normalize_data(row, min_value, max_value):
    # I'm gonna use mim-max normalization to get a numeric value and then multiply it by its weight
    normalized = (row - min_value) / (max_value - min_value)

    return normalized


# Using geodesic to calculate distances from office to client location
def calculate_distances(row):
    client_location = row['location']['latitude'], row['location']['longitude']
    distance = geodesic(office_location, client_location).kilometers 
    return distance    


def sort_and_make_json():
    # Eliminate distance to office column because it's no loger used
    # df.drop('distance_to_office', axis=1, inplace=True)

    # Sort df by "score" column
    df_sorted = df.sort_values(by='score', ascending=False)

    # Export it to a JSON
    df_sorted.to_json('sorted_taxpayers.json', orient='records')

    # Look for the top 10 and export it to a JSON
    top_10_clients = df_sorted.head(10)
    top_10_clients.to_json('top_10_taxpayers.json', orient='records')

if __name__ == "__main__":
    main()