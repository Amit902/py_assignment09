# Q1 Create a circle class and initialize it with radius. Make two methods get Area and get Circumference inside this class.

class circle:
    def __init__ (self,radius):
        self.radius=radius

    def area(self):
        self.area=(3.14*self.radius*self.radius)
        print("the area of circle is: ",str(self.area))


    def circumference(self):
        self.circumference=(2*3.14*self.radius)
        print("circumference is: ",str(self.circumference))

r=int(input("enter any radius: "))
obj1=circle(r)
obj1.area()
obj1.circumference()


#Q2 Create a Student class and initialize it with name and roll number. Make methods to :
#Display - It should display all informations of the student.

class student:
    def __init__(self, name,roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("name = %s\n roll no = %d"%(self.name,self.roll))


s1 = student("Amit raut",631621)
s1.display()
s2 = student("Aakash pradhan",6316213)
s2.display()

#Q.3- Create a Temprature class. Make two methods :
# a. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# b. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class temperature:
    def __init__(self,celsius,farenheit):
        self.celsius=celsius
        self.farenheit=farenheit

    def cel(self):
        celsius=(self.farenheit-32)*5/9
        print("The converted temperature  is : ",celsius)

    def far(self):
        farenheit=(1.8)*self.celsius+32
        print("The converted temperature is : ",farenheit)

m=int(input("enter the temperature in celsius : "))
n=int(input("enter the temperature in farenheit : "))
temp=temperature(m,n)
temp.cel()
temp.far()



#**Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to: (i). Display-Display the details.
                #(ii). Update- Update the movie details.

class movieDetails:
    def __init__(self,movie_name,artist_name,year_of_release,rating):
        self.movie_name = movie_name
        self.artist_name = artist_name
        self.year_of_release = year_of_release
        self.rating = rating

    def display(self):
        print("movie name: ",self.movie_name)
        print("artist name: ",self.artist_name)
        print("year of release: ",self.year_of_release)
        print("rating", self.rating)

    def update(self):
        self.movie_name=input("enter the movie name to update: ")
        self.artist_name=input("enter the attist name: ")
        self.year_of_release = input("enter the year of release: ")
        self.rating = input("enter the rating: ")

movdtl = movieDetails("Race-3","SalmanKhan","2018","10")
movdtl.display()
movdtl.update()
movdtl.display()

# Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.
# 1. Display expenditure and savings
# 2. Calculate total salary
# 3. Display salary

class expenditure:
    def __init__ (self,expenditure,saving):
        self.expenditure = expenditure
        self.saving = saving

    def show(self):
        print("Expenditure: ",self.expenditure)
        print("Saving: ",self.saving)

    def total_salary(self):
        salary = self.expenditure+self.saving
        print("The total salary is: ",salary)

ex = int(input("Enter expenditure: "))
s = int(input("Enter the saving: "))
sal = expenditure(ex,s)
sal.show()
sal.total_salary()