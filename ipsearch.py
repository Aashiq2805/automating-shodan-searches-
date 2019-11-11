import shodan 

string=input("\n\nEnter word you wish to search for in quotes : ")

SHODAN_API_KEY = "XGPN8vDnyZ0YYNL1Lp6vnHNPFpAmDd3e"

api = shodan.Shodan(SHODAN_API_KEY)

try:
        # Search Shodan
        results = api.search(string)
	# Show the results	
	for result in results['matches']:
		print '%s' % result['ip_str']
	
except shodan.APIError, e:
	print 'Error: %s' % e
