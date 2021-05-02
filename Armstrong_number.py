a=int(input())
number_= str(a)
length_= len(number_)
print(type(number_))
total_=0
for i in number_:
    x=int(i)
    sum_ =pow(x,length_)
    total_=total_+sum_
if total_ == a:
    print("armstrong")
else:
    print("not an armstrong")
             
