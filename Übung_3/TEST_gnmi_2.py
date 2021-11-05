from cisco_gnmi import ClientBuilder , proto
import json
import time


target = 'n9k1:50051'

client = (
    ClientBuilder(target)
    .set_os('NX-OS')
    .set_secure_from_file('./certs/self_sign2048.pem')
    #.set_ssl_target_override()
    .set_call_authentication('admin', '1234Qwer')
    .construct()
)


#####   Capabilities     ###################
'''
cap_response = client.capabilities()
print(cap_response)
'''
##########   Get ##########################################

'''
get_path1 = client.parse_xpath_to_gnmi_path("/openconfig-interfaces:interfaces/interface[name='eth1/49']/config")
get_path3 = client.parse_xpath_to_gnmi_path("/openconfig-interfaces:interfaces/interface[name='eth1/50']/config")
get_path2 = client.parse_xpath_to_gnmi_path("/oc-if:interfaces/interface[name='eth1/49']/state/counters/in-octets")
get_path4 = client.parse_xpath_to_gnmi_path("/Cisco-NX-OS-device:System/intf-items/lb-items/LbRtdIf-list[id='lo1']/descr")
get_path6 = client.parse_xpath_to_gnmi_path("/Cisco-NX-OS-device:System/ipv4-items/inst-items/dom-items/Dom-list[name='default']/if-items/If-list[id='lo1']/addr-items/Addr-list/addr")
get_path5 = client.parse_xpath_to_gnmi_path("/Cisco-NX-OS-device:System/ipv4-items/inst-items/dom-items/Dom-list[name='default']/if-items/If-list[id='lo0']/trafficstat-items/upktConsumed")
#get_path = client.parse_xpath_to_gnmi_path("/Cisco-NX-OS-device:System/intf-items/phys-items/PhysIf-list[id='eth1/49']/phys-items/lastErrors")
#get_path = client.parse_xpath_to_gnmi_path("/dme:sys/intf/phys-[eth1/49]")
get_path1.origin = 'openconfig'
get_path2.origin = 'openconfig'
get_path3.origin = 'openconfig'

#print(get_path)

#System/ipv4-items/inst-items/dom-items/Dom-list[name='default']/if-items/If-list[id='lo1']/addr-items/Addr-list


#get_response1 = client.get([get_path1 , get_path3, get_path4], data_type="CONFIG", encoding="JSON")
#get_response2 = client.get([get_path2], data_type="STATE", encoding="JSON")
#print(get_response1 , '\n' , get_response2)

get_response3 = client.get([get_path6], data_type="CONFIG", encoding="JSON")
print(get_response3)
'''
############ Set     #####################################

set_path1 = client.parse_xpath_to_gnmi_path("/openconfig-interfaces:interfaces/interface[name='eth1/49']/config/description")
set_path2 = client.parse_xpath_to_gnmi_path("/Cisco-NX-OS-device:System/intf-items/lb-items/LbRtdIf-list[id='lo1']/descr")
set_path3 = client.parse_xpath_to_gnmi_path("/Cisco-NX-OS-device:System/ipv4-items/inst-items/dom-items/Dom-list[name='default']/if-items/If-list[id='lo1']/addr-items/Addr-list/addr")
set_path1.origin = 'openconfig'

set_update = proto.gnmi_pb2.Update()
set_update.path.CopyFrom(set_path3)
set_update.val.json_val = json.dumps("1.2.3.4/32").encode("utf-8")
print(set_update)

#set_request = proto.gnmi_pb2.SetRequest()
#set_request.replace.append(set_update)
#print(set_request)

set_result = client.set(updates=[set_update])
#set_result = client.service.Set(set_request)

print(set_result)


