"""https://lepczynski.it/en/aws_en/how-to-automatically-copy-data-from-aws-s3-lambda-events/
permet de copier le contenu d'un S3 vers un autre S3
"""

import boto3
import json

s3 = boto3.resource('s3')

def lambda_handler (event, context):
 bucket = s3.Bucket('test-ndgegy4364gdu-source-bucket')
 dest_bucket=s3.Bucket('test-ndgegy4364gdu-destination-bucket')

 print(dest_bucket)
 print(bucket)
 
 for obj in bucket.objects.filter(Prefix='images/',Delimiter='/'):
  dest_key=obj.key
  print(dest_key)
  print('copy file ' + dest_key)
  s3.Object(dest_bucket.name, dest_key).copy_from(CopySource= {'Bucket': obj.bucket_name, 'Key': obj.key})
  print('delete file from source bucket ' + dest_key)
  s3.Object(bucket.name, obj.key).delete()
