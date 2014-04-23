#Auther Pei-Chen Tsai AKA Hammer
#please call this script for all Mercurial addtional information

echo start minging data...
CMD="hg clone "$1
echo $CMD
ret=$(time $CMD)
echo " "
#echo $ret

OIFS=$IFS
IFS=' '
retAry=$ret
state='FALSE'
tFolder=''

for item in $retAry
do
   #echo $item
   case $state in
      FALSE)
         ;;
      TRUE)
         tFolder=$item
         echo "target folder is:"$tFolder
         ;;         
   esac
   if [ "$item" == "directory:" ]; then
      state='TRUE'
   else
      state='FALSE'
   fi
done

IFS=$OIFS

cd $tFolder
hg status --all | python ../HGPlus.py
cd ..
rm -Rf $tFolder
