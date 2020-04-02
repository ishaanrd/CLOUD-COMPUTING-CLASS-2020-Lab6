import boto3
client = boto3.client('lambda') # accessing lambda funtion

response = client.create_function(FunctionName='serverless-cotroller',Runtime='python3.6',
                                  Role='arn:aws:iam::952638762329:role/service-role/serverless-controller-role',
                                  Handler='lambda_function.lambda_handler')

response = client.create_rest_api(name='myFunction-anant')
apiID = response['id']

req2 = client.get_resources(restApiId=apiID)

parentID = req2['items'][0]['id']

req3 = client.create_resource(
    restApiId=apiID,
    parentId=parentID,
    pathPart='serverless-controller2'
)

resourceID = req3['id']

final = client.put_integration(restApiId=apiID,resourceId=resourceID,
                            httpMethod='ANY',type='HTTP',integrationHttpMethod='ANY')

