import datetime
import requests
import json
import sys
import pprint
today = datetime.date.today()
apidate = today.strftime('%Y-%m-%d')
r = requests.get('https://www.ewtn.com/se/readings/readingsservice.svc/day/'+apidate+'/en')
data = json.loads(r.text)
#print(apidate)

d = 0
ref = {}
what = {}
payload = {}

for reading in data['ReadingGroups'][0]['Readings']:
    ref[d] = reading['Citations'][0]['Reference']
    what[d] = reading['Type']
    d = d + 1;

payload["Language"] = "en"
payload["References"] = ref
if(len(ref)==3):
    payload = {"References":[ref[2]],"Language":"en"};
else:
    payload = {"References":[ref[3]],"Language":"en"};
headers = {"Referer":"https://www.ewtn.com/daily-readings/","content-type":"application/json"}
r = requests.post("https://www.ewtn.com/se/readings/readingsservice.svc/books", data=json.dumps(payload), headers=headers)
verses = json.loads(r.text)
print(verses[0]['Reference'])
def prettyreadings(readings_input):
    r = 0
    for i in range(0,len(readings_input)):
        print(verses[0]['Chapters'][0]['Verses'][r]['Number'], end=". ")
        print(verses[0]['Chapters'][0]['Verses'][r]['Text'], end="")
        r = r+1
prettyreadings(verses[0]['Chapters'][0]['Verses'])


#pprint.pprint(verses)
sys.stdout.flush()

##{'Color': 'Violet',
##'Date': '2018-02-26',
##'Note': 'Total Consecration- Day 7',
##'ReadingGroups': [{'Name': 'Default', 'Note': None,
##	'Readings': [{
##		'Citations':
##		[{'Note': None, 'Reference': 'Daniel 9:4-10'}],
##			'Type': 'Reading 1'},
##			{'Citations':
##				[{'Note': None, 'Reference': 'Psalms 79:8-9, 11, 13'}],
##			'Type': 'Psalm'},
##			{'Citations': [{'Note': None, 'Reference': 'Luke 6:36-38'}],
##			'Type': 'Gospel'}]}],
##			'Title': 'Lenten Weekday'}

#[{"Chapters":
#	[{"Number":20,
#		"Verses":[{"Number":17,
#					"Text":"And as Jesus was going up to Jerusalem, he took the twelve disciples aside, and on the way he said to them,    "},
#				{"Number":18,
#					"Text":"\"Behold, we are going up to Jerusalem; and the Son of man will be delivered to the chief priests and scribes, and they will condemn him to death,  "},
#				{"Number":19,
#					"Text":"and deliver him to the Gentiles to be mocked and scourged and crucified, and he will be raised on the third day.\"  "},
#				{"Number":20,
#					"Text":"Then the mother of the sons of Zeb'edee came up to him, with her sons, and kneeling before him she asked him for something.    "},
#				{"Number":21,
#					"Text":"And he said to her, \"What do you want?\" She said to him, \"Command that these two sons of mine may sit, one at your right hand and one at your left, in your kingdom.\"  "},
#				{"Number":22,
#					"Text":"But Jesus answered, \"You do not know what you are asking. Are you able to drink the cup that I am to drink?\" They said to him, \"We are able.\"  "},
#				{"Number":23,
#					"Text":"He said to them, \"You will drink my cup, but to sit at my right hand and at my left is not mine to grant, but it is for those for whom it has been prepared by my Father.\"  "},
#				{"Number":24,
#					"Text":"And when the ten heard it, they were indignant at the two brothers.  "},
#				{"Number":25,
#					"Text":"But Jesus called them to him and said, \"You know that the rulers of the Gentiles lord it over them, and their great men exercise authority over them.  "},
#				{"Number":26,
#					"Text":"It shall not be so among you; but whoever would be great among you must be your servant,  "},
#				{"Number":27,
#					"Text":"and whoever would be first among you must be your slave;  "},
#				{"Number":28,
#					"Text":"even as the Son of man came not to be served but to serve, and to give his life as a ransom for many.\"  "}
#				]
#			}
#		],
#"Name":"Matthew","Reference":"Matthew 20:17-28","Verses":"20:17-28"}]
