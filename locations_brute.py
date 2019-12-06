us_states = {
'alabama': 0,
'alaska': 0,
'arizona': 0,
'arkansas': 0,
'california': 0,
'colorado': 0,
'connecticut': 0,
'delaware': 0,
'district of columbia': 0,
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
'new hampshire': 0,
'new jersey': 0,
'new mexico': 0,
'new york': 0,
'north carolina': 0,
'north dakota': 0,
'ohio': 0,
'oklahoma': 0,
'oregon': 0,
'pennsylvania': 0,
'rhode island': 0,
'south carolina': 0,
'south dakota': 0,
'tennessee': 0,
'texas': 0,
'utah': 0,
'vermont': 0,
'virginia': 0,
'washington': 0,
'west virginia': 0,
'wisconsin': 0,
'wyoming': 0,
}

states_map = {
        'AK': 'alaska',
        'AL': 'alabama',
        'AR': 'arkansas',
        'AS': 'american samoa',
        'AZ': 'arizona',
        'CA': 'california',
        'CO': 'colorado',
        'CT': 'connecticut',
        'DC': 'district of columbia',
        'DE': 'delaware',
        'FL': 'florida',
        'GA': 'georgia',
        'GU': 'guam',
        'HI': 'hawaii',
        'IA': 'iowa',
        'ID': 'idaho',
        'IL': 'illinois',
        'IN': 'indiana',
        'KS': 'kansas',
        'KY': 'kentucky',
        'LA': 'louisiana',
        'MA': 'massachusetts',
        'MD': 'maryland',
        'ME': 'maine',
        'MI': 'michigan',
        'MN': 'minnesota',
        'MO': 'missouri',
        'MS': 'mississippi',
        'MT': 'montana',
        'NA': 'national',
        'NC': 'north carolina',
        'ND': 'north dakota',
        'NE': 'nebraska',
        'NH': 'new hampshire',
        'NJ': 'new jersey',
        'NM': 'new mexico',
        'NV': 'nevada',
        'NY': 'new york',
        'OH': 'ohio',
        'OK': 'oklahoma',
        'OR': 'oregon',
        'PA': 'pennsylvania',
        'PR': 'puerto rico',
        'RI': 'rhode island',
        'SC': 'south carolina',
        'SD': 'south dakota',
        'TN': 'tennessee',
        'TX': 'texas',
        'UT': 'utah',
        'VA': 'virginia',
        'VI': 'virgin islands',
        'VT': 'vermont',
        'WA': 'washington',
        'WI': 'wisconsin',
        'WV': 'west virginia',
        'WY': 'wyoming'
}

states = {"AL":0, "AK":0, "AZ":0, "AR":0, "CA":0, "CO":0, "CT":0, "DC":0, "DE":0, "FL":0, "GA":0, 
          "HI":0, "ID":0, "IL":0, "IN":0, "IA":0, "KS":0, "KY":0, "LA":0, "ME":0, "MD":0, 
          "MA":0, "MI":0, "MN":0, "MS":0, "MO":0, "MT":0, "NE":0, "NV":0, "NH":0, "NJ":0, 
          "NM":0, "NY":0, "NC":0, "ND":0, "OH":0, "OK":0, "OR":0, "PA":0, "RI":0, "SC":0, 
          "SD":0, "TN":0, "TX":0, "UT":0, "VT":0, "VA":0, "WA":0, "WV":0, "WI":0, "WY":0}


count = 0

import collections

with open('vape_locations_clean.txt') as topo_file:
    for line in topo_file:

        line_lower = line.lower()

        for key in us_states:
            if(key in line_lower):
                us_states[key] = us_states[key] + 1
                continue
     
        for key2 in states:
            if(key2 in line):
                state_name = states_map[key2]
                us_states[state_name] = us_states[state_name] + 1
                continue


for key3 in us_states:
    print(str(key3) + " , " + str(us_states[key3]))

        
        