#################   Subscribe      ###########################
'''
subscription_list = proto.gnmi_pb2.SubscriptionList()
subscription_list.mode = proto.gnmi_pb2.SubscriptionList.Mode.STREAM
subscription_list.encoding = proto.gnmi_pb2.Encoding.JSON

sampled_subscription = proto.gnmi_pb2.Subscription()


sub_path1 = client.parse_xpath_to_gnmi_path("/openconfig-interfaces:interfaces/interface/state/counters/in-multicast-pkts")
sub_path2 = client.parse_xpath_to_gnmi_path("/Cisco-NX-OS-device:System/ipv4-items/inst-items/dom-items/Dom-list[name='default']/if-items/If-list[id='lo0']/trafficstat-items/upktConsumed")
sub_path1.origin = 'openconfig'

print(sub_path2)
#sampled_subscription.path.CopyFrom(
 #   client.parse_xpath_to_gnmi_path("/interfaces/interface/state/counters")
#)
sampled_subscription.path.CopyFrom(sub_path2)
sampled_subscription.mode = proto.gnmi_pb2.SubscriptionMode.SAMPLE
sampled_subscription.sample_interval = 1 * int(1e9)
#sampled_subscription.suppress_redundant = False
subscription_list.subscription.append(sampled_subscription)

print([subscription_list])


for subscribe_response in client.subscribe([subscription_list]):
    print(subscribe_response)

'''
'''



sub_path = client.parse_xpath_to_gnmi_path("/Cisco-NX-OS-device:System/intf-items/phys-items/PhysIf-list[id='eth1/49']/dbgEtherStats-items/pkts")
#sub_path2 = client.parse_xpath_to_gnmi_path("/Cisco-NX-OS-device:System/ipv4-items/inst-items/dom-items/Dom-list[name='default']/if-items/If-list[id='lo0']/trafficstat-items/upktConsumed")

subscription_obj = proto.gnmi_pb2.Subscription()
subscription_obj.path.CopyFrom(sub_path)
subscription_obj.mode = proto.gnmi_pb2.SubscriptionMode.SAMPLE
subscription_obj.sample_interval = 1 * int(1e9)

subscription_list = proto.gnmi_pb2.SubscriptionList()
subscription_list.subscription.append(subscription_obj)
subscription_list.mode = proto.gnmi_pb2.SubscriptionList.Mode.STREAM
subscription_list.encoding = proto.gnmi_pb2.Encoding.JSON

subscribe_resp = client.subscribe([subscription_list])

for subs in subscribe_resp:
	print(subs)
'''
'''
subscribe_req.subscribe.CopyFrom(subscription_list)

print(subscribe_req)

def sub_req_generator():
	yield subscribe_req

subscribe_resp = client.service.Subscribe(iter(sub_req_generator))

#subscribe_resp = client.service.Subscribe(subscribe_req)

print(subscribe_resp)

#for resp in subscribe_resp:
#	print(resp)

'''
'''
sub_path = client.parse_xpath_to_gnmi_path("/Cisco-NX-OS-device:System/intf-items/phys-items/PhysIf-list[id='eth1/49']/dbgEtherStats-items/pkts")

subscription_obj = proto.gnmi_pb2.Subscription()
subscription_obj.path.CopyFrom(sub_path)
subscription_obj.mode = proto.gnmi_pb2.SubscriptionMode.ON_CHANGE
#subscription_obj.sample_interval = 1 * int(1e9)

subscription_list = proto.gnmi_pb2.SubscriptionList()
subscription_list.subscription.append(subscription_obj)
subscription_list.mode = proto.gnmi_pb2.SubscriptionList.Mode.POLL
subscription_list.encoding = proto.gnmi_pb2.Encoding.JSON

poll = proto.gnmi_pb2.Poll()

def gen():
	for i in range(1,10):
		print(i)
		time.sleep(3)
		if i == 1:
			yield subscription_list
		yield poll
gen_obj = gen()

#for g in gen_obj:
#	print(g)


#subscribe_resp = client.subscribe(gen_obj)

for subs in client.subscribe(gen_obj):
	print(subs)

client.close()
'''
