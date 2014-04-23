#Auther Pei-Chen Tsai AKA Hammer
#please call this script for all Mercurial addtional information

echo start minging data...
if [ "$1" == "" ];then
CMD="hg clone https://workthethird@code.google.com/p/hgplus/"
else
CMD="hg clone "$1
fi

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
hg log | python ../HGPlusMore.py
cd ..
rm -Rf $tFolder
