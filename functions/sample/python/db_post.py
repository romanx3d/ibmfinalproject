"""IBM Cloud Function that gets all reviews for a dealership

Returns:
    List: List of reviews for the given dealership
    
"""

from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1, Document, AllDocsQuery
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests




def main(param_dict2):
    param_dict = {
    "IAM_API_KEY": "",
    "DB_URL": ""
}
    
    

  
    try:
        authenticator = IAMAuthenticator(param_dict["IAM_API_KEY"])
        service = CloudantV1(authenticator=authenticator)
        service.set_service_url(param_dict["DB_URL"])
   
        #print(f"Databases: {service.all_dbs()}")
    except ApiException as ae:
        print("Method failed")
        print(" - status code: " + str(ae.code))
        print(" - error message: " + ae.message)
        if ("reason" in ae.http_response.json()):
            print(" - reason: " + ae.http_response.json()["reason"])
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}
    
    if param_dict2 is not None:
        get_count = service.get_database_information(db='reviews').get_result()
        
        docid1= get_count["doc_count"] + 1
        
        param_dict2["review"]["id"] = docid1

        
        response = service.post_document(db='reviews', document=param_dict2['review']).get_result()


        
    return response
    #return {"dbs": service.get_all_dbs().get_result()}
    
 
