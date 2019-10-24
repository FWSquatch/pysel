#!/bin/bash
FUNCTIONS=("trouble/create_base_sudo.sh 1" "trouble/create_base_users.sh 1" "trouble/create_fake_sudo.sh 1" "trouble/create_sudo.sh 1" "trouble/remove_users.sh 1")

for i in {1..10} ; do
$(shuf -n1 -e "${FUNCTIONS[@]}")
done