# Hackerrank - Codeagon
# Gohan and Blocks

input_msg = input()
amsg_list = list(input_msg)

count_true = 0
count_all = 0
astack = []
agen_msg = []
uniques = []

def do(stack,msg_list,gen_msg):
    if(not msg_list and not stack):
        ms = ''.join(gen_msg)
        global count_true
        global uniques
        global input_msg
        if ms == input_msg:
            count_true = count_true+1
        uniques.append(ms)
        return
    elif not stack:
        stack.append(msg_list.pop(0))
        do(list(stack),list(msg_list),list(gen_msg))
    elif not msg_list:
        gen_msg.append(stack.pop())
        do(list(stack),list(msg_list),list(gen_msg))
    else:
        m3 = list(msg_list)
        s3 = list(stack)
        g3 = list(gen_msg)
        m4 = list(msg_list)
        s4 = list(stack)
        g4 = list(gen_msg)
        g4.append(s4.pop())
        s3.append(m3.pop(0))
        do(list(s3),list(m3),list(g3))
        do(list(s4),list(m4),list(g4))
        
do(astack,amsg_list,agen_msg)

print(str(count_true)+' '+str(len(set(uniques))))
