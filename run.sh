# run term
run=1
while [[ $run == 1 ]]
do
printf "$ "
read com
if [ "$com" == *";"* ] || [ "$com" == *"&&"* ]
then
  com="and_err"
fi


if [ "$com" == "exit" ]
then
  run=0
elif [ "$com" == "and_err" ]
then
  echo "error: logical line ends and and not allowed"
else
  eval "$com"
fi
done
