import EC2
if __name__ == '__main__':
    ec2_boto = EC2.Ec2()
    instance = ec2_boto.list_ec2()
