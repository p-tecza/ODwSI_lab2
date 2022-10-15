import string
from scipy.stats import entropy
from Crypto.Cipher import ARC4

def calc_probs(result):
        dict={}

        for x in result:
                if x in dict:
                        dict[x] += 1
                else:
                        dict[x] = 1

        for y in dict:
                dict[y]=dict[y]/len(result)

        return dict
                
chars = string.ascii_lowercase

lowest_ent=10

ARC4.key_size = range(3, 257)

file_chosen=2

if(file_chosen==1):
        f=open('crypto.rc4','rb')
elif(file_chosen==2):
        f=open('crypto2.rc4','rb')

data=f.read()

res=""

for a in chars:
        for b in chars:
                for c in chars:
                        key=a+b+c
                        cipher = ARC4.new(str.encode(key))
                        result=cipher.decrypt(data)
                        buffer=calc_probs(result)
                        to_list=list(buffer.values())
                        calc_ent=entropy(to_list,base=2)

                        if(calc_ent<lowest_ent):
                                lowest_ent=calc_ent
                                res=result                       

print(lowest_ent)
print(res.decode("latin-1"))

