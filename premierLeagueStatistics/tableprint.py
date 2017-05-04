dlist = {'Man Utd': ['23', '56'], 'Chelsea': ['23', '69'],'Arsenal':['23', '56'],'Swansea': ['22', '52'],'West Ham Utd': ['23', '79'],'Liverpool': ['22', '54']}

#dlist = {'West Bromwich ALbion':['23','56']}


print ('| Football Club        | Games played | Points |')
print '------------------------------------------'

#for item in nestedlist:
	#print '+ '+item[0]+' '*(13-len(item[0]))+' + '+item[1]+' '*(13-len(item[1]))+'+ '+item[2]+' '*(6-len(item[2]))+' +'

for name in dlist:
    item = dlist[name]
    print '| '+name+' '*(20-len(name))+' | '+item[0]+' '*(13-len(item[0]))+'| '+item[1]+' '*(6-len(item[1]))+' |'
