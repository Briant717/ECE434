#!/bin/sh

temp=`i2cget -y 2 0x48 0`  
temp2=$(($temp*9/5+32))
echo "Temperature 1: $temp2"

temp3=`i2cget -y 2 0x4a 0`  
temp4=$(($temp3*9/5+32))
echo "Temperature 2: $temp4"
