import logging
import stun
import socket



STUN_SERVERS = (
    'stun.l.google.com',
    'stun.voxgratia.org',
    'stun.ekiga.net',
    'stun.ideasip.com',
    'stun.voipbuster.com'
)


stun_servers_list = STUN_SERVERS


DEFAULTS = {
    'stun_port': 3478,
    'source_ip': '0.0.0.0',
    'source_port': 54320


}


# stun attributes




# getting NAT type
def get_nat_type():






# getting IP info
def get_ip_info(source_ip='0.0.0.0', source_port=54320, \
                stun_host=None, stun_port=3478):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(2)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((source_ip, source_port))
    nat_type, nat = get_nat_type(s, source_ip, source_port, \
                                 stun_host=stun_host, stun_port=stun_port)


