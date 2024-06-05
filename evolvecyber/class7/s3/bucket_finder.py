# import boto3 library
import boto3 

# initialize boto3 s3 client
s3 = boto3.client("s3") 

# Define variable for a region 
REGION = "us-west-2" 

# Create empty list 
BUCKET_LIST = [] 

TAGS = {
    'TagSet': [
        {
            'Key': 'envi',
            'Value': 'dev'
        },
        {
            'Key': 'managedBy',
            'Value': 'terraform'
        },
    ]
}

# print(type(s3))
# print(type(boto3)) 
# print(dir(boto3)) 
# print(dir(boto3.s3))

# List S3 buckets and save as "response"
response = s3.list_buckets()

# iterate thru response list and print bucketname
for bucket in response["Buckets"]:
    print(bucket["Name"]) 
    BUCKET_LIST.append(bucket["Name"])

# Print bucketnames
print(BUCKET_LIST)

for bucket in BUCKET_LIST:
    # find bucket location
    bucket_location = s3.get_bucket_location(Bucket=bucket) 
    bucket_region = bucket_location["LocationConstraint"]

    # if bucket is in region
    if bucket_region == REGION:
        # print to the screen
        print("The bucket %s is locatied in %s" % (bucket_region)) 
        # add tags
        response = s3.put_bucket_tagging(Bucket=bucket,Tagging=TAGS)
        print("The following buckets %s are tagger" % bucket)

    
    
    # response = client.put_bucket_tagging(
    #     Bucket=bucket,
    #     Tagging={
    #         'TagSet': [
    #             {
    #                 'Key': 'managedBy',
    #                 'Value': 'DevOps'
    #             },
    #         ]
    #     },
    # )

    # for bucket in BUCKET_LIST:
    #     response = s3.put_bucket_tagging(Bucket=bucket,Tagging=TAGS)