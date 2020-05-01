ACTIONS = {
  "ec2:AcceptReservedInstancesExchangeQuote": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Accepts the Convertible Reserved Instance exchange quote described in the GetReservedInstancesExchangeQuote call.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptReservedInstancesExchangeQuote.html"
  },
  "ec2:AcceptTransitGatewayVpcAttachment": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGatewayAttachment"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Accepts a request to attach a VPC to a transit gateway",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptTransitGatewayVpcAttachment.html"
  },
  "ec2:AcceptVpcEndpointConnections": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Accepts one or more interface VPC endpoint connection requests to your VPC endpoint service.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptVpcEndpointConnections.html"
  },
  "ec2:AcceptVpcPeeringConnection": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::VpcPeeringConnection",
      "AWS::Ec2::Vpc"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:Tenancy",
      "ec2:AccepterVpc",
      "ec2:RequesterVpc",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Accept a VPC peering connection request.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptVpcPeeringConnection.html"
  },
  "ec2:AdvertiseByoipCidr": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Advertises an IPv4 address range that is provisioned for use with your AWS resources through bring your own IP addresses (BYOIP)",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AdvertiseByoipCidr.html"
  },
  "ec2:AllocateAddress": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Acquires an Elastic IP address.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AllocateAddress.html"
  },
  "ec2:AllocateHosts": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Allocates a Dedicated Host to your account.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AllocateHosts.html"
  },
  "ec2:ApplySecurityGroupsToClientVpnTargetNetwork": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::VpcPeeringConnection",
      "AWS::Ec2::ClientVpnEndpoint",
      "AWS::Ec2::Vpc",
      "AWS::Ec2::SecurityGroup"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Applies a security group to the association between the target network and the Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ApplySecurityGroupsToClientVpnTargetNetwork.html"
  },
  "ec2:AssignIpv6Addresses": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Assigns one or more IPv6 addresses to the specified network interface.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssignIpv6Addresses.html"
  },
  "ec2:AssignPrivateIpAddresses": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Assigns one or more secondary private IP addresses to the specified network interface.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssignPrivateIpAddresses.html"
  },
  "ec2:AssociateAddress": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Associates an Elastic IP address with an instance or a network interface.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateAddress.html"
  },
  "ec2:AssociateClientVpnTargetNetwork": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::ClientVpnEndpoint",
      "AWS::Ec2::Subnet"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Associates a target network with a Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateClientVpnTargetNetwork.html"
  },
  "ec2:AssociateDhcpOptions": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Associates a set of DHCP options (that you've previously created) with the specified VPC, or associates no DHCP options with the VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateDhcpOptions.html"
  },
  "ec2:AssociateIamInstanceProfile": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [
      "ec2:AvailabilityZone",
      "ec2:EbsOptimized",
      "ec2:InstanceProfile",
      "ec2:InstanceType",
      "ec2:PlacementGroup",
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:RootDeviceType",
      "ec2:Tenancy"
    ],
    "Dependent Actions": [
      "iam:PassRole"
    ],
    "Description": "Associates an IAM instance profile with a running or stopped instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateIamInstanceProfile.html"
  },
  "ec2:AssociateRouteTable": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Associates a subnet with a route table.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateRouteTable.html"
  },
  "ec2:AssociateSubnetCidrBlock": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Associates a CIDR block with your subnet.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateSubnetCidrBlock.html"
  },
  "ec2:AssociateTransitGatewayRouteTable": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGatewayRouteTable",
      "AWS::Ec2::TransitGatewayAttachment"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Associates the specified attachment with the specified transit gateway route table",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateTransitGatewayRouteTable.html"
  },
  "ec2:AssociateVpcCidrBlock": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Associates a CIDR block with your VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateVpcCidrBlock.html"
  },
  "ec2:AttachClassicLinkVpc": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::VpcPeeringConnection",
      "AWS::Ec2::Instance",
      "AWS::Ec2::Vpc",
      "AWS::Ec2::SecurityGroup"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:Vpc",
      "ec2:InstanceType",
      "ec2:Tenancy",
      "ec2:InstanceProfile",
      "ec2:AvailabilityZone",
      "ec2:ResourceTag/${TagKey}",
      "ec2:EbsOptimized",
      "ec2:PlacementGroup",
      "ec2:RootDeviceType"
    ],
    "Dependent Actions": [],
    "Description": "Links an EC2-Classic instance to a ClassicLink-enabled VPC through one or more of the VPC's security groups.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachClassicLinkVpc.html"
  },
  "ec2:AttachInternetGateway": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Attaches an Internet gateway to a VPC, enabling connectivity between the Internet and the VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachInternetGateway.html"
  },
  "ec2:AttachNetworkInterface": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Attaches a network interface to an instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachNetworkInterface.html"
  },
  "ec2:AttachVolume": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Volume",
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:Encrypted",
      "ec2:InstanceType",
      "ec2:ParentSnapshot",
      "ec2:Tenancy",
      "ec2:InstanceProfile",
      "ec2:VolumeSize",
      "ec2:AvailabilityZone",
      "ec2:ResourceTag/${TagKey}",
      "ec2:VolumeIops",
      "ec2:EbsOptimized",
      "ec2:PlacementGroup",
      "ec2:VolumeType",
      "ec2:RootDeviceType"
    ],
    "Dependent Actions": [],
    "Description": "Attaches an EBS volume to a running or stopped instance and exposes it to the instance with the specified device name.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachVolume.html"
  },
  "ec2:AttachVpnGateway": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Attaches a virtual private gateway to a VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachVpnGateway.html"
  },
  "ec2:AuthorizeClientVpnIngress": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::ClientVpnEndpoint"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Adds an ingress authorization rule to a Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeClientVpnIngress.html"
  },
  "ec2:AuthorizeSecurityGroupEgress": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::SecurityGroup"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Vpc"
    ],
    "Dependent Actions": [],
    "Description": "[EC2-VPC only] Adds one or more egress rules to a security group for use with a VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupEgress.html"
  },
  "ec2:AuthorizeSecurityGroupIngress": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::SecurityGroup"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Vpc"
    ],
    "Dependent Actions": [],
    "Description": "Adds one or more ingress rules to a security group.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html"
  },
  "ec2:BundleInstance": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Bundles an Amazon instance store-backed Windows instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BundleInstance.html"
  },
  "ec2:CancelBundleTask": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Cancels a bundling operation for an instance store-backed Windows instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelBundleTask.html"
  },
  "ec2:CancelCapacityReservation": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::CapacityReservation"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Cancels the specified Capacity Reservation, releases the reserved capacity, and changes the Capacity Reservation's state to cancelled.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelCapacityReservation.html"
  },
  "ec2:CancelConversionTask": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Cancels an active conversion task.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelConversionTask.html"
  },
  "ec2:CancelExportTask": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Cancels an active export task.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelExportTask.html"
  },
  "ec2:CancelImportTask": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Cancels an in-process import virtual machine or import snapshot task.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelImportTask.html"
  },
  "ec2:CancelReservedInstancesListing": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Cancels the specified Reserved Instance listing in the Reserved Instance Marketplace.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelReservedInstancesListing.html"
  },
  "ec2:CancelSpotFleetRequests": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Cancels the specified Spot fleet requests.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelSpotFleetRequests.html"
  },
  "ec2:CancelSpotInstanceRequests": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Cancels one or more Spot instance requests.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelSpotInstanceRequests.html"
  },
  "ec2:ConfirmProductInstance": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Determines whether a product code is associated with an instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ConfirmProductInstance.html"
  },
  "ec2:CopyFpgaImage": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Initiates the copy of an Amazon FPGA Image (AFI) from the specified source region to the current region.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CopyFpgaImage.html"
  },
  "ec2:CopyImage": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Initiates the copy of an AMI from the specified source region to the current region.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CopyImage.html"
  },
  "ec2:CopySnapshot": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Snapshot"
    ],
    "Condition Keys": [
      "aws:TagKeys",
      "aws:RequestTag/${TagKey}",
      "ec2:Region"
    ],
    "Dependent Actions": [],
    "Description": "Copies a point-in-time snapshot of an EBS volume and stores it in Amazon S3.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CopySnapshot.html"
  },
  "ec2:CreateCapacityReservation": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a new Capacity Reservation with the specified attributes.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCapacityReservation.html"
  },
  "ec2:CreateClientVpnEndpoint": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::ClientVpnEndpoint"
    ],
    "Condition Keys": [
      "aws:RequestTag/${TagKey}",
      "aws:TagKeys",
      "ec2:Region"
    ],
    "Dependent Actions": [],
    "Description": "Creates a Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateClientVpnEndpoint.html"
  },
  "ec2:CreateClientVpnRoute": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::ClientVpnEndpoint",
      "AWS::Ec2::Subnet"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Adds a route to a network to a Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateClientVpnRoute.html"
  },
  "ec2:CreateCustomerGateway": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Provides information to AWS about your VPN customer gateway device.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCustomerGateway.html"
  },
  "ec2:CreateDefaultSubnet": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a default subnet with a size /20 IPv4 CIDR block in the specified Availability Zone in your default VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDefaultSubnet.html"
  },
  "ec2:CreateDefaultVpc": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a default VPC with a size /16 IPv4 CIDR block and a default subnet in each Availability Zone.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDefaultVpc.html"
  },
  "ec2:CreateDhcpOptions": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a set of DHCP options for your VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDhcpOptions.html"
  },
  "ec2:CreateEgressOnlyInternetGateway": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates an egress-only Internet gateway for your VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateEgressOnlyInternetGateway.html"
  },
  "ec2:CreateFleet": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Launches an EC2 Fleet.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet.html"
  },
  "ec2:CreateFlowLogs": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates one or more flow logs to capture IP traffic for a specific network interface, subnet, or VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFlowLogs.html"
  },
  "ec2:CreateFpgaImage": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates an Amazon FPGA Image (AFI) from the specified design checkpoint (DCP).",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFpgaImage.html"
  },
  "ec2:CreateImage": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is either running or stopped.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html"
  },
  "ec2:CreateInstanceExportTask": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Exports a running or stopped instance to an S3 bucket.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateInstanceExportTask.html"
  },
  "ec2:CreateInternetGateway": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates an Internet gateway for use with a VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateInternetGateway.html"
  },
  "ec2:CreateKeyPair": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a 2048-bit RSA key pair with the specified name.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateKeyPair.html"
  },
  "ec2:CreateLaunchTemplate": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a new launch template.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html"
  },
  "ec2:CreateLaunchTemplateVersion": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::LaunchTemplate"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Creates a new version for the specified launch template.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplateVersion.html"
  },
  "ec2:CreateNatGateway": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a NAT gateway in the specified subnet.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNatGateway.html"
  },
  "ec2:CreateNetworkAcl": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a network ACL in a VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkAcl.html"
  },
  "ec2:CreateNetworkAclEntry": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates an entry (a rule) in a network ACL with the specified rule number.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkAclEntry.html"
  },
  "ec2:CreateNetworkInterface": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a network interface in the specified subnet.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html"
  },
  "ec2:CreateNetworkInterfacePermission": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Ec2::NetworkInterface"
    ],
    "Condition Keys": [
      "ec2:AuthorizedUser",
      "ec2:AvailabilityZone",
      "ec2:Permission",
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Subnet",
      "ec2:Vpc",
      "ec2:AuthorizedService"
    ],
    "Dependent Actions": [],
    "Description": "Creates a permission for a network interface that grants certain operations to another authorized user.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterfacePermission.html"
  },
  "ec2:CreatePlacementGroup": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a placement group that you launch cluster instances into.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreatePlacementGroup.html"
  },
  "ec2:CreateReservedInstancesListing": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a listing for Amazon EC2 Standard Reserved Instances to be sold in the Reserved Instance Marketplace.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateReservedInstancesListing.html"
  },
  "ec2:CreateRoute": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::RouteTable"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Vpc"
    ],
    "Dependent Actions": [],
    "Description": "Creates a route in a route table within a VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateRoute.html"
  },
  "ec2:CreateRouteTable": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a route table for the specified VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateRouteTable.html"
  },
  "ec2:CreateSecurityGroup": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a security group.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSecurityGroup.html"
  },
  "ec2:CreateSnapshot": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Volume",
      "AWS::Ec2::Snapshot"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:Encrypted",
      "ec2:VolumeSize",
      "aws:TagKeys",
      "aws:RequestTag/${TagKey}",
      "ec2:ResourceTag/${TagKey}",
      "ec2:ParentVolume",
      "ec2:VolumeIops",
      "ec2:VolumeType"
    ],
    "Dependent Actions": [],
    "Description": "Creates a snapshot of an EBS volume and stores it in Amazon S3.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSnapshot.html"
  },
  "ec2:CreateSnapshots": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Volume",
      "AWS::Ec2::Snapshot",
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:Encrypted",
      "ec2:InstanceType",
      "ec2:Tenancy",
      "ec2:InstanceProfile",
      "ec2:VolumeSize",
      "aws:TagKeys",
      "ec2:AvailabilityZone",
      "aws:RequestTag/${TagKey}",
      "ec2:ResourceTag/${TagKey}",
      "ec2:VolumeIops",
      "ec2:EbsOptimized",
      "ec2:ParentVolume",
      "ec2:PlacementGroup",
      "ec2:VolumeType",
      "ec2:RootDeviceType"
    ],
    "Dependent Actions": [],
    "Description": "Creates a snapshots of an EBS volumes which attached to an EC2 instance and stores them in Amazon S3.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSnapshots.html"
  },
  "ec2:CreateSpotDatafeedSubscription": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a data feed for Spot instances, enabling you to view Spot instance usage logs. You can create one data feed per AWS account.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSpotDatafeedSubscription.html"
  },
  "ec2:CreateSubnet": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a subnet in an existing VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSubnet.html"
  },
  "ec2:CreateTags": {
    "Access": "Tagging",
    "Affects": [
      "AWS::Ec2::Subnet",
      "AWS::Ec2::VpnConnection",
      "AWS::Ec2::NetworkAcl",
      "AWS::Ec2::Snapshot",
      "AWS::Ec2::TrafficMirrorFilter",
      "AWS::Ec2::FpgaImage",
      "AWS::Ec2::TrafficMirrorTarget",
      "AWS::Ec2::TrafficMirrorSession",
      "AWS::Ec2::Instance",
      "AWS::Ec2::Volume",
      "AWS::Ec2::InternetGateway",
      "AWS::Ec2::VpnGateway",
      "AWS::Ec2::NetworkInterface",
      "AWS::Ec2::ReservedInstances",
      "AWS::Ec2::DhcpOptions",
      "AWS::Ec2::TransitGatewayRouteTable",
      "AWS::Ec2::Image",
      "AWS::Ec2::RouteTable",
      "AWS::Ec2::SpotInstanceRequest",
      "AWS::Ec2::ClientVpnEndpoint",
      "AWS::Ec2::TransitGatewayAttachment",
      "AWS::Ec2::SecurityGroup",
      "AWS::Ec2::CapacityReservation",
      "AWS::Ec2::TransitGateway",
      "AWS::Ec2::Vpc"
    ],
    "Condition Keys": [
      "ec2:Vpc",
      "ec2:Public",
      "ec2:CreateAction",
      "ec2:InstanceType",
      "ec2:Tenancy",
      "ec2:ReservedInstancesOfferingType",
      "ec2:AvailabilityZone",
      "ec2:ImageType",
      "ec2:PlacementGroup",
      "ec2:VolumeType",
      "ec2:Region",
      "ec2:ParentSnapshot",
      "ec2:VolumeSize",
      "ec2:Subnet",
      "aws:TagKeys",
      "ec2:EbsOptimized",
      "ec2:RootDeviceType",
      "ec2:Encrypted",
      "ec2:SnapshotTime",
      "ec2:InstanceProfile",
      "ec2:Owner",
      "aws:RequestTag/${TagKey}",
      "ec2:ResourceTag/${TagKey}",
      "ec2:ParentVolume",
      "ec2:VolumeIops"
    ],
    "Dependent Actions": [],
    "Description": "Adds or overwrites one or more tags for the specified Amazon EC2 resource or resources.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html"
  },
  "ec2:CreateTrafficMirrorFilter": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TrafficMirrorFilterRule",
      "AWS::Ec2::TrafficMirrorFilter"
    ],
    "Condition Keys": [
      "aws:RequestTag/${TagKey}",
      "aws:TagKeys",
      "ec2:Region"
    ],
    "Dependent Actions": [],
    "Description": "Creates a Traffic Mirror filter.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTrafficMirrorFilter.html"
  },
  "ec2:CreateTrafficMirrorFilterRule": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TrafficMirrorFilterRule",
      "AWS::Ec2::TrafficMirrorFilter"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Creates a Traffic Mirror filter rule.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTrafficMirrorFilterRule.html"
  },
  "ec2:CreateTrafficMirrorSession": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TrafficMirrorFilter",
      "AWS::Ec2::NetworkInterface",
      "AWS::Ec2::TrafficMirrorSession",
      "AWS::Ec2::TrafficMirrorTarget",
      "AWS::Ec2::TrafficMirrorFilterRule"
    ],
    "Condition Keys": [
      "ec2:Region",
      "aws:RequestTag/${TagKey}",
      "ec2:ResourceTag/${TagKey}",
      "aws:TagKeys"
    ],
    "Dependent Actions": [],
    "Description": "Creates a Traffic Mirror session.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTrafficMirrorSession.html"
  },
  "ec2:CreateTrafficMirrorTarget": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::NetworkInterface",
      "AWS::Ec2::TrafficMirrorTarget"
    ],
    "Condition Keys": [
      "ec2:Region",
      "aws:RequestTag/${TagKey}",
      "ec2:ResourceTag/${TagKey}",
      "aws:TagKeys"
    ],
    "Dependent Actions": [],
    "Description": "Creates a Traffic Mirror target.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTrafficMirrorTarget.html"
  },
  "ec2:CreateTransitGateway": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGateway",
      "AWS::Ec2::TransitGatewayRouteTable",
      "AWS::Ec2::TransitGatewayAttachment"
    ],
    "Condition Keys": [
      "aws:RequestTag/${TagKey}",
      "aws:TagKeys",
      "ec2:Region"
    ],
    "Dependent Actions": [],
    "Description": "Creates a transit gateway.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGateway.html"
  },
  "ec2:CreateTransitGatewayRoute": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGatewayAttachment",
      "AWS::Ec2::TransitGatewayRouteTable"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Creates a static route for the specified transit gateway route table.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayRoute.html"
  },
  "ec2:CreateTransitGatewayRouteTable": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGateway",
      "AWS::Ec2::TransitGatewayAttachment",
      "AWS::Ec2::TransitGatewayRouteTable"
    ],
    "Condition Keys": [
      "ec2:Region",
      "aws:RequestTag/${TagKey}",
      "ec2:ResourceTag/${TagKey}",
      "aws:TagKeys"
    ],
    "Dependent Actions": [],
    "Description": "Creates a route table for the specified transit gateway.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayRouteTable.html"
  },
  "ec2:CreateTransitGatewayVpcAttachment": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGatewayAttachment",
      "AWS::Ec2::Subnet",
      "AWS::Ec2::TransitGateway",
      "AWS::Ec2::Vpc",
      "AWS::Ec2::VpcPeeringConnection",
      "AWS::Ec2::TransitGatewayRouteTable"
    ],
    "Condition Keys": [
      "ec2:Region",
      "aws:RequestTag/${TagKey}",
      "ec2:ResourceTag/${TagKey}",
      "aws:TagKeys"
    ],
    "Dependent Actions": [],
    "Description": "Attaches the specified VPC to the specified transit gateway.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayVpcAttachment.html"
  },
  "ec2:CreateVolume": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Volume"
    ],
    "Condition Keys": [
      "aws:RequestTag/${TagKey}",
      "aws:TagKeys",
      "ec2:AvailabilityZone",
      "ec2:Encrypted",
      "ec2:ParentSnapshot",
      "ec2:Region",
      "ec2:VolumeIops",
      "ec2:VolumeSize",
      "ec2:VolumeType"
    ],
    "Dependent Actions": [],
    "Description": "Creates an EBS volume that can be attached to an instance in the same Availability Zone.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html"
  },
  "ec2:CreateVpc": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a VPC with the specified CIDR block.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpc.html"
  },
  "ec2:CreateVpcEndpoint": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [
      "route53:AssociateVPCWithHostedZone"
    ],
    "Description": "Creates a VPC endpoint for a specified AWS service.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpoint.html"
  },
  "ec2:CreateVpcEndpointConnectionNotification": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a connection notification for a specified VPC endpoint or VPC endpoint service.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointConnectionNotification.html"
  },
  "ec2:CreateVpcEndpointServiceConfiguration": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a VPC endpoint service configuration to which service consumers (AWS accounts, IAM users, and IAM roles) can connect.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointServiceConfiguration.html"
  },
  "ec2:CreateVpcPeeringConnection": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::VpcPeeringConnection",
      "AWS::Ec2::Vpc"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:Tenancy",
      "ec2:AccepterVpc",
      "ec2:RequesterVpc",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Requests a VPC peering connection between two VPCs: a requester VPC that you own and a peer VPC with which to create the connection.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcPeeringConnection.html"
  },
  "ec2:CreateVpnConnection": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::VpnConnection"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:AuthenticationType",
      "ec2:DPDTimeoutSeconds",
      "ec2:GatewayType",
      "ec2:IKEVersions",
      "ec2:InsideTunnelCidr",
      "ec2:Phase1DHGroupNumbers",
      "ec2:Phase2DHGroupNumbers",
      "ec2:Phase1EncryptionAlgorithms",
      "ec2:Phase2EncryptionAlgorithms",
      "ec2:Phase1IntegrityAlgorithms",
      "ec2:Phase2IntegrityAlgorithms",
      "ec2:Phase1LifetimeSeconds",
      "ec2:Phase2LifetimeSeconds",
      "ec2:PresharedKeys",
      "ec2:RekeyFuzzPercentage",
      "ec2:RekeyMarginTimeSeconds",
      "ec2:RoutingType"
    ],
    "Dependent Actions": [],
    "Description": "Creates a VPN connection between an existing virtual private gateway and a VPN customer gateway.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpnConnection.html"
  },
  "ec2:CreateVpnConnectionRoute": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpnConnectionRoute.html"
  },
  "ec2:CreateVpnGateway": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a virtual private gateway.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpnGateway.html"
  },
  "ec2:DeleteClientVpnEndpoint": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::ClientVpnEndpoint"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteClientVpnEndpoint.html"
  },
  "ec2:DeleteClientVpnRoute": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::ClientVpnEndpoint",
      "AWS::Ec2::Subnet"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes a route from a Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteClientVpnRoute.html"
  },
  "ec2:DeleteCustomerGateway": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::CustomerGateway"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified customer gateway.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteCustomerGateway.html"
  },
  "ec2:DeleteDhcpOptions": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::DhcpOptions"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified set of DHCP options.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteDhcpOptions.html"
  },
  "ec2:DeleteEgressOnlyInternetGateway": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes the specified egress-only Internet gateway.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteEgressOnlyInternetGateway.html"
  },
  "ec2:DeleteFleets": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes the specified EC2 Fleet.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteFleets.html"
  },
  "ec2:DeleteFlowLogs": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes one or more flow logs.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteFlowLogs.html"
  },
  "ec2:DeleteFpgaImage": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes the specified Amazon FPGA Image (AFI).",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteFpgaImage.html"
  },
  "ec2:DeleteInternetGateway": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::InternetGateway"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified Internet gateway.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteInternetGateway.html"
  },
  "ec2:DeleteKeyPair": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes the specified key pair, by removing the public key from Amazon EC2.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteKeyPair.html"
  },
  "ec2:DeleteLaunchTemplate": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::LaunchTemplate"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified launch template and all associated versions.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteLaunchTemplate.html"
  },
  "ec2:DeleteLaunchTemplateVersions": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::LaunchTemplate"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified versions for the specified launch template.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteLaunchTemplateVersions.html"
  },
  "ec2:DeleteNatGateway": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes the specified NAT gateway.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNatGateway.html"
  },
  "ec2:DeleteNetworkAcl": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::NetworkAcl"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Vpc"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified network ACL.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkAcl.html"
  },
  "ec2:DeleteNetworkAclEntry": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::NetworkAcl"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Vpc"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified ingress or egress entry (rule) from the specified network ACL.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkAclEntry.html"
  },
  "ec2:DeleteNetworkInterface": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes the specified network interface. You must detach the network interface before you can delete it.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterface.html"
  },
  "ec2:DeleteNetworkInterfacePermission": {
    "Access": "Permissions Management",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes a permission associated with a network interface.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterfacePermission.html"
  },
  "ec2:DeletePlacementGroup": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes the specified placement group.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeletePlacementGroup.html"
  },
  "ec2:DeleteRoute": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::RouteTable"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Vpc"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified route from the specified route table.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteRoute.html"
  },
  "ec2:DeleteRouteTable": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::RouteTable"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Vpc"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified route table.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteRouteTable.html"
  },
  "ec2:DeleteSecurityGroup": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::SecurityGroup"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Vpc"
    ],
    "Dependent Actions": [],
    "Description": "Deletes a security group.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSecurityGroup.html"
  },
  "ec2:DeleteSnapshot": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Snapshot"
    ],
    "Condition Keys": [
      "ec2:Owner",
      "ec2:ParentVolume",
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:SnapshotTime",
      "ec2:VolumeSize"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified snapshot.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSnapshot.html"
  },
  "ec2:DeleteSpotDatafeedSubscription": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes the data feed for Spot instances.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSpotDatafeedSubscription.html"
  },
  "ec2:DeleteSubnet": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes the specified subnet.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSubnet.html"
  },
  "ec2:DeleteTags": {
    "Access": "Tagging",
    "Affects": [
      "AWS::Ec2::Subnet",
      "AWS::Ec2::VpnConnection",
      "AWS::Ec2::NetworkAcl",
      "AWS::Ec2::Snapshot",
      "AWS::Ec2::FpgaImage",
      "AWS::Ec2::Instance",
      "AWS::Ec2::Volume",
      "AWS::Ec2::InternetGateway",
      "AWS::Ec2::VpnGateway",
      "AWS::Ec2::NetworkInterface",
      "AWS::Ec2::ReservedInstances",
      "AWS::Ec2::DhcpOptions",
      "AWS::Ec2::TransitGatewayRouteTable",
      "AWS::Ec2::Image",
      "AWS::Ec2::RouteTable",
      "AWS::Ec2::SpotInstanceRequest",
      "AWS::Ec2::ClientVpnEndpoint",
      "AWS::Ec2::TransitGatewayAttachment",
      "AWS::Ec2::SecurityGroup",
      "AWS::Ec2::CapacityReservation",
      "AWS::Ec2::TransitGateway",
      "AWS::Ec2::Vpc"
    ],
    "Condition Keys": [
      "ec2:Region",
      "aws:RequestTag/${TagKey}",
      "ec2:ResourceTag/${TagKey}",
      "aws:TagKeys"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified set of tags from the specified set of resources.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTags.html"
  },
  "ec2:DeleteTrafficMirrorFilter": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TrafficMirrorFilterRule",
      "AWS::Ec2::TrafficMirrorFilter"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified Traffic Mirror filter.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTrafficMirrorFilter.html"
  },
  "ec2:DeleteTrafficMirrorFilterRule": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TrafficMirrorFilterRule",
      "AWS::Ec2::TrafficMirrorFilter"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified Traffic Mirror rule.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTrafficMirrorFilterRule.html"
  },
  "ec2:DeleteTrafficMirrorSession": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TrafficMirrorSession"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified Traffic Mirror session.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTrafficMirrorSession.html"
  },
  "ec2:DeleteTrafficMirrorTarget": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TrafficMirrorTarget"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified Traffic Mirror target.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTrafficMirrorTarget.html"
  },
  "ec2:DeleteTransitGateway": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGateway",
      "AWS::Ec2::TransitGatewayRouteTable",
      "AWS::Ec2::TransitGatewayAttachment"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified transit gateway.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGateway.html"
  },
  "ec2:DeleteTransitGatewayRoute": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGatewayRouteTable"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified route from the specified transit gateway route table.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayRoute.html"
  },
  "ec2:DeleteTransitGatewayRouteTable": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGatewayRouteTable"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified transit gateway route table.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayRouteTable.html"
  },
  "ec2:DeleteTransitGatewayVpcAttachment": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGatewayAttachment"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified VPC attachment.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayVpcAttachment.html"
  },
  "ec2:DeleteVolume": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Volume"
    ],
    "Condition Keys": [
      "ec2:AvailabilityZone",
      "ec2:Encrypted",
      "ec2:ParentSnapshot",
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:VolumeIops",
      "ec2:VolumeSize",
      "ec2:VolumeType"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the specified EBS volume.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVolume.html"
  },
  "ec2:DeleteVpc": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes the specified VPC. You must detach or delete all gateways and resources that are associated with the VPC before you can delete it.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpc.html"
  },
  "ec2:DeleteVpcEndpointConnectionNotifications": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes one or more VPC endpoint connection notifications.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcEndpointConnectionNotifications.html"
  },
  "ec2:DeleteVpcEndpointServiceConfigurations": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes one or more VPC endpoint service configurations in your account.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcEndpointServiceConfigurations.html"
  },
  "ec2:DeleteVpcEndpoints": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes one or more specified VPC endpoints.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcEndpoints.html"
  },
  "ec2:DeleteVpcPeeringConnection": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::VpcPeeringConnection"
    ],
    "Condition Keys": [
      "ec2:AccepterVpc",
      "ec2:Region",
      "ec2:RequesterVpc",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Deletes a VPC peering connection.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcPeeringConnection.html"
  },
  "ec2:DeleteVpnConnection": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes a VPC peering connection.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpnConnection.html"
  },
  "ec2:DeleteVpnConnectionRoute": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes the specified static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpnConnectionRoute.html"
  },
  "ec2:DeleteVpnGateway": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes the specified virtual private gateway.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpnGateway.html"
  },
  "ec2:DeprovisionByoipCidr": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Releases the specified address range that you provisioned for use with your AWS resources through bring your own IP addresses (BYOIP) and deletes the corresponding address pool.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeprovisionByoipCidr.html"
  },
  "ec2:DeregisterImage": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deregisters the specified AMI.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeregisterImage.html"
  },
  "ec2:DescribeAccountAttributes": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes attributes of your AWS account.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAccountAttributes.html"
  },
  "ec2:DescribeAddresses": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your Elastic IP addresses.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html"
  },
  "ec2:DescribeAggregateIdFormat": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the longer ID format settings for all resource types in a specific region.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAggregateIdFormat.html"
  },
  "ec2:DescribeAvailabilityZones": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of the Availability Zones that are available to you.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html"
  },
  "ec2:DescribeBundleTasks": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your bundling tasks.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeBundleTasks.html"
  },
  "ec2:DescribeByoipCidrs": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the IP address ranges that were specified in calls to ProvisionByoipCidr.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeByoipCidrs.html"
  },
  "ec2:DescribeCapacityReservations": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your Capacity Reservations.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCapacityReservations.html"
  },
  "ec2:DescribeClassicLinkInstances": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your linked EC2-Classic instances.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClassicLinkInstances.html"
  },
  "ec2:DescribeClientVpnAuthorizationRules": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the authorization rules for a specified Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnAuthorizationRules.html"
  },
  "ec2:DescribeClientVpnConnections": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes active client connections and connections that have been terminated within the last 60 minutes for the specified Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnConnections.html"
  },
  "ec2:DescribeClientVpnEndpoints": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more Client VPN endpoints in the account.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnEndpoints.html"
  },
  "ec2:DescribeClientVpnRoutes": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the routes for the specified Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnRoutes.html"
  },
  "ec2:DescribeClientVpnTargetNetworks": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the target networks associated with the specified Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnTargetNetworks.html"
  },
  "ec2:DescribeConversionTasks": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your conversion tasks.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeConversionTasks.html"
  },
  "ec2:DescribeCustomerGateways": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your VPN customer gateways.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCustomerGateways.html"
  },
  "ec2:DescribeDhcpOptions": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your DHCP options sets.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeDhcpOptions.html"
  },
  "ec2:DescribeEgressOnlyInternetGateways": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your egress-only Internet gateways.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeEgressOnlyInternetGateways.html"
  },
  "ec2:DescribeElasticGpus": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the Elastic GPUs associated with your instances.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeElasticGpus.html"
  },
  "ec2:DescribeExportImageTasks": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the specified export image tasks or all your export image tasks.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeExportImageTasks.html"
  },
  "ec2:DescribeExportTasks": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your export tasks.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeExportTasks.html"
  },
  "ec2:DescribeFastSnapshotRestores": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the state of fast snapshot restores for your snapshots",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFastSnapshotRestores.html"
  },
  "ec2:DescribeFleetHistory": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the events for the specified EC2 Fleet during the specified time.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFleetHistory.html"
  },
  "ec2:DescribeFleetInstances": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the running instances for the specified EC2 Fleet.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFleetInstances.html"
  },
  "ec2:DescribeFleets": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your EC2 Fleet.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFleets.html"
  },
  "ec2:DescribeFlowLogs": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more flow logs.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFlowLogs.html"
  },
  "ec2:DescribeFpgaImageAttribute": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the specified attribute of the specified Amazon FPGA Images (AFI).",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFpgaImageAttribute.html"
  },
  "ec2:DescribeFpgaImages": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of the Amazon FPGA Images (AFIs) available to you.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFpgaImages.html"
  },
  "ec2:DescribeHostReservationOfferings": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the Dedicated Host Reservations that are available to purchase.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeHostReservationOfferings.html"
  },
  "ec2:DescribeHostReservations": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes Dedicated Host Reservations which are associated with Dedicated Hosts in your account.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeHostReservations.html"
  },
  "ec2:DescribeHosts": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your Dedicated Hosts.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeHosts.html"
  },
  "ec2:DescribeIamInstanceProfileAssociations": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes your IAM instance profile associations.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIamInstanceProfileAssociations.html"
  },
  "ec2:DescribeIdFormat": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the ID format settings for your resources on a per-region basis, for example, to view which resource types are enabled for longer IDs.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIdFormat.html"
  },
  "ec2:DescribeIdentityIdFormat": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the ID format settings for resources for the specified IAM user, IAM role, or root user.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIdentityIdFormat.html"
  },
  "ec2:DescribeImageAttribute": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the specified attribute of the specified AMI.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImageAttribute.html"
  },
  "ec2:DescribeImages": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of the images (AMIs, AKIs, and ARIs) available to you.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html"
  },
  "ec2:DescribeImportImageTasks": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Displays details about an import virtual machine or import snapshot tasks that are already created.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImportImageTasks.html"
  },
  "ec2:DescribeImportSnapshotTasks": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes your import snapshot tasks.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImportSnapshotTasks.html"
  },
  "ec2:DescribeInstanceAttribute": {
    "Access": "Read",
    "Affects": [
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the specified attribute of the specified instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceAttribute.html"
  },
  "ec2:DescribeInstanceCreditSpecifications": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the credit option for CPU usage of one or more of your instances.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceCreditSpecifications.html"
  },
  "ec2:DescribeInstanceStatus": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the status of one or more instances.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceStatus.html"
  },
  "ec2:DescribeInstanceTypes": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes all instance types offered in an AWS Region.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceTypes.html"
  },
  "ec2:DescribeInstances": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your instances.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html"
  },
  "ec2:DescribeInternetGateways": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your Internet gateways.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInternetGateways.html"
  },
  "ec2:DescribeKeyPairs": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your key pairs.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeKeyPairs.html"
  },
  "ec2:DescribeLaunchTemplateVersions": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your launch template versions.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplateVersions.html"
  },
  "ec2:DescribeLaunchTemplates": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your launch templates.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html"
  },
  "ec2:DescribeMovingAddresses": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes your Elastic IP addresses that are being moved to the EC2-VPC platform, or that are being restored to the EC2-Classic platform.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeMovingAddresses.html"
  },
  "ec2:DescribeNatGateways": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of the your NAT gateways.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNatGateways.html"
  },
  "ec2:DescribeNetworkAcls": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your network ACLs.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkAcls.html"
  },
  "ec2:DescribeNetworkInterfaceAttribute": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes a network interface attribute. You can specify only one attribute at a time.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaceAttribute.html"
  },
  "ec2:DescribeNetworkInterfacePermissions": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the permissions associated with a network interface.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfacePermissions.html"
  },
  "ec2:DescribeNetworkInterfaces": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your network interfaces.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.html"
  },
  "ec2:DescribePlacementGroups": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your placement groups.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePlacementGroups.html"
  },
  "ec2:DescribePrefixLists": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes available AWS services in a prefix list format, which includes the prefix list name and prefix list ID of the service and the IP address range for the service.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePrefixLists.html"
  },
  "ec2:DescribePrincipalIdFormat": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the ID format settings for the root user and all IAM roles and IAM users that have explicitly specified a longer ID (17-character ID) preference.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePrincipalIdFormat.html"
  },
  "ec2:DescribePublicIpv4Pools": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the specified IPv4 address pools.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePublicIpv4Pools.html"
  },
  "ec2:DescribeRegions": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more regions that are currently available to you.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRegions.html"
  },
  "ec2:DescribeReservedInstances": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of the Reserved Instances that you purchased.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstances.html"
  },
  "ec2:DescribeReservedInstancesListings": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes your account's Reserved Instance listings in the Reserved Instance Marketplace.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstancesListings.html"
  },
  "ec2:DescribeReservedInstancesModifications": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the modifications made to your Reserved Instances.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstancesModifications.html"
  },
  "ec2:DescribeReservedInstancesOfferings": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes Reserved Instance offerings that are available for purchase.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstancesOfferings.html"
  },
  "ec2:DescribeRouteTables": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your route tables.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRouteTables.html"
  },
  "ec2:DescribeScheduledInstanceAvailability": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Finds available schedules that meet the specified criteria.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeScheduledInstanceAvailability.html"
  },
  "ec2:DescribeScheduledInstances": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your Scheduled Instances.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeScheduledInstances.html"
  },
  "ec2:DescribeSecurityGroupReferences": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "[EC2-VPC only] Describes the VPCs on the other side of a VPC peering connection that are referencing the security groups you've specified in this request.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroupReferences.html"
  },
  "ec2:DescribeSecurityGroups": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your security groups.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html"
  },
  "ec2:DescribeSnapshotAttribute": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the specified attribute of the specified snapshot.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshotAttribute.html"
  },
  "ec2:DescribeSnapshots": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of the EBS snapshots available to you.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html"
  },
  "ec2:DescribeSpotDatafeedSubscription": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the data feed for Spot instances.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotDatafeedSubscription.html"
  },
  "ec2:DescribeSpotFleetInstances": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the running instances for the specified Spot fleet.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotFleetInstances.html"
  },
  "ec2:DescribeSpotFleetRequestHistory": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the events for the specified Spot fleet request during the specified time.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotFleetRequestHistory.html"
  },
  "ec2:DescribeSpotFleetRequests": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes your Spot fleet requests.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotFleetRequests.html"
  },
  "ec2:DescribeSpotInstanceRequests": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the Spot instance requests that belong to your account.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotInstanceRequests.html"
  },
  "ec2:DescribeSpotPriceHistory": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the Spot price history.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotPriceHistory.html"
  },
  "ec2:DescribeStaleSecurityGroups": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "[EC2-VPC only] Describes the stale security group rules for security groups in a specified VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeStaleSecurityGroups.html"
  },
  "ec2:DescribeSubnets": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your subnets.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html"
  },
  "ec2:DescribeTags": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of the tags for your EC2 resources.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTags.html"
  },
  "ec2:DescribeTrafficMirrorFilters": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more Traffic Mirror filters.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTrafficMirrorFilters.html"
  },
  "ec2:DescribeTrafficMirrorSessions": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more Traffic Mirror sessions.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTrafficMirrorSessions.html"
  },
  "ec2:DescribeTrafficMirrorTargets": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more Traffic Mirror targets.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTrafficMirrorTargets.html"
  },
  "ec2:DescribeTransitGatewayAttachments": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more attachments between resources and transit gateways.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayAttachments.html"
  },
  "ec2:DescribeTransitGatewayRouteTables": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more transit gateway route tables.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayRouteTables.html"
  },
  "ec2:DescribeTransitGatewayVpcAttachments": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more VPC attachments.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayVpcAttachments.html"
  },
  "ec2:DescribeTransitGateways": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more transit gateways.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGateways.html"
  },
  "ec2:DescribeVolumeAttribute": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the specified attribute of the specified volume.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumeAttribute.html"
  },
  "ec2:DescribeVolumeStatus": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the status of the specified volumes.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumeStatus.html"
  },
  "ec2:DescribeVolumes": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the specified EBS volumes.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumes.html"
  },
  "ec2:DescribeVolumesModifications": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Reports the current modification status of EBS volumes.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumesModifications.html"
  },
  "ec2:DescribeVpcAttribute": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the specified attribute of the specified VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcAttribute.html"
  },
  "ec2:DescribeVpcClassicLink": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the ClassicLink status of one or more VPCs.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcClassicLink.html"
  },
  "ec2:DescribeVpcClassicLinkDnsSupport": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the ClassicLink DNS support status of one or more VPCs.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcClassicLinkDnsSupport.html"
  },
  "ec2:DescribeVpcEndpointConnectionNotifications": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the connection notifications for VPC endpoints and VPC endpoint services.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointConnectionNotifications.html"
  },
  "ec2:DescribeVpcEndpointConnections": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the VPC endpoint connections to your VPC endpoint services, including any endpoints that are pending your acceptance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointConnections.html"
  },
  "ec2:DescribeVpcEndpointServiceConfigurations": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the VPC endpoint service configurations in your account (your services).",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServiceConfigurations.html"
  },
  "ec2:DescribeVpcEndpointServicePermissions": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes the principals (service consumers) that are permitted to discover your VPC endpoint service.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServicePermissions.html"
  },
  "ec2:DescribeVpcEndpointServices": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes all supported AWS services that can be specified when creating a VPC endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServices.html"
  },
  "ec2:DescribeVpcEndpoints": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your VPC endpoints.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.html"
  },
  "ec2:DescribeVpcPeeringConnections": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your VPC peering connections.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcPeeringConnections.html"
  },
  "ec2:DescribeVpcs": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your VPCs.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcs.html"
  },
  "ec2:DescribeVpnConnections": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your VPN connections.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnConnections.html"
  },
  "ec2:DescribeVpnGateways": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes one or more of your virtual private gateways.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnGateways.html"
  },
  "ec2:DetachClassicLinkVpc": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::VpcPeeringConnection",
      "AWS::Ec2::Vpc",
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:InstanceType",
      "ec2:Tenancy",
      "ec2:InstanceProfile",
      "ec2:AvailabilityZone",
      "ec2:ResourceTag/${TagKey}",
      "ec2:EbsOptimized",
      "ec2:PlacementGroup",
      "ec2:RootDeviceType"
    ],
    "Dependent Actions": [],
    "Description": "Unlinks (detaches) a linked EC2-Classic instance from a VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachClassicLinkVpc.html"
  },
  "ec2:DetachInternetGateway": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Detaches an Internet gateway from a VPC, disabling connectivity between the Internet and the VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachInternetGateway.html"
  },
  "ec2:DetachNetworkInterface": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Detaches a network interface from an instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachNetworkInterface.html"
  },
  "ec2:DetachVolume": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Volume",
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:Encrypted",
      "ec2:InstanceType",
      "ec2:ParentSnapshot",
      "ec2:Tenancy",
      "ec2:InstanceProfile",
      "ec2:VolumeSize",
      "ec2:AvailabilityZone",
      "ec2:ResourceTag/${TagKey}",
      "ec2:VolumeIops",
      "ec2:EbsOptimized",
      "ec2:PlacementGroup",
      "ec2:VolumeType",
      "ec2:RootDeviceType"
    ],
    "Dependent Actions": [],
    "Description": "Detaches an EBS volume from an instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachVolume.html"
  },
  "ec2:DetachVpnGateway": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Detaches a virtual private gateway from a VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachVpnGateway.html"
  },
  "ec2:DisableEbsEncryptionByDefault": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Disable the default EBS encryption by enabled for your account in the current region",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableEbsEncryptionByDefault.html"
  },
  "ec2:DisableFastSnapshotRestores": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Snapshot"
    ],
    "Condition Keys": [
      "ec2:Owner",
      "ec2:ParentVolume",
      "ec2:Region",
      "ec2:AvailabilityZone",
      "ec2:SnapshotTime",
      "ec2:Encrypted",
      "ec2:VolumeSize",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Disables fast snapshot restores for the specified snapshots in the specified Availability Zones",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableFastSnapshotRestores.html"
  },
  "ec2:DisableTransitGatewayRouteTablePropagation": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGatewayRouteTable",
      "AWS::Ec2::TransitGatewayAttachment"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Disables the specified resource attachment from propagating routes to the specified propagation route table.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableTransitGatewayRouteTablePropagation.html"
  },
  "ec2:DisableVgwRoutePropagation": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Disables a virtual private gateway (VGW) from propagating routes to a specified route table of a VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableVgwRoutePropagation.html"
  },
  "ec2:DisableVpcClassicLink": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::VpcPeeringConnection",
      "AWS::Ec2::Vpc"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Tenancy"
    ],
    "Dependent Actions": [],
    "Description": "Disables ClassicLink for a VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableVpcClassicLink.html"
  },
  "ec2:DisableVpcClassicLinkDnsSupport": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Disables ClassicLink DNS support for a VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableVpcClassicLinkDnsSupport.html"
  },
  "ec2:DisassociateAddress": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Disassociates an Elastic IP address from the instance or network interface it's associated with.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateAddress.html"
  },
  "ec2:DisassociateClientVpnTargetNetwork": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::ClientVpnEndpoint"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Disassociates a target network from the specified Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateClientVpnTargetNetwork.html"
  },
  "ec2:DisassociateIamInstanceProfile": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [
      "ec2:AvailabilityZone",
      "ec2:EbsOptimized",
      "ec2:InstanceProfile",
      "ec2:InstanceType",
      "ec2:PlacementGroup",
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:RootDeviceType",
      "ec2:Tenancy"
    ],
    "Dependent Actions": [],
    "Description": "Disassociates an IAM instance profile from a running or stopped instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateIamInstanceProfile.html"
  },
  "ec2:DisassociateRouteTable": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Disassociates a subnet from a route table.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateRouteTable.html"
  },
  "ec2:DisassociateSubnetCidrBlock": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Disassociates a CIDR block from a subnet.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateSubnetCidrBlock.html"
  },
  "ec2:DisassociateTransitGatewayRouteTable": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGatewayRouteTable",
      "AWS::Ec2::TransitGatewayAttachment"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Disassociates a resource attachment from a transit gateway route table.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateTransitGatewayRouteTable.html"
  },
  "ec2:DisassociateVpcCidrBlock": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Disassociates a CIDR block from a VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateVpcCidrBlock.html"
  },
  "ec2:EnableEbsEncryptionByDefault": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Enables EBS encryption by default for your account in the current Region",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableEbsEncryptionByDefault.html"
  },
  "ec2:EnableFastSnapshotRestores": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Snapshot"
    ],
    "Condition Keys": [
      "ec2:Owner",
      "ec2:ParentVolume",
      "ec2:Region",
      "ec2:AvailabilityZone",
      "ec2:SnapshotTime",
      "ec2:Encrypted",
      "ec2:VolumeSize",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Enables fast snapshot restores for the specified snapshots in the specified Availability Zones",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableFastSnapshotRestores.html"
  },
  "ec2:EnableTransitGatewayRouteTablePropagation": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGatewayRouteTable",
      "AWS::Ec2::TransitGatewayAttachment"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Enables the specified attachment to propagate routes to the specified propagation route table.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableTransitGatewayRouteTablePropagation.html"
  },
  "ec2:EnableVgwRoutePropagation": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Enables a virtual private gateway (VGW) to propagate routes to the specified route table of a VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableVgwRoutePropagation.html"
  },
  "ec2:EnableVolumeIO": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Enables I/O operations for a volume that had I/O operations disabled because the data on the volume was potentially inconsistent.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableVolumeIO.html"
  },
  "ec2:EnableVpcClassicLink": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::VpcPeeringConnection",
      "AWS::Ec2::Vpc"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Tenancy"
    ],
    "Dependent Actions": [],
    "Description": "Enables a VPC for ClassicLink.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableVpcClassicLink.html"
  },
  "ec2:EnableVpcClassicLinkDnsSupport": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Enables a VPC to support DNS hostname resolution for ClassicLink.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableVpcClassicLinkDnsSupport.html"
  },
  "ec2:ExportClientVpnClientCertificateRevocationList": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Downloads the client certificate revocation list for the specified Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportClientVpnClientCertificateRevocationList.html"
  },
  "ec2:ExportClientVpnClientConfiguration": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Downloads the contents of the Client VPN endpoint configuration file for the specified Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportClientVpnClientConfiguration.html"
  },
  "ec2:ExportImage": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Exports an Amazon Machine Image (AMI) to a VM file.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportImage.html"
  },
  "ec2:ExportTransitGatewayRoutes": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Exports routes from the specified transit gateway route table to the specified S3 bucket.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportTransitGatewayRoutes.html"
  },
  "ec2:GetCapacityReservationUsage": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Gets usage information about a Capacity Reservation.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetCapacityReservationUsage.html"
  },
  "ec2:GetConsoleOutput": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Gets the console output for the specified instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetConsoleOutput.html"
  },
  "ec2:GetConsoleScreenshot": {
    "Access": "Read",
    "Affects": [
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [
      "ec2:AvailabilityZone",
      "ec2:EbsOptimized",
      "ec2:InstanceProfile",
      "ec2:InstanceType",
      "ec2:PlacementGroup",
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:RootDeviceType",
      "ec2:Tenancy"
    ],
    "Dependent Actions": [],
    "Description": "Retrieve a JPG-format screenshot of a running instance to help with troubleshooting.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetConsoleScreenshot.html"
  },
  "ec2:GetEbsDefaultKmsKeyId": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Get EBS Default Kms Key Id",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetEbsDefaultKmsKeyId.html"
  },
  "ec2:GetEbsEncryptionByDefault": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Describes whether EBS encryption by default is enabled for your account in the current Region",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetEbsEncryptionByDefault.html"
  },
  "ec2:GetHostReservationPurchasePreview": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Preview a reservation purchase with configurations that match those of your Dedicated Host.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetHostReservationPurchasePreview.html"
  },
  "ec2:GetLaunchTemplateData": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Retrieves the configuration data of the specified instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetLaunchTemplateData.html"
  },
  "ec2:GetPasswordData": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Retrieves the encrypted administrator password for an instance running Windows.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html"
  },
  "ec2:GetReservedInstancesExchangeQuote": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Returns details about the values and term of your specified Convertible Reserved Instances.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetReservedInstancesExchangeQuote.html"
  },
  "ec2:GetTransitGatewayAttachmentPropagations": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Lists the route tables to which the specified resource attachment propagates routes.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayAttachmentPropagations.html"
  },
  "ec2:GetTransitGatewayRouteTableAssociations": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Gets information about the associations for the specified transit gateway route table.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayRouteTableAssociations.html"
  },
  "ec2:GetTransitGatewayRouteTablePropagations": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Gets information about the route table propagations for the specified transit gateway route table.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayRouteTablePropagations.html"
  },
  "ec2:ImportClientVpnClientCertificateRevocationList": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::ClientVpnEndpoint"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Uploads a client certificate revocation list to the specified Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportClientVpnClientCertificateRevocationList.html"
  },
  "ec2:ImportImage": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Import single or multi-volume disk images or EBS snapshots into an Amazon Machine Image (AMI).",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportImage.html"
  },
  "ec2:ImportInstance": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates an import instance task using metadata from the specified disk image.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html"
  },
  "ec2:ImportKeyPair": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Imports the public key from an RSA key pair that you created with a third-party tool.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportKeyPair.html"
  },
  "ec2:ImportSnapshot": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Imports a disk into an EBS snapshot.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportSnapshot.html"
  },
  "ec2:ImportVolume": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates an import volume task using metadata from the specified disk image.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportVolume.html"
  },
  "ec2:ModifyCapacityReservation": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::CapacityReservation"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Modifies a Capacity Reservation's capacity and the conditions under which it is to be released.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyCapacityReservation.html"
  },
  "ec2:ModifyClientVpnEndpoint": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::ClientVpnEndpoint"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Modifies the specified Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyClientVpnEndpoint.html"
  },
  "ec2:ModifyEbsDefaultKmsKeyId": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Changes the default customer master key (CMK) for EBS encryption by default for your account in this Region",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyEbsDefaultKmsKeyId.html"
  },
  "ec2:ModifyFleet": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the specified EC2 Fleet.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFleet.html"
  },
  "ec2:ModifyFpgaImageAttribute": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the specified attribute of the specified Amazon FPGA Image (AFI).",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFpgaImageAttribute.html"
  },
  "ec2:ModifyHosts": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modify the auto-placement setting of a Dedicated Host.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyHosts.html"
  },
  "ec2:ModifyIdFormat": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the ID format for the specified resource on a per-region basis.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIdFormat.html"
  },
  "ec2:ModifyIdentityIdFormat": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the ID format of a resource for a specified IAM user, IAM role, or the root user for an account; or all IAM users, IAM roles, and the root user for an account.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIdentityIdFormat.html"
  },
  "ec2:ModifyImageAttribute": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the specified attribute of the specified AMI.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html"
  },
  "ec2:ModifyInstanceAttribute": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the specified attribute of the specified instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceAttribute.html"
  },
  "ec2:ModifyInstanceCapacityReservationAttributes": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the Capacity Reservation settings for a stopped instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceCapacityReservationAttributes.html"
  },
  "ec2:ModifyInstanceCreditSpecification": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the credit option for CPU usage on an instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceCreditSpecification.html"
  },
  "ec2:ModifyInstanceEventStartTime": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [
      "ec2:Region"
    ],
    "Dependent Actions": [],
    "Description": "Modifies the start time for a scheduled EC2 instance event.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceEventStartTime.html"
  },
  "ec2:ModifyInstanceMetadataOptions": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the metadata options for an instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceMetadataOptions.html"
  },
  "ec2:ModifyInstancePlacement": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Set the instance affinity value for a specific stopped instance and modify the instance tenancy setting.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstancePlacement.html"
  },
  "ec2:ModifyLaunchTemplate": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::LaunchTemplate"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Modifies the specified launch template.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyLaunchTemplate.html"
  },
  "ec2:ModifyNetworkInterfaceAttribute": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the specified network interface attribute. You can specify only one attribute at a time.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyNetworkInterfaceAttribute.html"
  },
  "ec2:ModifyReservedInstances": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the Availability Zone, instance count, instance type, or network platform (EC2-Classic or EC2-VPC) of your Standard Reserved Instances.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyReservedInstances.html"
  },
  "ec2:ModifySnapshotAttribute": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Ec2::Snapshot"
    ],
    "Condition Keys": [
      "ec2:Owner",
      "ec2:ParentVolume",
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:SnapshotTime",
      "ec2:VolumeSize"
    ],
    "Dependent Actions": [],
    "Description": "Adds or removes permission settings for the specified snapshot.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySnapshotAttribute.html"
  },
  "ec2:ModifySpotFleetRequest": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the specified Spot fleet request.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySpotFleetRequest.html"
  },
  "ec2:ModifySubnetAttribute": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies a subnet attribute.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySubnetAttribute.html"
  },
  "ec2:ModifyTrafficMirrorFilterNetworkServices": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TrafficMirrorFilterRule",
      "AWS::Ec2::TrafficMirrorFilter"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Allows or restricts mirroring network services.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTrafficMirrorFilterNetworkServices.html"
  },
  "ec2:ModifyTrafficMirrorFilterRule": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TrafficMirrorFilterRule",
      "AWS::Ec2::TrafficMirrorFilter"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Modifies the specified Traffic Mirror rule.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTrafficMirrorFilterRule.html"
  },
  "ec2:ModifyTrafficMirrorSession": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TrafficMirrorSession",
      "AWS::Ec2::TrafficMirrorFilter",
      "AWS::Ec2::TrafficMirrorTarget"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Modifies a Traffic Mirror session.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTrafficMirrorSession.html"
  },
  "ec2:ModifyTransitGatewayVpcAttachment": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGatewayAttachment",
      "AWS::Ec2::Subnet"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Modifies the specified VPC attachment.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTransitGatewayVpcAttachment.html"
  },
  "ec2:ModifyVolume": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "You can modify several parameters of an existing EBS volume, including volume size, volume type, and IOPS capacity.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVolume.html"
  },
  "ec2:ModifyVolumeAttribute": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies a volume attribute.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVolumeAttribute.html"
  },
  "ec2:ModifyVpcAttribute": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the specified attribute of the specified VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcAttribute.html"
  },
  "ec2:ModifyVpcEndpoint": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies attributes of a specified VPC endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.html"
  },
  "ec2:ModifyVpcEndpointConnectionNotification": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies a connection notification for VPC endpoint or VPC endpoint service.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpointConnectionNotification.html"
  },
  "ec2:ModifyVpcEndpointServiceConfiguration": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the attributes of your VPC endpoint service configuration.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpointServiceConfiguration.html"
  },
  "ec2:ModifyVpcEndpointServicePermissions": {
    "Access": "Permissions Management",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the permissions for your VPC endpoint service.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpointServicePermissions.html"
  },
  "ec2:ModifyVpcPeeringConnectionOptions": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the VPC peering connection options on one side of a VPC peering connection.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcPeeringConnectionOptions.html"
  },
  "ec2:ModifyVpcTenancy": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the instance tenancy attribute of the specified VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcTenancy.html"
  },
  "ec2:ModifyVpnConnection": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::VpnConnection"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:GatewayType"
    ],
    "Dependent Actions": [],
    "Description": "Modifies the target gateway of a AWS Site-to-Site VPN connection",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpnConnection.html"
  },
  "ec2:ModifyVpnTunnelCertificate": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Modifies the certificate for an AWS Site-to-Site VPN connection.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpnTunnelCertificate"
  },
  "ec2:ModifyVpnTunnelOptions": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::VpnConnection"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:AuthenticationType",
      "ec2:DPDTimeoutSeconds",
      "ec2:IKEVersions",
      "ec2:InsideTunnelCidr",
      "ec2:Phase1DHGroupNumbers",
      "ec2:Phase2DHGroupNumbers",
      "ec2:Phase1EncryptionAlgorithms",
      "ec2:Phase2EncryptionAlgorithms",
      "ec2:Phase1IntegrityAlgorithms",
      "ec2:Phase2IntegrityAlgorithms",
      "ec2:Phase1LifetimeSeconds",
      "ec2:Phase2LifetimeSeconds",
      "ec2:PresharedKeys",
      "ec2:RekeyFuzzPercentage",
      "ec2:RekeyMarginTimeSeconds",
      "ec2:RoutingType"
    ],
    "Dependent Actions": [],
    "Description": "Modifies the options for an AWS Site-to-Site VPN connection.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpnTunnelOptions.html"
  },
  "ec2:MonitorInstances": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Enables detailed monitoring for a running instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MonitorInstances.html"
  },
  "ec2:MoveAddressToVpc": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Moves an Elastic IP address from the EC2-Classic platform to the EC2-VPC platform.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MoveAddressToVpc.html"
  },
  "ec2:ProvisionByoipCidr": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Provisions an address range for use with your AWS resources through bring your own IP addresses (BYOIP) and creates a corresponding address pool.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ProvisionByoipCidr.html"
  },
  "ec2:PurchaseHostReservation": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Purchase a reservation with configurations that match those of your Dedicated Host.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseHostReservation.html"
  },
  "ec2:PurchaseReservedInstancesOffering": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Purchases a Reserved Instance for use with your account.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseReservedInstancesOffering.html"
  },
  "ec2:PurchaseScheduledInstances": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Purchases one or more Scheduled Instances with the specified schedule.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseScheduledInstances.html"
  },
  "ec2:RebootInstances": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [
      "ec2:AvailabilityZone",
      "ec2:EbsOptimized",
      "ec2:InstanceProfile",
      "ec2:InstanceType",
      "ec2:PlacementGroup",
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:RootDeviceType",
      "ec2:Tenancy"
    ],
    "Dependent Actions": [],
    "Description": "Requests a reboot of one or more instances.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RebootInstances.html"
  },
  "ec2:RegisterImage": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Registers an AMI.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisterImage.html"
  },
  "ec2:RejectTransitGatewayVpcAttachment": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGatewayAttachment"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Rejects a request to attach a VPC to a transit gateway.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RejectTransitGatewayVpcAttachment.html"
  },
  "ec2:RejectVpcEndpointConnections": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Rejects one or more VPC endpoint connection requests to your VPC endpoint service.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RejectVpcEndpointConnections.html"
  },
  "ec2:RejectVpcPeeringConnection": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::VpcPeeringConnection"
    ],
    "Condition Keys": [
      "ec2:AccepterVpc",
      "ec2:Region",
      "ec2:RequesterVpc",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Rejects a VPC peering connection request.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RejectVpcPeeringConnection.html"
  },
  "ec2:ReleaseAddress": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Releases the specified Elastic IP address.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReleaseAddress.html"
  },
  "ec2:ReleaseHosts": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "When you no longer want to use an On-Demand Dedicated Host it can be released",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReleaseHosts.html"
  },
  "ec2:ReplaceIamInstanceProfileAssociation": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [
      "ec2:AvailabilityZone",
      "ec2:EbsOptimized",
      "ec2:InstanceProfile",
      "ec2:InstanceType",
      "ec2:PlacementGroup",
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:RootDeviceType",
      "ec2:Tenancy"
    ],
    "Dependent Actions": [
      "iam:PassRole"
    ],
    "Description": "Replaces an IAM instance profile for the specified instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceIamInstanceProfileAssociation.html"
  },
  "ec2:ReplaceNetworkAclAssociation": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Changes which network ACL a subnet is associated with.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceNetworkAclAssociation.html"
  },
  "ec2:ReplaceNetworkAclEntry": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Replaces an entry (rule) in a network ACL.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceNetworkAclEntry.html"
  },
  "ec2:ReplaceRoute": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::RouteTable"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Vpc"
    ],
    "Dependent Actions": [],
    "Description": "Replaces an existing route within a route table in a VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceRoute.html"
  },
  "ec2:ReplaceRouteTableAssociation": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Changes the route table associated with a given subnet in a VPC.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceRouteTableAssociation.html"
  },
  "ec2:ReplaceTransitGatewayRoute": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::TransitGatewayAttachment",
      "AWS::Ec2::TransitGatewayRouteTable"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Replaces the specified route in the specified transit gateway route table.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceTransitGatewayRoute.html"
  },
  "ec2:ReportInstanceStatus": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Submits feedback about the status of an instance",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReportInstanceStatus.html"
  },
  "ec2:RequestSpotFleet": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a Spot fleet request",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet.html"
  },
  "ec2:RequestSpotInstances": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a Spot instance request",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html"
  },
  "ec2:ResetEbsDefaultKmsKeyId": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Resets the default customer master key (CMK) for EBS encryption for your account in this Region to the AWS managed CMK for EBS",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetEbsDefaultKmsKeyId.html"
  },
  "ec2:ResetFpgaImageAttribute": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Resets an attribute of an Amazon FPGA Image (AFI) to its default value.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetFpgaImageAttribute.html"
  },
  "ec2:ResetImageAttribute": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Resets an attribute of an AMI to its default value",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetImageAttribute.html"
  },
  "ec2:ResetInstanceAttribute": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Resets an attribute of an instance to its default value",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetInstanceAttribute.html"
  },
  "ec2:ResetNetworkInterfaceAttribute": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Resets a network interface attribute. You can specify only one attribute at a time.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetNetworkInterfaceAttribute.html"
  },
  "ec2:ResetSnapshotAttribute": {
    "Access": "Permissions Management",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Resets permission settings for the specified snapshot.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetSnapshotAttribute.html"
  },
  "ec2:RestoreAddressToClassic": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Restores an Elastic IP address that was previously moved to the EC2-VPC platform back to the EC2-Classic platform.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RestoreAddressToClassic.html"
  },
  "ec2:RevokeClientVpnIngress": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::ClientVpnEndpoint"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Removes an ingress authorization rule from a Client VPN endpoint.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeClientVpnIngress.html"
  },
  "ec2:RevokeSecurityGroupEgress": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::SecurityGroup"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Vpc"
    ],
    "Dependent Actions": [],
    "Description": "[EC2-VPC only] Removes one or more egress rules from a security group for EC2-VPC. This action doesn't apply to security groups for use in EC2-Classic.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html"
  },
  "ec2:RevokeSecurityGroupIngress": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::SecurityGroup"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Vpc"
    ],
    "Dependent Actions": [],
    "Description": "Removes one or more ingress rules from a security group.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupIngress.html"
  },
  "ec2:RunInstances": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Volume",
      "AWS::Ec2::Snapshot",
      "AWS::Ec2::SecurityGroup",
      "AWS::Ec2::NetworkInterface",
      "AWS::Ec2::Subnet",
      "AWS::Ec2::KeyPair",
      "AWS::Ec2::LaunchTemplate",
      "AWS::Ec2::Image",
      "AWS::Ec2::PlacementGroup",
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [
      "ec2:Vpc",
      "ec2:Public",
      "ec2:InstanceType",
      "ec2:Tenancy",
      "ec2:AvailabilityZone",
      "ec2:ImageType",
      "ec2:ResourceTag/",
      "ec2:MetadataHttpTokens",
      "ec2:PlacementGroup",
      "ec2:VolumeType",
      "ec2:Region",
      "ec2:ParentSnapshot",
      "ec2:VolumeSize",
      "ec2:Subnet",
      "aws:TagKeys",
      "ec2:MetadataHttpPutResponseHopLimit",
      "ec2:MetadataHttpEndpoint",
      "ec2:EbsOptimized",
      "ec2:RootDeviceType",
      "ec2:Encrypted",
      "ec2:PlacementGroupStrategy",
      "ec2:SnapshotTime",
      "ec2:InstanceProfile",
      "ec2:Owner",
      "aws:RequestTag/${TagKey}",
      "ec2:ResourceTag/${TagKey}",
      "ec2:LaunchTemplate",
      "ec2:ParentVolume",
      "ec2:VolumeIops",
      "ec2:IsLaunchTemplateResource"
    ],
    "Dependent Actions": [],
    "Description": "SCENARIO: EC2-VPC-InstanceStore-Subnet",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html"
  },
  "ec2:RunScheduledInstances": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Launches the specified Scheduled Instances.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunScheduledInstances.html"
  },
  "ec2:SearchTransitGatewayRoutes": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Searches for routes in the specified transit gateway route table.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SearchTransitGatewayRoutes.html"
  },
  "ec2:SendDiagnosticInterrupt": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [
      "ec2:AvailabilityZone",
      "ec2:EbsOptimized",
      "ec2:InstanceProfile",
      "ec2:InstanceType",
      "ec2:PlacementGroup",
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:RootDeviceType",
      "ec2:Tenancy"
    ],
    "Dependent Actions": [],
    "Description": "Sends a diagnostic interrupt to the specified Amazon EC2 instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SendDiagnosticInterrupt.html"
  },
  "ec2:StartInstances": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [
      "ec2:AvailabilityZone",
      "ec2:EbsOptimized",
      "ec2:InstanceProfile",
      "ec2:InstanceType",
      "ec2:PlacementGroup",
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:RootDeviceType",
      "ec2:Tenancy"
    ],
    "Dependent Actions": [],
    "Description": "Starts an Amazon EBS-backed AMI that you've previously stopped.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartInstances.html"
  },
  "ec2:StopInstances": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [
      "ec2:AvailabilityZone",
      "ec2:EbsOptimized",
      "ec2:InstanceProfile",
      "ec2:InstanceType",
      "ec2:PlacementGroup",
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:RootDeviceType",
      "ec2:Tenancy"
    ],
    "Dependent Actions": [],
    "Description": "Stops an Amazon EBS-backed instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StopInstances.html"
  },
  "ec2:TerminateClientVpnConnections": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::ClientVpnEndpoint"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}"
    ],
    "Dependent Actions": [],
    "Description": "Terminates active Client VPN endpoint connections.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateClientVpnConnections.html"
  },
  "ec2:TerminateInstances": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::Instance"
    ],
    "Condition Keys": [
      "ec2:AvailabilityZone",
      "ec2:EbsOptimized",
      "ec2:InstanceProfile",
      "ec2:InstanceType",
      "ec2:PlacementGroup",
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:RootDeviceType",
      "ec2:Tenancy"
    ],
    "Dependent Actions": [],
    "Description": "Shuts down one or more instances.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html"
  },
  "ec2:UnassignIpv6Addresses": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Unassigns one or more IPv6 addresses from the specified network interface.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnassignIpv6Addresses.html"
  },
  "ec2:UnassignPrivateIpAddresses": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Unassigns one or more secondary private IP addresses from a network interface.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnassignPrivateIpAddresses.html"
  },
  "ec2:UnmonitorInstances": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Disables detailed monitoring for a running instance.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnmonitorInstances.html"
  },
  "ec2:UpdateSecurityGroupRuleDescriptionsEgress": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::SecurityGroup"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Vpc"
    ],
    "Dependent Actions": [],
    "Description": "[EC2-VPC only] Update descriptions for one or more egress rules of a security group. This action doesn't apply to security groups for use in EC2-Classic.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsEgress.html"
  },
  "ec2:UpdateSecurityGroupRuleDescriptionsIngress": {
    "Access": "Write",
    "Affects": [
      "AWS::Ec2::SecurityGroup"
    ],
    "Condition Keys": [
      "ec2:Region",
      "ec2:ResourceTag/${TagKey}",
      "ec2:Vpc"
    ],
    "Dependent Actions": [],
    "Description": "Update descriptions for one or more ingress rules of a security group.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsIngress.html"
  },
  "ec2:WithdrawByoipCidr": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Stops advertising an IPv4 address range that is provisioned as an address pool.",
    "Reference": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_WithdrawByoipCidr.html"
  },
  "iam:AddClientIDToOpenIDConnectProvider": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::OidcProvider"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to add a new client ID (audience) to the list of registered IDs for the specified IAM OpenID Connect (OIDC) provider resource",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_AddClientIDToOpenIDConnectProvider.html"
  },
  "iam:AddRoleToInstanceProfile": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::InstanceProfile"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to add an IAM role to the specified instance profile",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_AddRoleToInstanceProfile.html"
  },
  "iam:AddUserToGroup": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Group"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to add an IAM user to the specified IAM group",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_AddUserToGroup.html"
  },
  "iam:AttachGroupPolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Group"
    ],
    "Condition Keys": [
      "iam:PolicyARN"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to attach a managed policy to the specified IAM group",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_AttachGroupPolicy.html"
  },
  "iam:AttachRolePolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [
      "iam:PermissionsBoundary",
      "iam:PolicyARN"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to attach a managed policy to the specified IAM role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_AttachRolePolicy.html"
  },
  "iam:AttachUserPolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [
      "iam:PermissionsBoundary",
      "iam:PolicyARN"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to attach a managed policy to the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_AttachUserPolicy.html"
  },
  "iam:ChangePassword": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission for an IAM user to to change their own password",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ChangePassword.html"
  },
  "iam:CreateAccessKey": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to create access key and secret access key for the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateAccessKey.html"
  },
  "iam:CreateAccountAlias": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to create an alias for your AWS account",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateAccountAlias.html"
  },
  "iam:CreateGroup": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Group"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to create a new group",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateGroup.html"
  },
  "iam:CreateInstanceProfile": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::InstanceProfile"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to create a new instance profile",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateInstanceProfile.html"
  },
  "iam:CreateLoginProfile": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to create a password for the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateLoginProfile.html"
  },
  "iam:CreateOpenIDConnectProvider": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::OidcProvider"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to create an IAM resource that describes an identity provider (IdP) that supports OpenID Connect (OIDC)",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html"
  },
  "iam:CreatePolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Policy"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to create a new managed policy",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicy.html"
  },
  "iam:CreatePolicyVersion": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Policy"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to create a new version of the specified managed policy",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicyVersion.html"
  },
  "iam:CreateRole": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [
      "iam:PermissionsBoundary"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to create a new role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html"
  },
  "iam:CreateSAMLProvider": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::SamlProvider"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to create an IAM resource that describes an identity provider (IdP) that supports SAML 2.0",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateSAMLProvider.html"
  },
  "iam:CreateServiceLinkedRole": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [
      "iam:AWSServiceName"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to create an IAM role that allows an AWS service to perform actions on your behalf",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateServiceLinkedRole.html"
  },
  "iam:CreateServiceSpecificCredential": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to create a new service-specific credential for an IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateServiceSpecificCredential.html"
  },
  "iam:CreateUser": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [
      "iam:PermissionsBoundary"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to create a new IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateUser.html"
  },
  "iam:CreateVirtualMFADevice": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Mfa"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to create a new virtual MFA device",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateVirtualMFADevice.html"
  },
  "iam:DeactivateMFADevice": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to deactivate the specified MFA device and remove its association with the IAM user for which it was originally enabled",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeactivateMFADevice.html"
  },
  "iam:DeleteAccessKey": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete the access key pair that is associated with the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteAccessKey.html"
  },
  "iam:DeleteAccountAlias": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete the specified AWS account alias",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteAccountAlias.html"
  },
  "iam:DeleteAccountPasswordPolicy": {
    "Access": "Permissions Management",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete the password policy for the AWS account",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteAccountPasswordPolicy.html"
  },
  "iam:DeleteGroup": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Group"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete the specified IAM group",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteGroup.html"
  },
  "iam:DeleteGroupPolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Group"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete the specified inline policy from its group",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteGroupPolicy.html"
  },
  "iam:DeleteInstanceProfile": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::InstanceProfile"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete the specified instance profile",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteInstanceProfile.html"
  },
  "iam:DeleteLoginProfile": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete the password for the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteLoginProfile.html"
  },
  "iam:DeleteOpenIDConnectProvider": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::OidcProvider"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete an OpenID Connect identity provider (IdP) resource object in IAM",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteOpenIDConnectProvider.html"
  },
  "iam:DeletePolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Policy"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete the specified managed policy and remove it from any IAM entities (users, groups, or roles) to which it is attached",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeletePolicy.html"
  },
  "iam:DeletePolicyVersion": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Policy"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete a version from the specified managed policy",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeletePolicyVersion.html"
  },
  "iam:DeleteRole": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete the specified role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteRole.html"
  },
  "iam:DeleteRolePermissionsBoundary": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [
      "iam:PermissionsBoundary"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to remove the permissions boundary from a role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteRolePermissionsBoundary.html"
  },
  "iam:DeleteRolePolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [
      "iam:PermissionsBoundary"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to delete the specified inline policy from the specified role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteRolePolicy.html"
  },
  "iam:DeleteSAMLProvider": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::SamlProvider"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete a SAML provider resource in IAM",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteSAMLProvider.html"
  },
  "iam:DeleteSSHPublicKey": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete the specified SSH public key",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteSSHPublicKey.html"
  },
  "iam:DeleteServerCertificate": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::ServerCertificate"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete the specified server certificate",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteServerCertificate.html"
  },
  "iam:DeleteServiceLinkedRole": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete an IAM role that is linked to a specific AWS service, if the service is no longer using it",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteServiceLinkedRole.html"
  },
  "iam:DeleteServiceSpecificCredential": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete the specified service-specific credential for an IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteServiceSpecificCredential.html"
  },
  "iam:DeleteSigningCertificate": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete a signing certificate that is associated with the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteSigningCertificate.html"
  },
  "iam:DeleteUser": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteUser.html"
  },
  "iam:DeleteUserPermissionsBoundary": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [
      "iam:PermissionsBoundary"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to remove the permissions boundary from the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteUserPermissionsBoundary.html"
  },
  "iam:DeleteUserPolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [
      "iam:PermissionsBoundary"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to delete the specified inline policy from an IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteUserPolicy.html"
  },
  "iam:DeleteVirtualMFADevice": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::SmsMfa",
      "AWS::Iam::Mfa"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to delete a virtual MFA device",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteVirtualMFADevice.html"
  },
  "iam:DetachGroupPolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Group"
    ],
    "Condition Keys": [
      "iam:PolicyARN"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to detach a managed policy from the specified IAM group",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DetachGroupPolicy.html"
  },
  "iam:DetachRolePolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [
      "iam:PermissionsBoundary",
      "iam:PolicyARN"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to detach a managed policy from the specified role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DetachRolePolicy.html"
  },
  "iam:DetachUserPolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [
      "iam:PermissionsBoundary",
      "iam:PolicyARN"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to detach a managed policy from the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_DetachUserPolicy.html"
  },
  "iam:EnableMFADevice": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to enable an MFA device and associate it with the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_EnableMFADevice.html"
  },
  "iam:GenerateCredentialReport": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to generate a credential report for the AWS account",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GenerateCredentialReport.html"
  },
  "iam:GenerateOrganizationsAccessReport": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::AccessReport"
    ],
    "Condition Keys": [
      "iam:OrganizationsPolicyId"
    ],
    "Dependent Actions": [
      "organizations:ListParents",
      "organizations:ListPoliciesForTarget",
      "organizations:ListTargetsForPolicy",
      "organizations:ListRoots",
      "organizations:ListChildren",
      "organizations:DescribePolicy"
    ],
    "Description": "Grants permission to generate an access report for an AWS Organizations entity",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GenerateOrganizationsAccessReport.html"
  },
  "iam:GenerateServiceLastAccessedDetails": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to generate a service last accessed data report for an IAM resource",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GenerateServiceLastAccessedDetails.html"
  },
  "iam:GetAccessKeyLastUsed": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve information about when the specified access key was last used",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccessKeyLastUsed.html"
  },
  "iam:GetAccountAuthorizationDetails": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve information about all IAM users, groups, roles, and policies in your AWS account, including their relationships to one another",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountAuthorizationDetails.html"
  },
  "iam:GetAccountPasswordPolicy": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve the password policy for the AWS account",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountPasswordPolicy.html"
  },
  "iam:GetAccountSummary": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve information about IAM entity usage and IAM quotas in the AWS account",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountSummary.html"
  },
  "iam:GetContextKeysForCustomPolicy": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve a list of all of the context keys that are referenced in the specified policy",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetContextKeysForCustomPolicy.html"
  },
  "iam:GetContextKeysForPrincipalPolicy": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::Role",
      "AWS::Iam::Group",
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve a list of all context keys that are referenced in all IAM policies that are attached to the specified IAM identity (user, group, or role)",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetContextKeysForPrincipalPolicy.html"
  },
  "iam:GetCredentialReport": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve a credential report for the AWS account",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetCredentialReport.html"
  },
  "iam:GetGroup": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::Group"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve a list of IAM users in the specified IAM group",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetGroup.html"
  },
  "iam:GetGroupPolicy": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::Group"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve an inline policy document that is embedded in the specified IAM group",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetGroupPolicy.html"
  },
  "iam:GetInstanceProfile": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::InstanceProfile"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve information about the specified instance profile, including the instance profile's path, GUID, ARN, and role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetInstanceProfile.html"
  },
  "iam:GetLoginProfile": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve the user name and password creation date for the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetLoginProfile.html"
  },
  "iam:GetOpenIDConnectProvider": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::OidcProvider"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve information about the specified OpenID Connect (OIDC) provider resource in IAM",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetOpenIDConnectProvider.html"
  },
  "iam:GetOrganizationsAccessReport": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve an AWS Organizations access report",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetOrganizationsAccessReport.html"
  },
  "iam:GetPolicy": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::Policy"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve information about the specified managed policy, including the policy's default version and the total number of identities to which the policy is attached",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetPolicy.html"
  },
  "iam:GetPolicyVersion": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::Policy"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve information about a version of the specified managed policy, including the policy document",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetPolicyVersion.html"
  },
  "iam:GetRole": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve information about the specified role, including the role's path, GUID, ARN, and the role's trust policy",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRole.html"
  },
  "iam:GetRolePolicy": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve an inline policy document that is embedded with the specified IAM role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRolePolicy.html"
  },
  "iam:GetSAMLProvider": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::SamlProvider"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve the SAML provider metadocument that was uploaded when the IAM SAML provider resource was created or updated",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetSAMLProvider.html"
  },
  "iam:GetSSHPublicKey": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve the specified SSH public key, including metadata about the key",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetSSHPublicKey.html"
  },
  "iam:GetServerCertificate": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::ServerCertificate"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve information about the specified server certificate stored in IAM",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServerCertificate.html"
  },
  "iam:GetServiceLastAccessedDetails": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve information about the service last accessed data report",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLastAccessedDetails.html"
  },
  "iam:GetServiceLastAccessedDetailsWithEntities": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve information about the entities from the service last accessed data report",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLastAccessedDetailsWithEntities.html"
  },
  "iam:GetServiceLinkedRoleDeletionStatus": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve an IAM service-linked role deletion status",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLinkedRoleDeletionStatus.html"
  },
  "iam:GetUser": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve information about the specified IAM user, including the user's creation date, path, unique ID, and ARN",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetUser.html"
  },
  "iam:GetUserPolicy": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to retrieve an inline policy document that is embedded in the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetUserPolicy.html"
  },
  "iam:ListAccessKeys": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list information about the access key IDs that are associated with the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccessKeys.html"
  },
  "iam:ListAccountAliases": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the account alias that is associated with the AWS account",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccountAliases.html"
  },
  "iam:ListAttachedGroupPolicies": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::Group"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list all managed policies that are attached to the specified IAM group",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAttachedGroupPolicies.html"
  },
  "iam:ListAttachedRolePolicies": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list all managed policies that are attached to the specified IAM role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAttachedRolePolicies.html"
  },
  "iam:ListAttachedUserPolicies": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list all managed policies that are attached to the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAttachedUserPolicies.html"
  },
  "iam:ListEntitiesForPolicy": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::Policy"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list all IAM identities to which the specified managed policy is attached",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListEntitiesForPolicy.html"
  },
  "iam:ListGroupPolicies": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::Group"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the names of the inline policies that are embedded in the specified IAM group",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroupPolicies.html"
  },
  "iam:ListGroups": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the IAM groups that have the specified path prefix",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroups.html"
  },
  "iam:ListGroupsForUser": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the IAM groups that the specified IAM user belongs to",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroupsForUser.html"
  },
  "iam:ListInstanceProfiles": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::InstanceProfile"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the instance profiles that have the specified path prefix",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListInstanceProfiles.html"
  },
  "iam:ListInstanceProfilesForRole": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the instance profiles that have the specified associated IAM role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListInstanceProfilesForRole.html"
  },
  "iam:ListMFADevices": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the MFA devices for an IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListMFADevices.html"
  },
  "iam:ListOpenIDConnectProviders": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list information about the IAM OpenID Connect (OIDC) provider resource objects that are defined in the AWS account",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListOpenIDConnectProviders.html"
  },
  "iam:ListPolicies": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list all managed policies",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPolicies.html"
  },
  "iam:ListPoliciesGrantingServiceAccess": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list information about the policies that grant an entity access to a specific service",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPoliciesGrantingServiceAccess.html"
  },
  "iam:ListPolicyVersions": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::Policy"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list information about the versions of the specified managed policy, including the version that is currently set as the policy's default version",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPolicyVersions.html"
  },
  "iam:ListRolePolicies": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the names of the inline policies that are embedded in the specified IAM role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListRolePolicies.html"
  },
  "iam:ListRoleTags": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the tags that are attached to the specified IAM role.",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListRoleTags.html"
  },
  "iam:ListRoles": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the IAM roles that have the specified path prefix",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListRoles.html"
  },
  "iam:ListSAMLProviders": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the SAML provider resources in IAM",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListSAMLProviders.html"
  },
  "iam:ListSSHPublicKeys": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list information about the SSH public keys that are associated with the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListSSHPublicKeys.html"
  },
  "iam:ListServerCertificates": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the server certificates that have the specified path prefix",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListServerCertificates.html"
  },
  "iam:ListServiceSpecificCredentials": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the service-specific credentials that are associated with the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListServiceSpecificCredentials.html"
  },
  "iam:ListSigningCertificates": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list information about the signing certificates that are associated with the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListSigningCertificates.html"
  },
  "iam:ListUserPolicies": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the names of the inline policies that are embedded in the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUserPolicies.html"
  },
  "iam:ListUserTags": {
    "Access": "List",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the tags that are attached to the specified IAM user.",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUserTags.html"
  },
  "iam:ListUsers": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list the IAM users that have the specified path prefix",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUsers.html"
  },
  "iam:ListVirtualMFADevices": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to list virtual MFA devices by assignment status",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListVirtualMFADevices.html"
  },
  "iam:PassRole": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [
      "iam:PassedToService"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to pass a role to a service",
    "Reference": ""
  },
  "iam:PutGroupPolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Group"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to create or update an inline policy document that is embedded in the specified IAM group",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutGroupPolicy.html"
  },
  "iam:PutRolePermissionsBoundary": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [
      "iam:PermissionsBoundary"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to set a managed policy as a permissions boundary for a role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutRolePermissionsBoundary.html"
  },
  "iam:PutRolePolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [
      "iam:PermissionsBoundary"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to create or update an inline policy document that is embedded in the specified IAM role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutRolePolicy.html"
  },
  "iam:PutUserPermissionsBoundary": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [
      "iam:PermissionsBoundary"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to set a managed policy as a permissions boundary for an IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutUserPermissionsBoundary.html"
  },
  "iam:PutUserPolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [
      "iam:PermissionsBoundary"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to create or update an inline policy document that is embedded in the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutUserPolicy.html"
  },
  "iam:RemoveClientIDFromOpenIDConnectProvider": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::OidcProvider"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to remove the client ID (audience) from the list of client IDs in the specified IAM OpenID Connect (OIDC) provider resource",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_RemoveClientIDFromOpenIDConnectProvider.html"
  },
  "iam:RemoveRoleFromInstanceProfile": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::InstanceProfile"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to remove an IAM role from the specified EC2 instance profile",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_RemoveRoleFromInstanceProfile.html"
  },
  "iam:RemoveUserFromGroup": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Group"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to remove an IAM user from the specified group",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_RemoveUserFromGroup.html"
  },
  "iam:ResetServiceSpecificCredential": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to reset the password for an existing service-specific credential for an IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ResetServiceSpecificCredential.html"
  },
  "iam:ResyncMFADevice": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to synchronize the specified MFA device with its IAM entity (user or role)",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_ResyncMFADevice.html"
  },
  "iam:SetDefaultPolicyVersion": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Policy"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to set the version of the specified policy as the policy's default version",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_SetDefaultPolicyVersion.html"
  },
  "iam:SetSecurityTokenServicePreferences": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to set the STS global endpoint token version",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_SetSecurityTokenServicePreferences.html"
  },
  "iam:SimulateCustomPolicy": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to simulate whether an identity-based policy or resource-based policy provides permissions for specific API operations and resources",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_SimulateCustomPolicy.html"
  },
  "iam:SimulatePrincipalPolicy": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::Role",
      "AWS::Iam::Group",
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to simulate whether an identity-based policy that is attached to a specified IAM entity (user or role) provides permissions for specific API operations and resources",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_SimulatePrincipalPolicy.html"
  },
  "iam:TagRole": {
    "Access": "Tagging",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to add tags to an IAM role.",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_TagRole.html"
  },
  "iam:TagUser": {
    "Access": "Tagging",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to add tags to an IAM user.",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_TagUser.html"
  },
  "iam:UntagRole": {
    "Access": "Tagging",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to remove the specified tags from the role.",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UntagRole.html"
  },
  "iam:UntagUser": {
    "Access": "Tagging",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to remove the specified tags from the user.",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UntagUser.html"
  },
  "iam:UpdateAccessKey": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to update the status of the specified access key as Active or Inactive",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAccessKey.html"
  },
  "iam:UpdateAccountPasswordPolicy": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to update the password policy settings for the AWS account",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAccountPasswordPolicy.html"
  },
  "iam:UpdateAssumeRolePolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to update the policy that grants an IAM entity permission to assume a role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAssumeRolePolicy.html"
  },
  "iam:UpdateGroup": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Group"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to update the name or path of the specified IAM group",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateGroup.html"
  },
  "iam:UpdateLoginProfile": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to change the password for the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateLoginProfile.html"
  },
  "iam:UpdateOpenIDConnectProviderThumbprint": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::OidcProvider"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to update the entire list of server certificate thumbprints that are associated with an OpenID Connect (OIDC) provider resource",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateOpenIDConnectProviderThumbprint.html"
  },
  "iam:UpdateRole": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to update the description or maximum session duration setting of a role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateRole.html"
  },
  "iam:UpdateRoleDescription": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to update only the description of a role",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateRoleDescription.html"
  },
  "iam:UpdateSAMLProvider": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::SamlProvider"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to update the metadata document for an existing SAML provider resource",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateSAMLProvider.html"
  },
  "iam:UpdateSSHPublicKey": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to update the status of an IAM user's SSH public key to active or inactive",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateSSHPublicKey.html"
  },
  "iam:UpdateServerCertificate": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::ServerCertificate"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to update the name or the path of the specified server certificate stored in IAM",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateServerCertificate.html"
  },
  "iam:UpdateServiceSpecificCredential": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to update the status of a service-specific credential to active or inactive for an IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateServiceSpecificCredential.html"
  },
  "iam:UpdateSigningCertificate": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to update the status of the specified user signing certificate to active or disabled",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateSigningCertificate.html"
  },
  "iam:UpdateUser": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to update the name or the path of the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateUser.html"
  },
  "iam:UploadSSHPublicKey": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to upload an SSH public key and associate it with the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UploadSSHPublicKey.html"
  },
  "iam:UploadServerCertificate": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::ServerCertificate"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to upload a server certificate entity for the AWS account",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UploadServerCertificate.html"
  },
  "iam:UploadSigningCertificate": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Grants permission to upload an X.509 signing certificate and associate it with the specified IAM user",
    "Reference": "https://docs.aws.amazon.com/IAM/latest/APIReference/API_UploadSigningCertificate.html"
  },
  "lambda:AddLayerVersionPermission": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Lambda::LayerVersion"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Adds a permission policy to a version of a function layer.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_AddLayerVersionPermission.html"
  },
  "lambda:AddPermission": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [
      "lambda:Principal"
    ],
    "Dependent Actions": [],
    "Description": "Adds a permission to the resource policy associated with the specified AWS Lambda function.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_AddPermission.html"
  },
  "lambda:CreateAlias": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates an alias that points to the specified Lambda function version.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_CreateAlias.html"
  },
  "lambda:CreateEventSourceMapping": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [
      "lambda:FunctionArn"
    ],
    "Dependent Actions": [],
    "Description": "Identifies a stream as an event source for a Lambda function.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_CreateEventSourceMapping.html"
  },
  "lambda:CreateFunction": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [
      "lambda:Layer"
    ],
    "Dependent Actions": [],
    "Description": "Creates a new Lambda function.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html"
  },
  "lambda:DeleteAlias": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes the specified Lambda function alias.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteAlias.html"
  },
  "lambda:DeleteEventSourceMapping": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::EventSourceMapping"
    ],
    "Condition Keys": [
      "lambda:FunctionArn"
    ],
    "Dependent Actions": [],
    "Description": "Removes an event source mapping.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteEventSourceMapping.html"
  },
  "lambda:DeleteFunction": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes the specified Lambda function code and configuration.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteFunction.html"
  },
  "lambda:DeleteFunctionConcurrency": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Remove concurrency limit set on a Lambda function.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteFunctionConcurrency.html"
  },
  "lambda:DeleteLayerVersion": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::LayerVersion"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Deletes a version of a function layer.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteLayerVersion.html"
  },
  "lambda:DisableReplication": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Removes resource policy permission that allows Lambda replication service to retrieve function code and configuration.",
    "Reference": ""
  },
  "lambda:EnableReplication": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Adds a permission to resource policy that gives Lambda replication service permission to get function code and configuration.",
    "Reference": ""
  },
  "lambda:GetAccountSettings": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Returns account limits and usage statistics, such as concurrency and code storage.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_GetAccountSettings.html"
  },
  "lambda:GetAlias": {
    "Access": "Read",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Returns the specified alias information such as the alias ARN, description, and function version it is pointing to.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_GetAlias.html"
  },
  "lambda:GetEventSourceMapping": {
    "Access": "Read",
    "Affects": [
      "AWS::Lambda::EventSourceMapping"
    ],
    "Condition Keys": [
      "lambda:FunctionArn"
    ],
    "Dependent Actions": [],
    "Description": "Returns configuration information for the specified event source mapping.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_GetEventSourceMapping.html"
  },
  "lambda:GetFunction": {
    "Access": "Read",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Returns the configuration information of the Lambda function and a presigned URL link to the .zip file you uploaded with CreateFunction so you can download the .zip file.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunction.html"
  },
  "lambda:GetFunctionConfiguration": {
    "Access": "Read",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Returns the configuration information of the Lambda function.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConfiguration.html"
  },
  "lambda:GetLayerVersion": {
    "Access": "Read",
    "Affects": [
      "AWS::Lambda::LayerVersion"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Returns information about a version of a function layer, with a link to download the layer archive that is valid for 10 minutes.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_GetLayerVersion.html"
  },
  "lambda:GetLayerVersionPolicy": {
    "Access": "Read",
    "Affects": [
      "AWS::Lambda::LayerVersion"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Returns the permissions policy for a layer version.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_GetLayerVersionPolicy.html"
  },
  "lambda:GetPolicy": {
    "Access": "Read",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Returns the resource policy associated with the specified Lambda function.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_GetPolicy.html"
  },
  "lambda:InvokeAsync": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Submits an invocation request to AWS Lambda. Is deprecated",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_InvokeAsync.html"
  },
  "lambda:InvokeFunction": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Invokes a specific Lambda function.",
    "Reference": ""
  },
  "lambda:ListAliases": {
    "Access": "List",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Returns list of aliases created for a Lambda function.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_ListAliases.html"
  },
  "lambda:ListEventSourceMappings": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Returns a list of event source mappings you created using the CreateEventSourceMapping.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_ListEventSourceMappings.html"
  },
  "lambda:ListFunctions": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Returns a list of your Lambda functions.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctions.html"
  },
  "lambda:ListLayerVersions": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Returns a list of your Lambda layer versions.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_ListLayerVersions.html"
  },
  "lambda:ListLayers": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Lists function layers and shows information about the latest version of each.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_ListLayers.html"
  },
  "lambda:ListTags": {
    "Access": "Read",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Lists tags for a Lambda function.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_ListTags.html"
  },
  "lambda:ListVersionsByFunction": {
    "Access": "List",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "List all versions of a function.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_ListVersionsByFunction.html"
  },
  "lambda:PublishLayerVersion": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::Layer",
      "AWS::Lambda::LayerVersion"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Creates a function layer from a ZIP archive. Each time you call PublishLayerVersion with the same version name, a new version is created.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_PublishLayerVersion.html"
  },
  "lambda:PublishVersion": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Publishes a version of your function from the current snapshot of $LATEST.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_PublishVersion.html"
  },
  "lambda:PutFunctionConcurrency": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Adds concurrency limit to a Lambda function.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_PutFunctionConcurrency.html"
  },
  "lambda:RemoveLayerVersionPermission": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Lambda::LayerVersion"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Removes a statement from the permissions policy for a layer version.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_RemoveLayerVersionPermission.html"
  },
  "lambda:RemovePermission": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [
      "lambda:Principal"
    ],
    "Dependent Actions": [],
    "Description": "You can remove individual permissions from an resource policy associated with a Lambda function by providing a statement ID that you provided when you added the permission.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_RemovePermission.html"
  },
  "lambda:TagResource": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Adds tags to a Lambda function.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_TagResources.html"
  },
  "lambda:UntagResource": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Removes tags from a Lambda function.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_UntagResource.html"
  },
  "lambda:UpdateAlias": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Using this API you can update the function version to which the alias points and the alias description.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateAlias.html"
  },
  "lambda:UpdateEventSourceMapping": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::EventSourceMapping"
    ],
    "Condition Keys": [
      "lambda:FunctionArn"
    ],
    "Dependent Actions": [],
    "Description": "You can update an event source mapping.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateEventSourceMapping.html"
  },
  "lambda:UpdateFunctionCode": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Updates the code for the specified Lambda function.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateFunctionCode.html"
  },
  "lambda:UpdateFunctionConfiguration": {
    "Access": "Write",
    "Affects": [
      "AWS::Lambda::Function"
    ],
    "Condition Keys": [
      "lambda:Layer"
    ],
    "Dependent Actions": [],
    "Description": "Updates the configuration parameters for the specified Lambda function by using the values provided in the request.",
    "Reference": "https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateFunctionConfiguration.html"
  },
  "s3:AbortMultipartUpload": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "Aborts a multipart upload.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html"
  },
  "s3:BypassGovernanceRetention": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:object-lock-legal-hold",
      "s3:object-lock-remaining-retention-days",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:x-amz-grant-read-acp",
      "s3:x-amz-grant-read",
      "s3:x-amz-website-redirect-location",
      "s3:x-amz-copy-source",
      "s3:DataAccessPointAccount",
      "s3:RequestObjectTag/<key>",
      "s3:x-amz-metadata-directive",
      "s3:AccessPointNetworkOrigin",
      "s3:object-lock-mode",
      "s3:x-amz-storage-class",
      "s3:x-amz-content-sha256",
      "s3:x-amz-grant-full-control",
      "s3:x-amz-grant-write-acp",
      "s3:x-amz-server-side-encryption-aws-kms-key-id",
      "s3:x-amz-grant-write",
      "s3:authtype",
      "s3:signatureage",
      "s3:RequestObjectTagKeys",
      "s3:x-amz-server-side-encryption",
      "s3:object-lock-retain-until-date",
      "s3:x-amz-acl"
    ],
    "Dependent Actions": [],
    "Description": "Allows circumvention of governance-mode object retention settings",
    "Reference": ""
  },
  "s3:CreateAccessPoint": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [
      "s3:authtype",
      "s3:locationconstraint",
      "s3:AccessPointNetworkOrigin",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount",
      "s3:x-amz-acl"
    ],
    "Dependent Actions": [],
    "Description": "Creates a new access point.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html"
  },
  "s3:CreateBucket": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:x-amz-grant-read-acp",
      "s3:locationconstraint",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:x-amz-grant-full-control",
      "s3:x-amz-grant-read",
      "s3:x-amz-grant-write-acp",
      "s3:signatureversion",
      "s3:x-amz-acl",
      "s3:x-amz-grant-write"
    ],
    "Dependent Actions": [],
    "Description": "Creates a new bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html"
  },
  "s3:CreateJob": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion",
      "s3:x-amz-content-sha256",
      "s3:RequestJobPriority",
      "s3:RequestJobOperation"
    ],
    "Dependent Actions": [],
    "Description": "Creates a new Amazon S3 Batch Operations job.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html"
  },
  "s3:DeleteAccessPoint": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the access point named in the URI",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html"
  },
  "s3:DeleteAccessPointPolicy": {
    "Access": "Permissions Management",
    "Affects": [],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "Delete the policy on a specified access point",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html"
  },
  "s3:DeleteBucket": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Deletes the bucket named in the URI",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html"
  },
  "s3:DeleteBucketPolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Delete the policy on a specified bucket",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html"
  },
  "s3:DeleteBucketWebsite": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Removes the website configuration for a bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketWebsite.html"
  },
  "s3:DeleteObject": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "Removes the null version (if there is one) of an object and inserts a delete marker, which becomes the current version of the object.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html"
  },
  "s3:DeleteObjectTagging": {
    "Access": "Tagging",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:ExistingObjectTag/<key>",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "This implementation of the DELETE operation uses the tagging subresource to remove the entire tag set from the specified object.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html"
  },
  "s3:DeleteObjectVersion": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:versionid",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "To remove a specific version of a object, you must be the bucket owner and you must use the versionId subresource.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html"
  },
  "s3:DeleteObjectVersionTagging": {
    "Access": "Tagging",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:versionid",
      "s3:ExistingObjectTag/<key>",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "DELETE Object tagging (for a Specific Version of the Object)",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html"
  },
  "s3:DescribeJob": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Job"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Retrieves the configuration parameters and status for an Amazon S3 batch operations job.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html"
  },
  "s3:GetAccelerateConfiguration": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "This implementation of the GET operation uses the accelerate subresource to return the Transfer Acceleration state of a bucket, which is either Enabled or Suspended.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAccelerateConfiguration.html"
  },
  "s3:GetAccessPoint": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [
      "s3:DataAccessPointAccount",
      "s3:DataAccessPointArn",
      "s3:AccessPointNetworkOrigin",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion",
      "s3:x-amz-content-sha256"
    ],
    "Dependent Actions": [],
    "Description": "Retrieve access point metadata",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html"
  },
  "s3:GetAccessPointPolicy": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "Return the policy of a specified access point.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html"
  },
  "s3:GetAccessPointPolicyStatus": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "Retrieve the policy status for an specific access point's policy",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyStatus.html"
  },
  "s3:GetAccountPublicAccessBlock": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion",
      "s3:x-amz-content-sha256"
    ],
    "Dependent Actions": [],
    "Description": "Retrieve the PublicAccessBlock configuration for an AWS account",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetPublicAccessBlock.html"
  },
  "s3:GetAnalyticsConfiguration": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "This implementation of the GET operation returns an analytics configuration (identified by the analytics configuration ID) from the bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAnalyticsConfiguration.html"
  },
  "s3:GetBucketAcl": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Return the access control list (ACL) of a bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAcl.html"
  },
  "s3:GetBucketCORS": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Returns the CORS configuration information set for the bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketCors.html"
  },
  "s3:GetBucketLocation": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Return a bucket's region.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLocation.html"
  },
  "s3:GetBucketLogging": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Return the logging status of a bucket and the permissions users have to view and modify that status.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLogging.html"
  },
  "s3:GetBucketNotification": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Return the notification configuration of a bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotification.html"
  },
  "s3:GetBucketObjectLockConfiguration": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "GET Object Lock configuration for a specific bucket",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLockConfiguration.html"
  },
  "s3:GetBucketPolicy": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Return the policy of a specified bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html"
  },
  "s3:GetBucketPolicyStatus": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Retrieve the policy status for an specific S3 bucket, indicating whether the bucket is public.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicyStatus.html"
  },
  "s3:GetBucketPublicAccessBlock": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Retrieve the PublicAccessBlock configuration for a specific S3 bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html"
  },
  "s3:GetBucketRequestPayment": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Return the request payment configuration of a bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketRequestPayment.html"
  },
  "s3:GetBucketTagging": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Return the tag set associated with the bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html"
  },
  "s3:GetBucketVersioning": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Return the versioning state of a bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html"
  },
  "s3:GetBucketWebsite": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Returns the website configuration associated with a bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketWebsite.html"
  },
  "s3:GetEncryptionConfiguration": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Returns the encryption configuration information set on the bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html"
  },
  "s3:GetInventoryConfiguration": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "This implementation of the GET operation returns an inventory configuration (identified by the inventory configuration ID) from the bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketInventoryConfiguration.html"
  },
  "s3:GetLifecycleConfiguration": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Returns the lifecycle configuration information set on the bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html"
  },
  "s3:GetMetricsConfiguration": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Gets a metrics configuration for the CloudWatch request metrics (specified by the metrics configuration ID) from the bucket. Note that this doesn't include the daily storage metrics.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetricsConfiguration.html"
  },
  "s3:GetObject": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:ExistingObjectTag/<key>",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "Retrieves objects from Amazon S3.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html"
  },
  "s3:GetObjectAcl": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:ExistingObjectTag/<key>",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "Return the access control list (ACL) of an object.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html"
  },
  "s3:GetObjectLegalHold": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "GET Object Legal Hold for a specific object",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLegalHold.html"
  },
  "s3:GetObjectRetention": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "GET Object Legal Hold for a specific object",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectRetention.html"
  },
  "s3:GetObjectTagging": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:ExistingObjectTag/<key>",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "This implementation of the GET operation returns the tags associated with an object. You send the GET request against the tagging subresource associated with the object.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html"
  },
  "s3:GetObjectTorrent": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "return torrent files from a bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTorrent.html"
  },
  "s3:GetObjectVersion": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:versionid",
      "s3:ExistingObjectTag/<key>",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "To return a different version, use the versionId subresource.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html"
  },
  "s3:GetObjectVersionAcl": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:versionid",
      "s3:ExistingObjectTag/<key>",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "To return ACL information about a different version, use the versionId subresource.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html"
  },
  "s3:GetObjectVersionForReplication": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Permission exercised by S3 replication",
    "Reference": ""
  },
  "s3:GetObjectVersionTagging": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:versionid",
      "s3:ExistingObjectTag/<key>",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "GET Object tagging (for a Specific Version of the Object)",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html"
  },
  "s3:GetObjectVersionTorrent": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:versionid",
      "s3:x-amz-content-sha256",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "To return Torrent files about a different version, use the versionId subresource.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTorrent.html"
  },
  "s3:GetReplicationConfiguration": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Returns the replication configuration information set on the bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketReplication.html"
  },
  "s3:ListAccessPoints": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion",
      "s3:x-amz-content-sha256"
    ],
    "Dependent Actions": [],
    "Description": "Lists access points.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html"
  },
  "s3:ListAllMyBuckets": {
    "Access": "List",
    "Affects": [],
    "Condition Keys": [
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion",
      "s3:x-amz-content-sha256"
    ],
    "Dependent Actions": [],
    "Description": "Returns a list of all buckets owned by the authenticated sender of the request.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html"
  },
  "s3:ListBucket": {
    "Access": "List",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:max-keys",
      "s3:AccessPointNetworkOrigin",
      "s3:delimiter",
      "s3:signatureage",
      "s3:prefix",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "Returns some or all (up to 1000) of the objects in a bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html"
  },
  "s3:ListBucketMultipartUploads": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "Lists in-progress multipart uploads.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html"
  },
  "s3:ListBucketVersions": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:max-keys",
      "s3:AccessPointNetworkOrigin",
      "s3:delimiter",
      "s3:signatureage",
      "s3:prefix",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "Use the versions subresource to list metadata about all of the versions of objects in a bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html"
  },
  "s3:ListJobs": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion",
      "s3:x-amz-content-sha256"
    ],
    "Dependent Actions": [],
    "Description": "Lists current jobs and jobs that have ended recently.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html"
  },
  "s3:ListMultipartUploadParts": {
    "Access": "Read",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "Lists the parts that have been uploaded for a specific multipart upload.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html"
  },
  "s3:ObjectOwnerOverrideToBucketOwner": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Permission exercised by S3 replication",
    "Reference": ""
  },
  "s3:PutAccelerateConfiguration": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "This implementation of the PUT operation uses the accelerate subresource to set the Transfer Acceleration state of an existing bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAccelerateConfiguration.html"
  },
  "s3:PutAccessPointPolicy": {
    "Access": "Permissions Management",
    "Affects": [],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "Add to or replace a data policy on a access point.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html"
  },
  "s3:PutAccountPublicAccessBlock": {
    "Access": "Permissions Management",
    "Affects": [],
    "Condition Keys": [
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion",
      "s3:x-amz-content-sha256"
    ],
    "Dependent Actions": [],
    "Description": "Create or modify the PublicAccessBlock configuration for an AWS account.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutPublicAccessBlock.html"
  },
  "s3:PutAnalyticsConfiguration": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "This implementation of the PUT operation adds an analytics configuration (identified by the analytics ID) to the bucket. You can have up to 1,000 analytics configurations per bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAnalyticsConfiguration.html"
  },
  "s3:PutBucketAcl": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:x-amz-grant-read-acp",
      "s3:x-amz-content-sha256",
      "s3:signatureage",
      "s3:x-amz-grant-full-control",
      "s3:x-amz-grant-read",
      "s3:x-amz-grant-write-acp",
      "s3:signatureversion",
      "s3:x-amz-acl",
      "s3:x-amz-grant-write"
    ],
    "Dependent Actions": [],
    "Description": "Set the permissions on an existing bucket using access control lists (ACL).",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAcl.html"
  },
  "s3:PutBucketCORS": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Sets the CORS configuration for your bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketCors.html"
  },
  "s3:PutBucketLogging": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Set the logging parameters for a bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLogging.html"
  },
  "s3:PutBucketNotification": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Enables you to receive notifications when certain events happen in your bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotification.html"
  },
  "s3:PutBucketObjectLockConfiguration": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "PUT Object Lock configuration on a specific bucket",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLockConfiguration.html"
  },
  "s3:PutBucketPolicy": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Add to or replace a policy on a bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html"
  },
  "s3:PutBucketPublicAccessBlock": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Create or modify the PublicAccessBlock configuration for an specific S3 bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html"
  },
  "s3:PutBucketRequestPayment": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Set the request payment configuration of a bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketRequestPayment.html"
  },
  "s3:PutBucketTagging": {
    "Access": "Tagging",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Add a set of tags to an existing bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html"
  },
  "s3:PutBucketVersioning": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Set the versioning state of an existing bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html"
  },
  "s3:PutBucketWebsite": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Sets the configuration of the website that is specified in the website subresource.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketWebsite.html"
  },
  "s3:PutEncryptionConfiguration": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Sets the encryption configuration for the bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html"
  },
  "s3:PutInventoryConfiguration": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "This implementation of the PUT operation adds an inventory configuration (identified by the inventory ID) to the bucket. You can have up to 1,000 inventory configurations per bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketInventoryConfiguration.html"
  },
  "s3:PutLifecycleConfiguration": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Creates a new lifecycle configuration for the bucket or replaces an existing lifecycle configuration.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html"
  },
  "s3:PutMetricsConfiguration": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Sets or updates a metrics configuration for the CloudWatch request metrics (specified by the metrics configuration ID) from the bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketMetricsConfiguration.html"
  },
  "s3:PutObject": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:object-lock-legal-hold",
      "s3:object-lock-remaining-retention-days",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:x-amz-grant-read-acp",
      "s3:x-amz-grant-read",
      "s3:x-amz-website-redirect-location",
      "s3:x-amz-copy-source",
      "s3:DataAccessPointAccount",
      "s3:RequestObjectTag/<key>",
      "s3:x-amz-metadata-directive",
      "s3:AccessPointNetworkOrigin",
      "s3:object-lock-mode",
      "s3:x-amz-storage-class",
      "s3:x-amz-content-sha256",
      "s3:x-amz-grant-full-control",
      "s3:x-amz-grant-write-acp",
      "s3:x-amz-server-side-encryption-aws-kms-key-id",
      "s3:x-amz-grant-write",
      "s3:authtype",
      "s3:signatureage",
      "s3:RequestObjectTagKeys",
      "s3:x-amz-server-side-encryption",
      "s3:object-lock-retain-until-date",
      "s3:x-amz-acl"
    ],
    "Dependent Actions": [],
    "Description": "Adds an object to a bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html"
  },
  "s3:PutObjectAcl": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:x-amz-grant-read-acp",
      "s3:AccessPointNetworkOrigin",
      "s3:x-amz-storage-class",
      "s3:ExistingObjectTag/<key>",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:x-amz-grant-full-control",
      "s3:DataAccessPointArn",
      "s3:x-amz-grant-read",
      "s3:x-amz-grant-write-acp",
      "s3:signatureversion",
      "s3:DataAccessPointAccount",
      "s3:x-amz-acl",
      "s3:x-amz-grant-write"
    ],
    "Dependent Actions": [],
    "Description": "Set the access control list (ACL) permissions for an object that already exists in a bucket.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html"
  },
  "s3:PutObjectLegalHold": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:object-lock-legal-hold",
      "s3:AccessPointNetworkOrigin",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "PUT Object Legal Hold on a specific object",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLegalHold.html"
  },
  "s3:PutObjectRetention": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:object-lock-remaining-retention-days",
      "s3:object-lock-mode",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:object-lock-retain-until-date",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "PUT Object Retention on a specific object",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectRetention.html"
  },
  "s3:PutObjectTagging": {
    "Access": "Tagging",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:RequestObjectTag/<key>",
      "s3:AccessPointNetworkOrigin",
      "s3:ExistingObjectTag/<key>",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:RequestObjectTagKeys",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "This implementation of the PUT operation uses the tagging subresource to add a set of tags to an existing object.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html"
  },
  "s3:PutObjectVersionAcl": {
    "Access": "Permissions Management",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:x-amz-grant-read-acp",
      "s3:AccessPointNetworkOrigin",
      "s3:versionid",
      "s3:x-amz-storage-class",
      "s3:ExistingObjectTag/<key>",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:x-amz-grant-full-control",
      "s3:DataAccessPointArn",
      "s3:x-amz-grant-read",
      "s3:x-amz-grant-write-acp",
      "s3:signatureversion",
      "s3:DataAccessPointAccount",
      "s3:x-amz-acl",
      "s3:x-amz-grant-write"
    ],
    "Dependent Actions": [],
    "Description": "The ACL of an object is set at the object version level.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html"
  },
  "s3:PutObjectVersionTagging": {
    "Access": "Tagging",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:RequestObjectTag/<key>",
      "s3:AccessPointNetworkOrigin",
      "s3:versionid",
      "s3:ExistingObjectTag/<key>",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:RequestObjectTagKeys",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "PUT Object tagging (for a Specific Version of the Object)",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html"
  },
  "s3:PutReplicationConfiguration": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Bucket"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "In a versioning-enabled bucket, this operation creates a new replication configuration (or replaces an existing one, if present).",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketReplication.html"
  },
  "s3:ReplicateDelete": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Permission exercised by S3 replication",
    "Reference": ""
  },
  "s3:ReplicateObject": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:x-amz-content-sha256",
      "s3:signatureage",
      "s3:x-amz-server-side-encryption",
      "s3:signatureversion",
      "s3:x-amz-server-side-encryption-aws-kms-key-id"
    ],
    "Dependent Actions": [],
    "Description": "Permission exercised by S3 replication",
    "Reference": ""
  },
  "s3:ReplicateTags": {
    "Access": "Tagging",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:x-amz-content-sha256",
      "s3:authtype",
      "s3:signatureage",
      "s3:signatureversion"
    ],
    "Dependent Actions": [],
    "Description": "Permission exercised by S3 replication",
    "Reference": ""
  },
  "s3:RestoreObject": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Object"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:AccessPointNetworkOrigin",
      "s3:signatureage",
      "s3:x-amz-content-sha256",
      "s3:DataAccessPointArn",
      "s3:signatureversion",
      "s3:DataAccessPointAccount"
    ],
    "Dependent Actions": [],
    "Description": "Restores a temporary copy of an archived object.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html"
  },
  "s3:UpdateJobPriority": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Job"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:RequestJobPriority",
      "s3:ExistingJobPriority",
      "s3:x-amz-content-sha256",
      "s3:signatureage",
      "s3:signatureversion",
      "s3:ExistingJobOperation"
    ],
    "Dependent Actions": [],
    "Description": "Updates an existing job's priority.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html"
  },
  "s3:UpdateJobStatus": {
    "Access": "Write",
    "Affects": [
      "AWS::S3::Job"
    ],
    "Condition Keys": [
      "s3:authtype",
      "s3:ExistingJobPriority",
      "s3:x-amz-content-sha256",
      "s3:signatureage",
      "s3:JobSuspendedCause",
      "s3:signatureversion",
      "s3:ExistingJobOperation"
    ],
    "Dependent Actions": [],
    "Description": "Updates the status for the specified job.",
    "Reference": "https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html"
  },
  "sts:AssumeRole": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [
      "sts:TransitiveTagKeys",
      "aws:PrincipalTag/${TagKey}",
      "aws:RequestTag/${TagKey}",
      "aws:TagKeys"
    ],
    "Dependent Actions": [],
    "Description": "Returns a set of temporary security credentials that you can use to access AWS resources that you might not normally have access to",
    "Reference": "https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html"
  },
  "sts:AssumeRoleWithSAML": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [
      "sts:TransitiveTagKeys",
      "saml:sub",
      "aws:PrincipalTag/${TagKey}",
      "saml:eduorgsuperioruri",
      "saml:surname",
      "saml:primaryGroupSID",
      "saml:givenName",
      "saml:x500UniqueIdentifier",
      "saml:edupersonassurance",
      "saml:eduorgwhitepagesuri",
      "saml:eduorgidentityauthnpolicyuri",
      "saml:edupersonscopedaffiliation",
      "saml:mail",
      "saml:cn",
      "saml:sub_type",
      "saml:iss",
      "saml:aud",
      "saml:name",
      "saml:edupersonprimaryaffiliation",
      "saml:edupersontargetedid",
      "saml:edupersonorgunitdn",
      "aws:TagKeys",
      "saml:edupersonaffiliation",
      "saml:commonName",
      "saml:edupersonprimaryorgunitdn",
      "saml:edupersonprincipalname",
      "saml:edupersonnickname",
      "saml:edupersonentitlement",
      "saml:organizationStatus",
      "saml:eduorghomepageuri",
      "aws:RequestTag/${TagKey}",
      "saml:uid",
      "saml:edupersonorgdn",
      "saml:eduorglegalname",
      "saml:doc",
      "saml:namequalifier"
    ],
    "Dependent Actions": [],
    "Description": "Returns a set of temporary security credentials for users who have been authenticated via a SAML authentication response",
    "Reference": "https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html"
  },
  "sts:AssumeRoleWithWebIdentity": {
    "Access": "Write",
    "Affects": [
      "AWS::Iam::Role"
    ],
    "Condition Keys": [
      "sts:TransitiveTagKeys",
      "accounts.google.com:sub",
      "cognito-identity.amazonaws.com:aud",
      "www.amazon.com:user_id",
      "www.amazon.com:app_id",
      "cognito-identity.amazonaws.com:amr",
      "graph.facebook.com:id",
      "aws:TagKeys",
      "graph.facebook.com:app_id",
      "cognito-identity.amazonaws.com:sub",
      "aws:RequestTag/${TagKey}",
      "accounts.google.com:aud",
      "aws:PrincipalTag/${TagKey}",
      "accounts.google.com:oaud"
    ],
    "Dependent Actions": [],
    "Description": "Returns a set of temporary security credentials for users who have been authenticated in a mobile or web application with a web identity provider",
    "Reference": "https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html"
  },
  "sts:DecodeAuthorizationMessage": {
    "Access": "Write",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Decodes additional information about the authorization status of a request from an encoded message returned in response to an AWS request",
    "Reference": "https://docs.aws.amazon.com/STS/latest/APIReference/API_DecodeAuthorizationMessage.html"
  },
  "sts:GetAccessKeyInfo": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Returns details about the access key id passed as a parameter to the request.",
    "Reference": "https://docs.aws.amazon.com/STS/latest/APIReference/API_GetAccessKeyInfo.html"
  },
  "sts:GetCallerIdentity": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Returns details about the IAM identity whose credentials are used to call the API",
    "Reference": "https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html"
  },
  "sts:GetFederationToken": {
    "Access": "Read",
    "Affects": [
      "AWS::Iam::User"
    ],
    "Condition Keys": [
      "aws:PrincipalTag/${TagKey}",
      "aws:RequestTag/${TagKey}",
      "aws:TagKeys"
    ],
    "Dependent Actions": [],
    "Description": "Returns a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token) for a federated user",
    "Reference": "https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html"
  },
  "sts:GetSessionToken": {
    "Access": "Read",
    "Affects": [],
    "Condition Keys": [],
    "Dependent Actions": [],
    "Description": "Returns a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token) for an AWS account or IAM user",
    "Reference": "https://docs.aws.amazon.com/STS/latest/APIReference/API_GetSessionToken.html"
  },
  "sts:TagSession": {
    "Access": "Tagging",
    "Affects": [
      "AWS::Iam::Role",
      "AWS::Iam::User"
    ],
    "Condition Keys": [
      "sts:TransitiveTagKeys",
      "aws:PrincipalTag/${TagKey}",
      "aws:RequestTag/${TagKey}",
      "aws:TagKeys"
    ],
    "Dependent Actions": [],
    "Description": "Grants permission to add tags to a STS session",
    "Reference": ""
  }
}
