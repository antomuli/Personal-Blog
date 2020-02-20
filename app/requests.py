import urllib.request,json

def get_quote():
    '''
    Function to get random quote
    '''

    quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(quote_url) as url:
        quote_data = url.read()
        quote_response = json.loads(quote_data)

        
        return quote_response

        