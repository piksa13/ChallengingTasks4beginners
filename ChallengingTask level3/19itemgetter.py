a = []

# create the table (name, age, job)
a.append(["Nick", 30, "Doctor"])
a.append(["John",  8, "Student"])
a.append(["Paul", 22, "Car Dealer"])
a.append(["Mark", 66, "Retired"])


# sort the table by age
import operator
a.sort(key=operator.itemgetter(0,1,2))
#func = operator.itemgetter(1)
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
