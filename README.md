# KEA Technical Interview

## Overview

This is a takehome test for candidates applying for a developer position at KEA.


## Problem Definition

Fixat has a list of clients(aka taxpayers) waiting to schedule an appointment with an accountant. The waitlist is created sequentially (e.g. clients are added in a fifo order) from the time the client calls.  Once there is an availability, the front desk calls each client to offer the appointment in the order they were added to the waitlist. The staff member from the front desk has noticed that she wastes a lot of time trying to find a client from the waitlist since they&#39;re often not available, don&#39;t pick up the phone, etc.  She would like to generate a better list that will increase her chances of finding a client in the first few calls.

## Interview Task

Given client demographics and behavioral data (see sample-data/taxpayers.json), create an algorithm that will process a set of historical client data and compute a score for each client that (1 as the lowest, 10 as the highest) that represents the chance of a client accepting the offer off the waitlist. Take in consideration that clients who have little behavior data should be randomly added to the top list as to give them a chance to be selected. Create an api or script that takes a Fixat's office location (latitude and longitud coordinates) as input and **returns an ordered list of 10 clients who will most likely accept the appointment offer, each client must include their computed score.**

Example of input Fixat's office location
```
Latitude: 19.3797208
Longitude: -99.1940332
```

Example of response with an taxpayer list of client
```
[
    {
        "id": "0a5d2f34-6baa-4455-a3e7-0682c2094cac",
        "name": "Jorge Sullivan",
        "location": {
            "latitude": 20.28527,
            "longitude": -103.42897
        },
        "age": 56,
        "accepted_offers": 61,
        "canceled_offers": 45,
        "average_reply_time": 2390,
        "score": 10
    },
    ...,
    {
        "id": "23c6612f-4826-4673-a3a7-711a81332876",
        "name": "Lisa King",
        "location": {
            "latitude": 17.94979,
            "longitude": -94.91386
        },
        "age": 86,
        "accepted_offers": 90,
        "canceled_offers": 77,
        "average_reply_time": 602,
        "score": 8
    }
]
```

## Weighting Categories

Demographic

- age  (weighted 10%)
- distance to office (weighted 10%)

Behavior

- number of accepted offers (weighted 30%)
- number of cancelled offers (weighted 30%)
- reply time (how long it took for clients to reply) (weighted 20%)

## Client Model

- ID
- Age (in years)
- location
  - Lat
  - long
- accepted_offers (integer)
- canceled_offers (integer)
- average_reply_time (integer, in seconds)

## Deliverables

The code should be written in Python 3 with the instructions to run the script or API.

Feel free to structure the code however you prefer and use third-party libraries at your discretion.

## Duration

Up to 72 hours. We do not expect you to complete the assessment in this time.

## Submission
1.  Fork this repo
3.  Once you've completed the test, submit a Pull Request (PR)
3.  In the PR, include a README that includes the following:
    -  If you made any assumptions, what are they

**Notes:**
1.  Feel free to contact me if you have any questions about the test.
2.  Feel free to generate more sample data to test your algorithm. 
    - **See the Python script:** `sample-data/generate_data.py` 

Thanks!
