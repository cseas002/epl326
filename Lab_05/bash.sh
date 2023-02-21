!#/bin/bash

for i in {1..99999}
do
pass=`echo $i | openssl md5`
if [ $pass -eq "a86850deb2742ec3cb41518e26aa2d89" ] 
then 
echo $i
fi 
done
