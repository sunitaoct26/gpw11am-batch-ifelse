sub1 = int(input("enter marks of sunject 1:"))
sub2 = int(input("enter marks of sunject 2:"))
sub3 = int(input("enter marks of sunject 3:"))
sub4 = int(input("enter marks of sunject 4:"))
sub5 = int(input("enter marks of sunject 5:"))
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total/5
print("total marks=", total)
print("percentage=", percentage)
if percentage >= 40:
    ptint("pass")
else:
    print("fail")                    