#GENERATE RANDOM STRING OF LENGTH 5, 
# STRING MUST BE THE COMBINATION OF UPPERCASE AND LOWERCASE ONLY, NO SPECIAL CHARACTER OR DIGITS SHOULD BE USED?
import random
l = [chr(i) for i in list(range(65,91)) + list(range(97,123))]
print(''.join(random.sample(l,5)))
