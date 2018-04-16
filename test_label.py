import os

LABEL = '/Users/lion/PycharmProjects/bl-color/labels.txt'
#LABEL = os.environ('LABEL')

label_dic = {}
label_f = open(LABEL,'rb')
lines = label_f.readlines()
for w in lines:
    w = str(w).replace('b\'',"")
    w = w.replace("\\n","")
    tmp = w.split(':')
    label_dic[tmp[0]] = tmp[1]

print(label_dic)