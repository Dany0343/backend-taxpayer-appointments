###########################################################
#                                                         #
#   Sample data generation script                        #
#   Usage:                                                #
#     1. Install Faker library: pip3 install Faker        #
#     2. Run the script: python3 generate_data.py         #
#                                                         #
###########################################################

from faker import Faker
import json

fake = Faker()
Faker.seed(0)

taxpayers = []

for _ in range(1000):
    geolocation = fake.local_latlng(country_code="MX")
    taxpayer = {
        "id": fake.uuid4(),
        "name": fake.name(),
        "location": {
          "latitude":float(geolocation[0]),
          "longitude":float(geolocation[1])
        },
        "age" : fake.random_int(18, 90),
        "accepted_offers" : fake.random_int(0, 100),
        "canceled_offers" : fake.random_int(0, 100),
        "average_reply_time" : fake.random_int(1, 3600),
    }
    taxpayers.append(taxpayer)

# Writing to taxpayers.json
with open("taxpayers.json", "w") as outfile:
    outfile.write(json.dumps(taxpayers))