from cisco_gnmi import ClientBuilder , proto



target = '10.10.201.91:50051'

client = (
    ClientBuilder(target)
    .set_os('NX-OS')
    .set_secure_from_file('./certs/self_sign2048.pem')
    .set_ssl_target_override()
    .set_call_authentication('studen', '1234QWer')
    .construct()
)


#####   Capabilities     ###################

cap_response = client.capabilities()
print(cap_response)

