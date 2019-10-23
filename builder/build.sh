#!/bin/bash

for a in badsudo1 badsudo2 ; do
	/bin/bash trouble/create_fake_sudo.sh $a
done

for b in user1 user2 user3 user4 user5 user6 user7 ; do
	/bin/bash trouble/create_base_users.sh $b
done

for c in goodsudo1 ; do
	trouble/create_sudo.sh $c
done

trouble/disable_firewall.sh

trouble/enable_guest.sh
