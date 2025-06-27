# Exercise 1: What wil the output of following code
d={"a":1,"b":2}
print(d.get("a"))  #It will Print 1
print(d.get("b"))	#It will print 2
print(d.get("c"))	#It will print None

# d.get("c") safley tries to access the c ,but it does not exists so it will return none
