import boto3
import sys

# function for describing the ec2 instances with id and state of the instance
def ec2_describe():
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.all()
    for instance in instances:
        print instance.id , instance.state

# function for creating the ec2 instance using the imageid , instance type, keyName,MinCount,MaxCount,SubnetId,SecurityGroups
def create_instance():
    ec2 = boto3.resource('ec2')
    instances = ec2.create_instances(
        ImageId='ami-4fffc834',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='class'

    )
    print instances[0].id
# function for terminting the instances by passing the instanceid as argument
def terminate_instance():

    ec2 = boto3.resource('ec2')
    for instance_id in sys.argv[1:]:
        instance = ec2.Instance(instance_id)
        response = instance.terminate()
        print response

#main function to run the required functions
if __name__ == '__main__':
    create_instance()
    ec2_describe()
    #terminate_instance()