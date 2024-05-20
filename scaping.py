import requests
import pandas as pd
import csv
import re

json_headline = requests.get(
    "https://sabq.org/route-data.json?path=%2Fmoment-by-moment").json()

for item in json_headline['data']['collection']['items']:
    json_stroy = requests.get("https://sabq.org/api/v1/stories-by-slug?slug=" +
                              item['story']['slug']).json()
    for headline in item['item']['headline']:
        print("Headline: " + re.sub("<[^>]+>", "", headline))

        for item in json_stroy['story']['cards']:
            for story in item['story-elements']:

                if 'text' in story:
                    print("Story : " + re.sub("<[^>]+>", "", story['text']))
                else:
                    print('The text key does not exist.')
