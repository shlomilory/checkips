# get ip and put them in a list:
def absorbing_ips():
    ips=[]
    while True:
        ip = input("Enter an IP (as many as you want) Press enter to finish")
        if ip:
            ips.append(ip)
        else:
            break
    return ips

input_ip=absorbing_ips()

#check validity of IPs AND RETURN BOOLEAN AND THE CORRECT IPS ONLY!
def check_ip(input_ip):
    valid_ips=[]

    for ip in input_ip:
        octats = ip.split('.')
        if len(octats) == 4:
            valid_ip = True
            for octa in octats:
                if not octa.isdigit() or not 0 <= int(octa) <= 255:
                    valid_ip=False
                    break
            if valid_ip:
                valid_ips.append(ip)
                print(ip, "is" ,valid_ip)
    return valid_ips    

valid_ip = check_ip(input_ip)
print(valid_ip)