# Game of thrones

got = input()
occ_table = {}
for i in got:
    if i not in occ_table:
        occ_table[i]=1
    else:
        occ_table[i]+=1
unpaired_chars=0
for i in occ_table.keys():
    if occ_table[i]%2 is 1:
        unpaired_chars+=1
if unpaired_chars > 1:
    print('NO')
else:
    print('YES')
