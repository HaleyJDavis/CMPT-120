#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''

class student:
    def __init__(self, name, studID, year, major, gpa):
        self.name = name
        self.studID = studID
        self.year = year
        self.major = major
        self.gpa = gpa

    def honorsCheck(self):
        if self.gpa >= 3.5:
            return True
            print("You qualify for honors")
        else:
            return False
            print("You don't qualify for honors")

    def idCheck(self):
        import random
        if self.studID == (random.randint(100000, 999999)):
            print("Winner! Student (name) gets free lunch!")
        else:
            print("Loser!")
    
def main():
    #create three students and check if they get free lunch and if they qualify for honors
    studA = student("Lily", 341957, "Sophomore", "Business", 3.4)
    studB = student("Hope", 502111, "Senior", "Art", 4.1)
    studC = student("Theo", 903816, "Junior", "History", 3.9)
    print(studA.honorsCheck(), studA.idCheck())
    print(studB.honorsCheck(), studB.idCheck())
    print(studC.honorsCheck(), studC.idCheck())

main()
