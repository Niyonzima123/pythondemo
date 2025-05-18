# Create a empty set
s=set()

# Add elements in set
a = input("Enter first number:")
b= input("Enter first number:")
c = input("Enter first number:")
d= input("Enter first number:")
e = input("Enter first number:")
s.add(a)
s.add(b)
s.add(c)
s.add(d)
s.add(e)
s.remove(b)
print(s)
# And also we can calculate the number of element in the set usin len().
print(f"The Number of element in the sete is {len(s)}")