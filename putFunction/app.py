import boto3
import json

client = boto3.client('dynamodb')

def lambda_handler(event, context):
  data = client.scan(
    TableName='visitors'
    )
  #y = json.loads(data.decode('utf-8'))
  oldNum = int(data["Items"][0]["count"]["N"])
  newNum = oldNum+1

  data = client.update_item(
    TableName='visitors',
    Key={
        'ID': {'S':'visitors'}
    },
    ExpressionAttributeNames = {
    '#ct': 'count'
    },
    UpdateExpression="set #ct = :newNum",
    ExpressionAttributeValues={
        ':newNum': {
            "N":str(newNum)
        }
    }
  )

  response = {
      'statusCode': 200,
      'body': 'successfully updated item!',
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }

  return response
