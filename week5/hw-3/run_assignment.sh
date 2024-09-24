#!/bin/bash

# Abhi Rangarajan uxs876

export COURSE_NAME="Unknown Course"

user_id=$1
if [[ -z "$user_id" ]]; then

  user_id="uxs876"

fi

# Call the C binary (your compiled program)
./assignment3 $user_id
