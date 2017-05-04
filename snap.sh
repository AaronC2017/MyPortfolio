read prev
while read curr && ! test "$curr" = "$prev" 
do
	prev="$curr"
done

echo "snap:" "$curr"
