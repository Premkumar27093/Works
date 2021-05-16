train_fare= int(input())
train_dur= int(input())
bus_fare= int(input())
bus_dur= int(input())
flig_fare= int(input())
flig_dur= int(input())
tot_fare= int(input())
tot_dur= int(input())
weigt_train =((train_fare*tot_fare) +(train_dur*tot_dur))
weigt_bus=((bus_fare*tot_fare) +(bus_dur*tot_dur))
weigt_flig=((flig_fare*tot_fare) +(flig_dur*tot_dur))
a=[weigt_bus,weigt_train,weigt_flig]
if min(a) == weigt_flig:
    print("Flight Transportation")
elif min(a)==weigt_train:
    print("Train Transportation")
elif min(a)==weigt_bus:
    print("Bus Transportation")