a = []

# create the table (name, age, job)
a.append(["Nick", 30, "Doctor"])
a.append(["John",  18, "Student"])
a.append(["John",  18, "Seller"])
a.append(["Chris", 18, "Seller"])
a.append(["Paul", 22, "Car Dealer"])
a.append(["Mark", 66, "Retired"])


# sort the table by age
import operator
a.sort(key=operator.itemgetter(1, 0, 2))

b = ['Zilla',' Jen', 'Brenda', 'Molly', 'Zoe']
b.sort()
print(b)
#func =a.append(["John",  8, "Student"]) operator.itemgetter(1)
#print(func(a))
#print(func(a[0]))
# print the table
print(a)

#sorted("This is a test string from Andrew".split(), key=str.lower)
#>>> student_tuples = [
 #       ('john', 'A', 15),
  #      ('jane', 'B', 12),
   #     ('dave', 'B', 10),]
#>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
