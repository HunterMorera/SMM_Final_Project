us_states = {
'alabama': 0,
'alaska': 0,
'arizona': 0,
'arkansas': 0,
'california': 0,
'colorado': 0,
'connecticut': 0,
'delaware': 0,
'districtofcolumbia': 0,
'florida': 0,
'georgia': 0,
'hawaii': 0,
'idaho': 0,
'illinois': 0,
'indiana': 0,
'iowa': 0,
'kansas': 0,
'kentucky': 0,
'louisiana': 0,
'maine': 0,
'maryland': 0,
'massachusetts': 0,
'michigan': 0,
'minnesota': 0,
'mississippi': 0,
'missouri': 0,
'montana': 0,
'nebraska': 0,
'nevada': 0,
'newhampshire': 0,
'newjersey': 0,
'newmexico': 0,
'newyork': 0,
'northcarolina': 0,
'northdakota': 0,
'ohio': 0,
'oklahoma': 0,
'oregon': 0,
'pennsylvania': 0,
'rhodeisland': 0,
'southcarolina': 0,
'southdakota': 0,
'tennessee': 0,
'texas': 0,
'utah': 0,
'vermont': 0,
'virginia': 0,
'washington': 0,
'westvirginia': 0,
'wisconsin': 0,
'wyoming': 0,
}

states_map = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

states = {"AL":0, "AK":0, "AZ":0, "AR":0, "CA":0, "CO":0, "CT":0, "DC":0, "DE":0, "FL":0, "GA":0, 
          "HI":0, "ID":0, "IL":0, "IN":0, "IA":0, "KS":0, "KY":0, "LA":0, "ME":0, "MD":0, 
          "MA":0, "MI":0, "MN":0, "MS":0, "MO":0, "MT":0, "NE":0, "NV":0, "NH":0, "NJ":0, 
          "NM":0, "NY":0, "NC":0, "ND":0, "OH":0, "OK":0, "OR":0, "PA":0, "RI":0, "SC":0, 
          "SD":0, "TN":0, "TX":0, "UT":0, "VT":0, "VA":0, "WA":0, "WV":0, "WI":0, "WY":0}


count = 0

# import geocoder
# from geopy.geocoders import Nominatim
# import tqdm as tqdm

outfile = open("all_age_states.txt",'a')

from geocodio import GeocodioClient


tweet_list = []

count = 0

with open('all_age_locations_clean.txt') as topo_file:
    for line in topo_file:

        count += 1

        print(count)

        try:

            client = GeocodioClient("2f4d4b6ef25a45b4e5d50df4be45d4e4fda24da")

            geocoded_location = client.geocode(line)

            coordinates = geocoded_location.coords

            location = client.reverse(coordinates)

            result = location['results'][0]['address_components']['state']

            states[result] = states[result] + 1

        except:
            continue





for key in states:
    outfile.write(str(key) + " , " + str(states[key]))
    outfile.write("\n")





