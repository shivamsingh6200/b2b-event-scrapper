import requests
from bs4 import BeautifulSoup
import json

event_urls = [
    'https://b2bmarketingleaders.com.au/singapore/',
    'https://www.marketingaiinstitute.com/events/marketing-artificial-intelligence-conference',
    'https://events.joinpavilion.com/gtm2024?utm_medium=banner&utm_campaign=GTM2024&utm_source=Website&utm_content=&utm_term=',
    'https://www.eventbrite.com/e/engage-2024-tickets-781606475007',
    'https://www.saastrannual2024.com/',
]

events_data = []

# scraping 'https://b2bmarketingleaders.com.au/singapore/'
response = requests.get(event_urls[0])
soup = BeautifulSoup(response.content, 'html.parser')

main_div = soup.find('div', class_='col-md-6 col-sm-push-1 col-sm-10 intro-txt white-color')
headings_text = []

for heading in main_div.find_all(['h2', 'h3', 'h4']):
    headings_text.append(heading.get_text(strip=True))

event_name = headings_text[1]
event_date, location = headings_text[0].split('|')
description = headings_text[2]

ul_element = soup.find('ul', class_='speakers-wrapper')
speaker_names = []
li_elements = ul_element.find_all('li')

for li in li_elements:
    h2 = li.find('h2')
    if h2:
        a_tag = h2.find('a')
        if a_tag:
            speaker_names.append(a_tag.get_text(strip=True))

key_speakers = speaker_names

categories = []

all_divs = soup.find_all('div', class_='wpb_column vc_column_container vc_col-sm-4')
for div in all_divs[:18]:
    inner = div.find('div', class_='vc_column-inner')
    wrapper = inner.find('div', class_='wpb_wrapper')
    category = wrapper.find('h3').get_text(strip=True)
    categories.append(category)

events_data.append({
'Event Name': event_name,
'Event Date(s)': event_date,
'Location': location,
'Website URL': event_urls[0],
'Description': description,
'Key Speakers': key_speakers,
'Agenda/Schedule': "",
'Registration Details': "",
'Pricing': "",
'Categories': categories,
'Audience Type': "",
})


# scraping 'https://www.marketingaiinstitute.com/events/marketing-artificial-intelligence-conference'
response = requests.get(event_urls[1])
soup = BeautifulSoup(response.content, 'html.parser')

all_divs = soup.find('div', class_='hhs-rich-text')
event_name, event_date, location = list(map(lambda x: x.get_text(), all_divs.find_all('h1')))


key_speakers = []
profile_cards = soup.find_all('div', class_='hhs-profile-card')
for profile_card in profile_cards:
    profile_content = profile_card.find('div', class_='hhs-profile-content')
    key_speakers.append(profile_content.find('h4').get_text(strip=True))

description = soup.find('p').get_text()

response = requests.get('https://www.marketingaiinstitute.com/events/marketing-artificial-intelligence-conference/agenda')
soup = BeautifulSoup(response.content, 'html.parser')
agenda = soup.find('h3').get_text()

events_data.append({
'Event Name': event_name,
'Event Date(s)': event_date,
'Location': location,
'Website URL': event_urls[1],
'Description': description,
'Key Speakers': key_speakers,
'Agenda/Schedule': agenda,
'Registration Details': "",
'Pricing': "",
'Categories': categories,
'Audience Type': "",
})

# scraping 'https://events.joinpavilion.com/gtm2024?utm_medium=banner&utm_campaign=GTM2024&utm_source=Website&utm_content=&utm_term='
response = requests.get(event_urls[2])
soup = BeautifulSoup(response.content, 'html.parser')

event_name = soup.find('h2', class_='xxxl-blue').get_text()
description = soup.find('div', class_='atom-main full-width margin-custom-element element-12384895').find('div').find('p').get_text()
location, event_date = soup.find('h4', class_='headline-m white').get_text(strip=True).split('|')

events_data.append({
    'Event Name': event_name,
    'Event Date(s)': event_date,
    'Location': location,
    'Website URL': event_urls[2],
    'Description': description,
    'Key Speakers': "",
    'Agenda/Schedule': "",
    'Registration Details': "",
    'Pricing': "",
    'Categories': "",
    'Audience Type': "",
})

# scraping 'https://www.eventbrite.com/e/engage-2024-tickets-781606475007'
response = requests.get(event_urls[3])
soup = BeautifulSoup(response.content, 'html.parser')

event_name = soup.find('h1', class_='event-title css-0').get_text(strip=True)
event_date = soup.find('span', class_='date-info__full-datetime').get_text(strip=True)
location = soup.find('p', class_='location-info__address-text').get_text(strip=True)
description = soup.find('div', class_='eds-text--left').get_text(strip=True)

events_data.append({
    'Event Name': event_name,
    'Event Date(s)': event_date,
    'Location': location,
    'Website URL': event_urls[3],
    'Description': description,
    'Key Speakers': "",
    'Agenda/Schedule': "",
    'Registration Details': "",
    'Pricing': "",
    'Categories': "",
    'Audience Type': "",
})


# scrap 'https://www.saastrannual2024.com/'
response = requests.get(event_urls[4])
soup = BeautifulSoup(response.content, 'html.parser')

event_name = soup.find('div', class_='sqs-html-content').find('h1').get_text(strip=True)
event_date, location = soup.find('div', class_='sqs-html-content').find('h4').get_text(strip=True).split('|')
description = soup.find('div', class_='sqs-block html-block sqs-block-html').find('div', class_='sqs-block-content').find('div', class_='sqs-html-content').get_text(strip=True)

key_speakers = []
audience_type = []
speakers_list = soup.find('ul', class_='user-items-list-item-container user-items-list-simple').find_all('li')
for speaker in speakers_list:
    speaker_name = speaker.find('div', class_='list-item-content').find('div').find('div').find('p').get_text().split(',')
    key_speakers.append(speaker_name[0])
    audience_type.append(speaker_name[1])

events_data.append({
    'Event Name': event_name,
    'Event Date(s)': event_date,
    'Location': location,
    'Website URL': event_urls[0],
    'Description': description,
    'Key Speakers': key_speakers,
    'Agenda/Schedule': "",
    'Registration Details': "",
    'Pricing': "",
    'Categories': "",
    'Audience Type': audience_type,
})

with open('b2b_events.json', 'w') as f:
    json.dump(events_data, f, indent=4)
    
print("Scraping completed and data saved to b2b_events.json")