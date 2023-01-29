#GENERATE A PASSWORD WHICH MEETS THE FOLLOWING 
#1> PASSWORD LENGTH - 10
#2> MUST CONTAIN 2 UPPERCASE AND 1 DIGIT AND 1 SPECIAL CHARACTER
import random
u = [chr(i) for i in list(range(65,91))]
l = [chr(i) for i in list(range(97,122))]
d = list(range(0,10))
sp = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=',']','[','{','}',';',':','<','>','/','?','.',',','"','\\','|']
la = random.sample(u,2) + [f'{random.choice(d)}'] + [f'{random.choice(sp)}'] + random.sample(l,6)
print(''.join(la))