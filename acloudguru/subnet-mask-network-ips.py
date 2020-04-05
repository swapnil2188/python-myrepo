#!/usr/bin/python

print ("\nScript to Calculate Host IPs based on Subnet_mask\n")

network_ips = []
subnet_mask = []
k = 2

for i in range(29, 15, -1):
	j = 32 - i
	ips = k ** j
	network_ips.append(ips)
 	subnet_mask.append(i)

#Using zip to zip two lists and print together

for (s, n) in zip(subnet_mask, network_ips):
	print ("subnet_mask = " + str(s) + " network_ips " + str(n))
