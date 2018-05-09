import boto3
def create_bucket():
    s3 = boto3.client('s3')
    response = s3.create_bucket(Bucket= raw_input())
    print response.get('Location')
    pass

def list_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    n = len(response.get('Buckets'))
    while n > 0:
        n = n-1
        print response.get('Buckets')[n].get('Name')

def uploadobjets():
    s3 = boto3.client('s3')
    sourcefile = 'E:\workspace\ec2 sample1.json'
    bucketname = 'chaitnayaconstuctions'
    objectname = "test1/test2/test_python.txt"
    response = s3.upload_file(sourcefile,bucketname,objectname)
    print response





if __name__ == '__main__':
    #create_bucket()
    #list_buckets()
    uploadobjets()