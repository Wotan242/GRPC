from cisco_gnmi import ClientBuilder , proto


target = '10.10.201.91:50051'

client = (
    ClientBuilder(target)
    .set_os('NX-OS')
    .set_secure_from_file('./certs/self_sign2048.pem')
    .set_ssl_target_override()
    .set_call_authentication('admin', '1234Qwer')
    .construct()
)



##########   Get ##########################################



get_path1 = client.parse_xpath_to_gnmi_path("/Cisco-NX-OS-device:System/ipv4-items/inst-items/dom-items/Dom-list[name='default']/if-items/If-list[id='lo1']/addr-items/Addr-list/addr")
get_path2 = client.parse_xpath_to_gnmi_path("/Cisco-NX-OS-device:System/intf-items/lb-items/LbRtdIf-list[id='lo1']/descr")

get_response = client.get([get_path1, get_path2], data_type="CONFIG", encoding="JSON")
print(get_response)


