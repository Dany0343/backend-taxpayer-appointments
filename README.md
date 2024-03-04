# KEA Developer Position Takehome Test Solution

## Assumptions
In the development of this solution, several assumptions have been made:
- The `taxpayers.json` file will always be well-structured and contain the expected data fields.
- For the scoring algorithm, higher values of `"canceled_offers"` and `"average_reply_time"` are considered negative. This reflects the intuition that clients who cancel more often or take longer to reply are less likely to accept an offer.

## Installation and Setup
Before running the script, ensure you have Python installed on your system. This script was developed with Python 3 in mind. Follow these steps to set up and run the script:

1. **Install Required Libraries**: The script relies on a few external libraries, such as `pandas` and `geopy`. Install them by running the following command in your terminal:
   ```
   pip install -r requirements.txt
   ```

2. **Data File**: Make sure the `taxpayers.json` file exists in the `./sample-data` directory and is populated with data. This file is essential for the script to run properly.

3. **Office Location**: If necessary, you can change the office location used in the calculations. This is set on line 12 of the script as follows:
   ```python
   office_location = (19.3797208, -99.1940332) # Change if necessary
   ```
   Adjust the latitude and longitude values to match the desired office location.

## Running the Script
Execute the script by running the following command in your terminal:
```
python main.py
```
This will process the data in `taxpayers.json`, calculate scores for each client, and output two JSON files:
- `sorted_taxpayers.json`: Contains all clients from the input file, sorted by their score from highest to lowest.
- `top_10_taxpayers.json`: Extracts the top 10 clients with the highest scores from `sorted_taxpayers.json`.
```