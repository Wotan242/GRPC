from cisco_gnmi import ClientBuilder , proto
import json
import time


target = '10.10.201.91:50051'

client = (
    ClientBuilder(target)
    .set_os('NX-OS')
    .set_secure_from_file('./certs/self_sign2048.pem')
    .set_ssl_target_override()
    .set_call_authentication('student', '1234QWer')
    .construct()
)




#################   Subscribe      ###########################



sub_path = client.parse_xpath_to_gnmi_path("/Cisco-NX-OS-device:System/intf-items/phys-items/PhysIf-list[id='eth1/49']/dbgEtherStats-items/pkts")

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

client.close()
