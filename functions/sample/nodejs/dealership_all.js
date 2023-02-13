const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');


async function main(params) {
      var params = {
          IAM_API_KEY: "",
          COUCH_URL: ""
      }
      const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
      const service = CloudantV1.newInstance({
          authenticator: authenticator
      });
      service.setServiceUrl(params.COUCH_URL);
      try {
       var response = service.postAllDocs({
         db: 'dealerships',
         includeDocs: true
        
          });
          var response2={};
        
        return response; 

        
     
      } catch (error) {
          return { error: error.description };
      }
}