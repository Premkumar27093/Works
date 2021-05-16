x_axis = float(input())
y_axis = float(input())
if x_axis > 0 and y_axis > 0:
    print("I")
elif x_axis > 0 and y_axis < 0:
    print("IV")
elif x_axis < 0 and y_axis < 0:
    print("III")
else:
    print("II")