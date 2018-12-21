import http.client
import json
import os

elasticsearch = os.environ.get('ES_HOST')
s3_bucket_name = os.environ.get('S3_BUCKET_NAME')
aws_access_key = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
aws_region = os.environ.get('AWS_REGION')
task_name = os.environ.get('SNAPSHOT_S3_TASK')
headers = {'Content-type': 'application/json'}
task = {"type":"s3","settings":{"bucket": s3_bucket_name,"region":aws_region,"access_key":aws_access_key,"secret_key":aws_secret_key, "compress": True}}
json_task = json.dumps(task)

path = "/_snapshot/" + task_name
es_uri = elasticsearch + ":9200"
connection = http.client.HTTPConnection(es_uri)
connection.request('POST', path, json_task, headers)
response = connection.getresponse()
print(response.read().decode())

#{"acknowledged":true}
