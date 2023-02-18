import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth


def get_request(url, api_key=None,**kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        if api_key:
            auth=HTTPBasicAuth('apikey', api_key)
            response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs, auth=auth)
        else:
            response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

def analyze_review_sentiments(dealerreview):
    params = dict()
    url="https://api.us-east.natural-language-understanding.watson.cloud.ibm.com/instances/d26f17a4-697c-4484-b809-fc3993c16fb4/v1/analyze"
    api_key="HX_Uxh7Q7CacZ_qf0F1yHywCl9orlVQ3DU8aRXbDrh0D"
    params["text"] = dealerreview
    params["version"] = "2022-04-07"
    params["features"] = "sentiment"
    params["return_analyzed_text"] = True
    response = get_request(url=url, api_key=api_key, **params)
    print (response)
    return response

def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    print (json_result)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["result"]["rows"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)
            
        result_dict = {}
        result_dict["dealership_list"]=results 
        #for x in results:
           # name = x.id
           # result_dict[name] = x
    return result_dict

def get_dealer_reviews_from_cf(url, **kwargs):
    results = []
    json_result=get_request(url, **kwargs)
    #print (json_result)

    if json_result:
        reviews=json_result["docs"]
        #print(reviews)

        for review in reviews:
            review_doc=review
            #print(review_doc["dealership"])
            sentiment_response = analyze_review_sentiments(review_doc["review"])
            
            try:
                sentiment=sentiment_response['sentiment']['document']['label']
            except:
                sentiment = " "

            review_obj = DealerReview (dealership=review_doc["dealership"],name=review_doc["name"],purchase=review_doc["purchase"],review=review_doc["review"], purchase_date=review_doc["purchase_date"],car_make=review_doc["car_make"],car_model=review_doc["car_model"],car_year=review_doc["car_year"], id=review_doc["id"],sentiment=sentiment)
            results.append(review_obj)
    return results

def post_request(url, json_payload, **kwargs):
     response = requests.post(url, params=kwargs,json=json_payload)
     return response



# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)







