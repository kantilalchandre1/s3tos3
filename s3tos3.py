import json
import boto3

s3_client = boto3.client(
    's3',
    aws_access_key_id='AKIA6OXVQAOSU7PXS6PW',
    aws_secret_access_key='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',
    
)
source_bucket = 'offline12-demo'
destination_bucket  = 'ainexusit-online911'


def copy_to_destination_bucket(fname):
    client.copy_object(Bucket='{}'.format(destination_bucket),CopySource='/{}/{}'.format(source_bucket,fname),Key='{}'.format(fname))


def delete_from_source_bucket(fname):
    response = client.delete_object(Bucket='{}'.format(source_bucket),Key='{}'.format(fname))


def main():
    response = client.list_objects(Bucket='{}'.format(source_bucket))

    for key in response['Contents']:
        filename = key['Key']
        copy_to_destination_bucket(filename)
        delete_from_source_bucket(filename)


if __name__=='__main__':
    main()