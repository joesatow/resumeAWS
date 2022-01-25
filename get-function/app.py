import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
  data = client.scan(
    TableName='visitors'
  )

  response = {
      'statusCode': 200,
      'body': json.dumps(data['Items'][0]['count']),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }

  return response
