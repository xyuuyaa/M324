all: address

ip:
	hostname -I | awk '{print $$1}' > ip

host:
	hostname > host

address: host ip
	printf "%s@%s\n" "$$(cat host)" "$$(cat ip)" > address

clean:
	rm -f ip host address
