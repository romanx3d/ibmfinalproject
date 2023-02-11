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
    
    #param_dict2 = {"dealerid": "2" }
    """Main Function

    Args:
        param_dict (Dict): input paramater

    Returns:
        _type_: _description_ TODO
    """
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
    
    if param_dict2["dealerid"] is not None:
        response = service.post_find(db='reviews',selector={'dealership': {'$eq': int(param_dict2["dealerid"])}}).get_result()
        #response = service.post_all_docs( db='dealerships',include_docs=True).get_result()
        
    #response = service.post_all_docs( db='dealerships',include_docs=True).get_result()
    #all_docs_query1 = AllDocsQuery(keys=['5530363f68d3002ea17f7c99a30512aa', '5530363f68d3002ea17f7c99a305209c'])
    #response = service.post_all_docs_queries(db='dealerships',queries=[all_docs_query1]).get_result()

    #response = service.get_document(db='dealerships',doc_id='5530363f68d3002ea17f7c99a30512aa').get_result()
    return response
    #return {"dbs": service.get_all_dbs().get_result()}
    
 
