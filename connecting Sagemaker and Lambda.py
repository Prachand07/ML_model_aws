import boto3
import json

def lambda_handler(event, context):
    print("Event:", event)
    
    if 'body' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': "'body' missing in the event"})
        }
    
    sagemaker_runtime = boto3.client('runtime.sagemaker')

    try:
        response = sagemaker_runtime.invoke_endpoint(
            EndpointName='sagemaker-scikit-learn-2024-08-18-09',
            ContentType='application/json',
            Body=json.dumps(input_data)
        )
        result = json.loads(response['Body'].read().decode())
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'predicted_sales': result})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }