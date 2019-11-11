import shodan 

string=input("\n\nEnter word you wish to search for in quotes : ")

SHODAN_API_KEY = "XGPN8vDnyZ0YYNL1Lp6vnHNPFpAmDd3e"

api = shodan.Shodan(SHODAN_API_KEY)

try:
        # Search Shodan
        results = api.search(string)
	# Show the results	
	print 'Results found: %s' % results['total']
	for result in results['matches']:
		print 'IP: %s' % result['ip_str']
		print result['data']
		print ''
	
except shodan.APIError, e:
	print 'Error: %s' % e
