const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');


async function main(params) {
      var params2 = {
          IAM_API_KEY: "",
          COUCH_URL: ""
      }
      const authenticator = new IamAuthenticator({ apikey: params2.IAM_API_KEY })
      const service = CloudantV1.newInstance({
          authenticator: authenticator
      });
      service.setServiceUrl(params2.COUCH_URL);
      try {
        
          
       var selector= CloudantV1.JsonObject = {
  state: {
    '$regex': params["state"]
  }
};
          
       var response = service.postFind({
         db: 'dealerships',
         selector: selector
         
        
          });
          var response2={};
        
        return response; 

        
     
      } catch (error) {
          return { error: error.description };
      }
}