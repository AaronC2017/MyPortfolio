for arg in "$@"
do
   if test -f "$arg"
   then
   echo "$arg"
   fi

done
