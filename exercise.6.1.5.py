import boto.ec2
import os
from boto.ec2.elb import ELBConnection
from boto.ec2.elb import HealthCheck

from boto.ec2.autoscale import AutoScaleConnection
from boto.ec2.autoscale import LaunchConfiguration
from boto.ec2.autoscale import AutoScalingGroup
from boto.ec2.autoscale import ScalingPolicy

region = 'eu-west-1'
AWS_ACCESS_KEY = 'ASIARHS7F46CBBQQZMOW'
AWS_SECRET_KEY = 'qkvyeKfYmKlj3TiHYUkO+7P/zvF5nKD5vW/SiiN+'

conn_elb = ELBConnection(AWS_ACCESS_KEY, AWS_SECRET_KEY)
conn_as = AutoScaleConnection(AWS_ACCESS_KEY, AWS_SECRET_KEY)

elastic_load_balancer = {
    'name': 'load-balancer',
    'health_check_target': 'HTTP:80/index.html',#Loaction to perform health checks
    'connection_forwarding': [(80, 80, 'http'), (443, 443, 'tcp')]
}

autoscaling_group = {
    'name': 'web-server-auto-scaling-group',
    'min_size': 2,  # Since we want 2 Minimum instances running at all times
    'max_size': 4, #Maximum number of instances that should be running at all times

}

as_ami = {
    'id': 'ami-8e1fece7', #The AMI ID of the instance your Auto Scaling group will launch
    'access_key': 'anant-key', #The key the EC2 instance will be configured with
    'security_groups': ['web-sg'], 
    'instance_type': 't1.nano', 
    'instance_monitoring': True 
}

lc_name = 'web-server-auto-scaling-configuration'


conn_reg = boto.ec2.connect_to_region(region_name=region)
zones = conn_reg.get_all_zones()

zoneStrings = []
for zone in zones:
    zoneStrings.append(zone.name)
    
lb = conn_elb.create_load_balancer(LoadBalancerName=elastic_load_balancer['name'],
                                    AvailabilityZones=zoneStrings,
                                       Listeners=elastic_load_balancer['connection_forwarding'],
                                       SecurityGroups=['load-balancer-sg']
                                       Tags=[{'Project':'ccbda bootstrap','Cost-center':'laboratory'}])
conn_as.create_launch_configuration(lc)

ag = AutoScalingGroup(group_name=autoscaling_group['name'], load_balancers=[elastic_load_balancer['name']],
                          availability_zones=zoneStrings,
                          launch_config=lc, min_size=autoscaling_group['min_size'], max_size=autoscaling_group['max_size'])
conn_as.create_auto_scaling_group(ag)

