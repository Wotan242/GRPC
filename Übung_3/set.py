from cisco_gnmi import ClientBuilder , proto
import json



target = '<IP Nexus>:50051'

client = (
    ClientBuilder(target)
    .set_os('NX-OS')
    .set_secure_from_file('./certs/self_sign2048.pem')
    .set_ssl_target_override()
    .set_call_authentication('student', '1234QWer')
    .construct()
)



############ Set     #####################################



set_path1 = client.parse_xpath_to_gnmi_path("/Cisco-NX-OS-device:System/ipv4-items/inst-items/dom-items/Dom-list[name='default']/if-items/If-list[id='lo1']/addr-items/Addr-list/addr")



set_update1 = proto.gnmi_pb2.Update()
set_update1.path.CopyFrom(set_path1)
set_update1.val.json_val = json.dumps("<IP Loopback 1>/32").encode("utf-8")




set_result = client.set(updates=[set_update1])


print(set_result)



