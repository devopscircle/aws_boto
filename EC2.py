import boto3
class Ec2():
    def __init__(self, ec2=boto3.resource('ec2'), sg=boto3.client('ec2')):

        self.ec2 = ec2
        self.sg = sg

    # code for the Listing the ec2_instances
    def list_ec2(self):
        instances = self.ec2.instances.all()
        for instance in instances:
            print  "Instance_Id : %s" % instance.id + "," \
                  + "Instance_type : %s" % instance.instance_type + "," + "Availability_Zone : %s" % instance.placement.get(
                'AvailabilityZone') + "," + "Instance_State : %s" % instance.state.get('Name') + "," \
                  + "Public_dns : %s" % instance.public_dns_name + "," + "Public_Ipv4Ip : %s" % instance.public_ip_address + "," \
                  + "Key_Name : %s" % instance.key_name + "," + "Monitoring : %s" % instance.monitoring.get('State') + \
                  "," + "Launch_time : %s" % instance.launch_time + "," + "Security_Group : %s" % \
                                                                          instance.security_groups[0].get('GroupId') + \
                  "," + "VPC_ID : %s" % instance.vpc_id + "," + "Subnet_ID : %s" % instance.subnet_id + "," \
                  + "IAM_Instance_Profile : %s" % instance.iam_instance_profile + "," + "Image_ID : %s" % instance.image_id + "," \
                  + "Paltform : %s" % instance.platform + "," + "Private_DNS_Name :%s" % instance.private_dns_name + "," \
                  + "Private_IP_Address :%s" % instance.private_ip_address + "," + "Virtualization_Type :%s" % instance.virtualization_type \
                  + "," + "Architecture :%s" % instance.architecture + "," + "Root_Device_Name :%s" % instance.root_device_name
           # Getting the list of instance using vpc
            vpc = self.ec2.Vpc(instance.vpc_id)
            ins = vpc.instances.all()
            for i in ins:
                print i

    # code for creating the instance using attributes
    def create_Instances(self):
        instances = self.ec2.create_instances(
            ImageId='ami-4fffc834',
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            KeyName='class',
            SubnetId='subnet-56eaf01e',
            SecurityGroupIds=('sg-915d58e1', 'sg-264c4956'),
            Placement={'AvailabilityZone': 'us-east-1a', 'AvailabilityZone': 'us-east-1b',
                       'AvailabilityZone': 'us-east-1c'},

        )
        print instances[0].id

    # code for the starting the instnaces using instance id
    def start_instances(self):
        print "Give Instance_Id to Start:"
        response = self.sg.start_instances(
            InstanceIds=[raw_input()]  # input as instanceid
        )
        print "Instance_Id : %s" % response.get('StartingInstances')[0].get('InstanceId') + "," + "Current_State : %s" \
                                                                                                  % response.get(
            'StartingInstances')[0].get('CurrentState').get('Name') + "," + "Previous_state : %s" \
                                                                            % response.get('StartingInstances')[0].get(
            'PreviousState').get('Name')

    # code for the stopping the instnaces using instance id
    def stop_instances(self):
        print "Give Instance_Id to Stop:"
        response = self.sg.stop_instances(
            InstanceIds=[raw_input()]  # input as instanceid
        )
        print "Instance_Id : %s" % response.get('StoppingInstances')[0].get('InstanceId') + "," + "Current_State : %s" \
                                                                                                  % response.get(
            'StoppingInstances')[0].get('CurrentState').get('Name') + "," + "Previous_state : %s" \
                                                                            % response.get('StoppingInstances')[0].get(
            'PreviousState').get('Name')

    # code for the terminating the instances using Instance id
    def terminate_instance(self):
        print "Give Instance_Id to Terminate:"
        response = self.sg.terminate_instances(
            InstanceIds=[raw_input()]  # input as instanceid
        )
        print "Instance_Id : %s" % response.get('TerminatingInstances')[0].get(
            'InstanceId') + "," + "Current_State : %s" \
                                  % response.get('TerminatingInstances')[0].get('CurrentState').get(
            'Name') + "," + "Previous_state : %s" \
                            % response.get('TerminatingInstances')[0].get('PreviousState').get('Name')

    # code for the security groups
    def list_securitygroup(self):
        print "Give Vpc-Id to list Security Groups:"
        response = self.sg.describe_security_groups(
            Filters=[
                {
                    'Name': 'vpc-id',
                    'Values': [
                        raw_input()  # input as vpc-id
                    ]
                }
            ]
        )
        # printing the index using while loop to get the
        print response
        n = len(response.get('SecurityGroups'))  #
        while n > 0:
            n = n - 1
            print response.get('SecurityGroups')[n - 1].get('GroupId')

    def create_securitygroup(self):
        print "Give Groupname and VpcId one after other :"
        response = self.sg.create_security_group(
            Description='this security group is for the development',
            GroupName= raw_input(), #enter the group anme
            VpcId= raw_input()
        )
        print response.get('GroupId')

    def Addrule_securitygroup(self):
        pass

    def deleterule_securitygroup(self):
        pass

    def delete_securitygroup(self):
        print "Give the groupId to delete the instance:"
        response = self.sg.delete_security_group(
            GroupId=raw_input()
        )
        print response

    # code for the keypairs
    def list_keypairs(self):
        response = self.sg.describe_key_pairs()
        n = len(response.get('KeyPairs'))  #
        while n > 0:
            n = n - 1
            print response.get('KeyPairs')[n - 1].get('KeyName')

    def create_keypair(self):
        keyname = raw_input()
        response = self.sg.create_key_pair(
            KeyName = keyname
        )

        f = open(keyname + ".pem" , 'w')
        f.write(response.get('KeyMaterial'))
        f.close()
        print f , response.get('KeyMaterial')

    def del_keypairs(self):
        response = self.sg.delete_key_pair(
            KeyName = raw_input()
        )
        #print  response.get('ResponseMetadata').get('HTTPStatusCode')
        if response.get('ResponseMetadata').get('HTTPStatusCode')!=200:
          print "The Keypair was not deleted. Check wether key exists "
        else:
            print"The Keypair was deleted sucessfully "

#Listing the regions In aws
    def list_regions(self):
        response = self.sg.describe_regions()
        print response
        n = len(response.get('Regions'))
        while n > 0:
            n = n -1
            print response.get('Regions')[n].get('RegionName')

# describing the list of AZ in particular resion

    def list_Azs(self):
        response = self.sg.describe_availability_zones(
            Filters=[
                {
                    'Name': 'region-name',
                    'Values': [
                        'us-east-1',
                    ]
                },
            ]
            )
        n = len(response.get('AvailabilityZones'))
        while n > 0:
            n = n -1
            print response.get('AvailabilityZones')[n].get('ZoneName') +"______" +  response.get('AvailabilityZones')[n].get('State')






