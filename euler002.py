first_term=1
second_term = 1
next_term = 0
sum=0
while(next_term<=4000000):
       next_term=first_term+second_term
       first_term=second_term
       second_term=next_term
       if(next_term%2==0):
           sum+=next_term
print(sum)
