#!/usr/bin/env python3
#!
# pet_club.py
# Generates a xml file which is a database for members of a pet club.
# Names, date of birth, and pets, etc. are randomly generated.
# To generate quotes needs corporate_ipsum modules from Lawrence:
# https://github.com/ldo/corporate_ipsum
# Add if __name__ == "__main__": after the mainline comment #Mainline
#
# ===
# Using BaseX to convert xml file to a database in a folder:
#
# $ basex -V -c 'CREATE DB pet_club /home/ian/BaseXData/pet_club.xml;'
# Database 'pet_club' created in 684.46 ms.
#ian@X200:~$ cd BaseXData/
#ian@X200:~/BaseXData$ ls -l pet_club.xml
#-rw-rw-r-- 1 ian ian 897 Jan 21 22:44 pet_club.xml
#ian@X200:~/BaseXData$ ls -l pet_club/
#total 28
#-rw-rw-r-- 1 ian ian    0 Jan 21 23:05 atv.basex
#-rw-rw-r-- 1 ian ian    4 Jan 21 23:05 atvl.basex
#-rw-rw-r-- 1 ian ian    0 Jan 21 23:05 atvr.basex
#-rw-rw-r-- 1 ian ian 1448 Jan 21 23:05 inf.basex
#-rw-rw-r-- 1 ian ian 4096 Jan 21 23:05 tbl.basex
#-rw-rw-r-- 1 ian ian    6 Jan 21 23:05 tbli.basex
#-rw-rw-r-- 1 ian ian  141 Jan 21 23:05 txt.basex
#-rw-rw-r-- 1 ian ian   56 Jan 21 23:05 txtl.basex
#-rw-rw-r-- 1 ian ian  120 Jan 21 23:05 txtr.basex

# Access xml file
# $ basex -V -i /home/ian/BaseXData/pet_club.xml "data(//member_id)"
# Access the basex database for pet_club
# $ basex -V -i /home/ian/BaseXData/pet_club/pet_club "data(//member_id)"

# $basex -c 'OPEN pet_club; EXPORT /home/ian/BaseXData/pet_club_1'
# $ ls -l pet_club_1/pet_club.xml
#-rw-rw-r-- 1 ian ian 857 Jan 21 23:20 pet_club_1/pet_club.xml
# 897 - 857 = 42 shorter - missing <?xml version="1.0" encoding="UTF-8"?>
#
# $ basex -i /home/ian/BaseXData/pet_club/pet_club "data(//member)"
# 4FieldsRussellS.male1985-06-13hampsterblackCredibly productivate agile fungibility.
# 3CastroEdwardK.male1974-07-20catwhiteProactively drive technically sound benefits.
# 2PenaJeanZ.male1979-02-06catblackHolisticly strategize front-end quality vectors.
# 1HopkinsCalebB.male1979-09-12hampsterblackInteractively generate effective processes.
#
import random
import sys
import time
import os

is_quote = True
try:
    import corporate_ipsum
except:
    print("corporate_ipsum module not present. Unable to generate quotes")
    print("Module may be copied from: https://github.com/ldo/corporate_ipsum")
    print("Add: if __name__ == '__main__': after the comment '#Mainline'")
    is_quote = False


total_member = 4
file_name = 'pet_club'
file_extension = '.xml'

surname = [
'Abbott', 'Adams', 'Adkins', 'Aguilar', 'Alexander', 'Allen', 'Allison', 
'Alvarado', 'Alvarez', 'Anderson', 'Andrews', 'Armstrong', 'Arnold', 'Atkins', 
'Austin', 'Bailey', 'Baker', 'Baldwin', 'Ball', 'Ballard', 'Banks', 
'Barber', 'Barker', 'Barnes', 'Barnett', 'Barrett', 'Barton', 'Bass', 
'Bates', 'Beck', 'Becker', 'Bell', 'Bennett', 'Benson', 'Berry', 
'Bishop', 'Black', 'Blair', 'Blake', 'Boone', 'Bowen', 'Bowers', 
'Bowman', 'Boyd', 'Bradley', 'Brady', 'Brewer', 'Bridges', 'Briggs', 
'Brock', 'Brooks', 'Brown', 'Bryan', 'Bryant', 'Buchanan', 'Burgess', 
'Burke', 'Burns', 'Burton', 'Bush', 'Butler', 'Byrd', 'Cain', 
'Caldwell', 'Campbell', 'Cannon', 'Carlson', 'Carpenter', 'Carr', 'Carroll', 
'Carson', 'Carter', 'Casey', 'Castillo', 'Castro', 'Chambers', 'Chandler', 
'Chapman', 'Chavez', 'Christensen', 'Clark', 'Clarke', 'Clayton', 'Cobb', 
'Cohen', 'Cole', 'Coleman', 'Collier', 'Collins', 'Colon', 'Conner', 
'Cook', 'Cooper', 'Copeland', 'Cortez', 'Cox', 'Craig', 'Crawford', 
'Cross', 'Cruz', 'Cummings', 'Cunningham', 'Curry', 'Curtis', 'Daniel', 
'Daniels', 'Davidson', 'Davis', 'Dawson', 'Day', 'Dean', 'Delgado', 
'Dennis', 'Diaz', 'Dixon', 'Douglas', 'Doyle', 'Drake', 'Duncan', 
'Dunn', 'Edwards', 'Elliott', 'Ellis', 'Erickson', 'Estrada', 'Evans', 
'Farmer', 'Ferguson', 'Fernandez', 'Fields', 'Figueroa', 'Fisher', 'Fitzgerald', 
'Fleming', 'Fletcher', 'Flores', 'Flowers', 'Floyd', 'Ford', 'Foster', 
'Fowler', 'Fox', 'Francis', 'Frank', 'Franklin', 'Frazier', 'Freeman', 
'French', 'Fuller', 'Garcia', 'Gardner', 'Garner', 'Garrett', 'Garza', 
'George', 'Gibbs', 'Gibson', 'Gilbert', 'Gill', 'Glover', 'Gomez', 
'Gonzales', 'Gonzalez', 'Goodman', 'Goodwin', 'Gordon', 'Graham', 'Grant', 
'Graves', 'Gray', 'Green', 'Greene', 'Greer', 'Gregory', 'Griffin', 
'Griffith', 'Gross', 'Guerrero', 'Gutierrez', 'Guzman', 'Hale', 'Hall', 
'Hamilton', 'Hammond', 'Hampton', 'Hansen', 'Hanson', 'Hardy', 'Harmon', 
'Harper', 'Harrington', 'Harris', 'Harrison', 'Hart', 'Harvey', 'Hawkins', 
'Hayes', 'Haynes', 'Henderson', 'Henry', 'Hernandez', 'Herrera', 'Hicks', 
'Higgins', 'Hill', 'Hines', 'Hodges', 'Hoffman', 'Hogan', 'Holland', 
'Holloway', 'Holmes', 'Holt', 'Hopkins', 'Horton', 'Houston', 'Howard', 
'Howell', 'Hubbard', 'Hudson', 'Huff', 'Hughes', 'Hunt', 'Hunter', 
'Ingram', 'Jackson', 'Jacobs', 'James', 'Jefferson', 'Jenkins', 'Jennings', 
'Jensen', 'Jimenez', 'Johnson', 'Johnston', 'Jones', 'Jordan', 'Joseph', 
'Keller', 'Kelley', 'Kelly', 'Kennedy', 'Kim', 'King', 'Klein', 
'Knight', 'Lamb', 'Lambert', 'Lane', 'Larson', 'Lawrence', 'Lawson', 
'Lee', 'Leonard', 'Lewis', 'Lindsey', 'Little', 'Lloyd', 'Logan', 
'Long', 'Lopez', 'Love', 'Lowe', 'Lucas', 'Luna', 'Lynch', 
'Lyons', 'Mack', 'Maldonado', 'Malone', 'Mann', 'Manning', 'Marsh', 
'Marshall', 'Martin', 'Martinez', 'Mason', 'Massey', 'Mathis', 'Matthews', 
'Maxwell', 'May', 'McBride', 'McCarthy', 'McCormick', 'McCoy', 'McDaniel', 
'McDonald', 'McGee', 'McGuire', 'McKenzie', 'McKinney', 'McLaughlin', 'Medina', 
'Mendez', 'Mendoza', 'Meyer', 'Miles', 'Miller', 'Mills', 'Mitchell', 
'Montgomery', 'Moody', 'Moore', 'Morales', 'Moran', 'Moreno', 'Morgan', 
'Morris', 'Morrison', 'Morton', 'Moss', 'Mullins', 'Munoz', 'Murphy', 
'Murray', 'Myers', 'Nash', 'Neal', 'Nelson', 'Newman', 'Newton', 
'Nguyen', 'Nichols', 'Norman', 'Norris', 'Norton', 'Nunez', 'Obrien', 
'Oliver', 'Olson', 'Ortega', 'Ortiz', 'Osborne', 'Owen', 'Owens', 
'Padilla', 'Page', 'Palmer', 'Park', 'Parker', 'Parks', 'Parsons', 
'Patrick', 'Patterson', 'Patton', 'Paul', 'Payne', 'Pearson', 'Pena', 
'Perez', 'Perkins', 'Perry', 'Peters', 'Peterson', 'Phelps', 'Phillips', 
'Pierce', 'Pittman', 'Poole', 'Pope', 'Porter', 'Potter', 'Powell', 
'Powers', 'Pratt', 'Price', 'Quinn', 'Ramirez', 'Ramos', 'Ramsey', 
'Ray', 'Reed', 'Reese', 'Reeves', 'Reid', 'Reyes', 'Reynolds', 
'Rhodes', 'Rice', 'Richards', 'Richardson', 'Riley', 'Rios', 'Rivera', 
'Robbins', 'Roberson', 'Roberts', 'Robertson', 'Robinson', 'Rodgers', 'Rodriguez', 
'Rodriquez', 'Rogers', 'Romero', 'Rose', 'Ross', 'Rowe', 'Roy', 
'Ruiz', 'Russell', 'Ryan', 'Salazar', 'Sanchez', 'Sanders', 'Sandoval', 
'Santiago', 'Santos', 'Saunders', 'Schmidt', 'Schneider', 'Schultz', 'Schwartz', 
'Scott', 'Sharp', 'Shaw', 'Shelton', 'Sherman', 'Silva', 'Simmons', 
'Simon', 'Simpson', 'Sims', 'Singleton', 'Smith', 'Snyder', 'Soto', 
'Sparks', 'Spencer', 'Stanley', 'Steele', 'Stephens', 'Stevens', 'Stevenson', 
'Stewart', 'Stokes', 'Stone', 'Strickland', 'Sullivan', 'Summers', 'Sutton', 
'Swanson', 'Tate', 'Taylor', 'Terry', 'Thomas', 'Thompson', 'Thornton', 
'Todd', 'Torres', 'Townsend', 'Tran', 'Tucker', 'Turner', 'Tyler', 
'Underwood', 'Valdez', 'Vargas', 'Vasquez', 'Vaughn', 'Vega', 'Wade', 
'Wagner', 'Walker', 'Wallace', 'Walsh', 'Walters', 'Walton', 'Ward', 
'Warner', 'Warren', 'Washington', 'Waters', 'Watkins', 'Watson', 'Watts', 
'Weaver', 'Webb', 'Weber', 'Webster', 'Welch', 'Wells', 'West', 
'Wheeler', 'White', 'Wilkerson', 'Wilkins', 'Williams', 'Williamson', 'Willis', 
'Wilson', 'Wise', 'Wolfe', 'Wong', 'Wood', 'Woods', 'Wright', 
'Yates', 'Young', 'Zimmerman', 
]

male = ['Aaron', 'Abel', 'Abraham', 'Adam', 'Adrian', 'Al', 'Alan', 
'Albert', 'Alberto', 'Alejandro', 'Alex', 'Alexander', 'Alfonso', 'Alfred', 
'Alfredo', 'Allan', 'Allen', 'Alonzo', 'Alton', 'Alvin', 'Amos', 
'Andre', 'Andres', 'Andrew', 'Andy', 'Angel', 'Angelo', 'Anthony', 
'Antonio', 'Archie', 'Armando', 'Arnold', 'Arthur', 'Arturo', 'Aubrey', 
'Austin', 'Barry', 'Ben', 'Benjamin', 'Bennie', 'Benny', 'Bernard', 
'Bert', 'Bill', 'Billy', 'Blake', 'Bob', 'Bobby', 'Boyd', 
'Brad', 'Bradford', 'Bradley', 'Brandon', 'Brendan', 'Brent', 'Brett', 
'Brian', 'Bruce', 'Bryan', 'Bryant', 'Byron', 'Caleb', 'Calvin', 
'Cameron', 'Carl', 'Carlos', 'Carlton', 'Carroll', 'Cary', 'Casey', 
'Cecil', 'Cedric', 'Cesar', 'Chad', 'Charles', 'Charlie', 'Chester', 
'Chris', 'Christian', 'Christopher', 'Clarence', 'Clark', 'Claude', 'Clay', 
'Clayton', 'Clifford', 'Clifton', 'Clint', 'Clinton', 'Clyde', 'Cody', 
'Colin', 'Conrad', 'Corey', 'Cornelius', 'Cory', 'Courtney', 'Craig', 
'Curtis', 'Dale', 'Dallas', 'Damon', 'Dan', 'Dana', 'Daniel', 
'Danny', 'Darin', 'Darnell', 'Darrel', 'Darrell', 'Darren', 'Darrin', 
'Darryl', 'Daryl', 'Dave', 'David', 'Dean', 'Delbert', 'Dennis', 
'Derek', 'Derrick', 'Devin', 'Dewey', 'Dexter', 'Domingo', 'Dominic', 
'Dominick', 'Don', 'Donald', 'Donnie', 'Doug', 'Douglas', 'Doyle', 
'Drew', 'Duane', 'Dustin', 'Dwayne', 'Dwight', 'Earl', 'Earnest', 
'Ed', 'Eddie', 'Edgar', 'Edmond', 'Edmund', 'Eduardo', 'Edward', 
'Edwin', 'Elbert', 'Elias', 'Elijah', 'Ellis', 'Elmer', 'Emanuel', 
'Emilio', 'Emmett', 'Enrique', 'Eric', 'Erick', 'Erik', 'Ernest', 
'Ernesto', 'Ervin', 'Eugene', 'Evan', 'Everett', 'Felipe', 'Felix', 
'Fernando', 'Floyd', 'Forrest', 'Francis', 'Francisco', 'Frank', 'Frankie', 
'Franklin', 'Fred', 'Freddie', 'Frederick', 'Fredrick', 'Gabriel', 'Garrett', 
'Garry', 'Gary', 'Gene', 'Geoffrey', 'George', 'Gerald', 'Gerard', 
'Gerardo', 'Gilbert', 'Gilberto', 'Glen', 'Glenn', 'Gordon', 'Grady', 
'Grant', 'Greg', 'Gregg', 'Gregory', 'Guadalupe', 'Guillermo', 'Gustavo', 
'Guy', 'Harold', 'Harry', 'Harvey', 'Hector', 'Henry', 'Herbert', 
'Herman', 'Homer', 'Horace', 'Howard', 'Hubert', 'Hugh', 'Hugo', 
'Ian', 'Ignacio', 'Ira', 'Irvin', 'Irving', 'Isaac', 'Ismael', 
'Israel', 'Ivan', 'Jack', 'Jackie', 'Jacob', 'Jaime', 'Jake', 
'James', 'Jamie', 'Jan', 'Jared', 'Jason', 'Javier', 'Jay', 
'Jean', 'Jeff', 'Jeffery', 'Jeffrey', 'Jerald', 'Jeremiah', 'Jeremy', 
'Jermaine', 'Jerome', 'Jerry', 'Jesse', 'Jessie', 'Jesus', 'Jim', 
'Jimmie', 'Jimmy', 'Jody', 'Joe', 'Joel', 'Joey', 'John', 
'Johnathan', 'Johnnie', 'Johnny', 'Jon', 'Jonathan', 'Jonathon', 'Jordan', 
'Jorge', 'Jose', 'Joseph', 'Josh', 'Joshua', 'Juan', 'Julian', 
'Julio', 'Julius', 'Justin', 'Karl', 'Keith', 'Kelly', 'Kelvin', 
'Ken', 'Kenneth', 'Kenny', 'Kent', 'Kerry', 'Kevin', 'Kim', 
'Kirk', 'Kristopher', 'Kurt', 'Kyle', 'Lamar', 'Lance', 'Larry', 
'Laurence', 'Lawrence', 'Lee', 'Leland', 'Leo', 'Leon', 'Leonard', 
'Leroy', 'Leslie', 'Lester', 'Levi', 'Lewis', 'Lionel', 'Lloyd', 
'Lonnie', 'Loren', 'Lorenzo', 'Louis', 'Lowell', 'Lucas', 'Luis', 
'Luke', 'Luther', 'Lyle', 'Lynn', 'Mack', 'Malcolm', 'Manuel', 
'Marc', 'Marco', 'Marcos', 'Marcus', 'Mario', 'Marion', 'Mark', 
'Marlon', 'Marshall', 'Martin', 'Marty', 'Marvin', 'Mathew', 'Matt', 
'Matthew', 'Maurice', 'Max', 'Melvin', 'Merle', 'Michael', 'Micheal', 
'Miguel', 'Mike', 'Milton', 'Mitchell', 'Morris', 'Moses', 'Myron', 
'Nathan', 'Nathaniel', 'Neal', 'Neil', 'Nelson', 'Nicholas', 'Nick', 
'Nicolas', 'Noah', 'Noel', 'Norman', 'Oliver', 'Omar', 'Orlando', 
'Orville', 'Oscar', 'Otis', 'Owen', 'Pablo', 'Pat', 'Patrick', 
'Paul', 'Pedro', 'Percy', 'Perry', 'Pete', 'Peter', 'Phil', 
'Philip', 'Phillip', 'Preston', 'Rafael', 'Ralph', 'Ramiro', 'Ramon', 
'Randal', 'Randall', 'Randolph', 'Randy', 'Raul', 'Ray', 'Raymond', 
'Reginald', 'Rene', 'Rex', 'Ricardo', 'Richard', 'Rick', 'Rickey', 
'Ricky', 'Robert', 'Roberto', 'Robin', 'Roderick', 'Rodney', 'Rodolfo', 
'Rogelio', 'Roger', 'Roland', 'Rolando', 'Roman', 'Ron', 'Ronald', 
'Ronnie', 'Roosevelt', 'Ross', 'Roy', 'Ruben', 'Rudolph', 'Rudy', 
'Rufus', 'Russell', 'Ryan', 'Salvador', 'Salvatore', 'Sam', 'Sammy', 
'Samuel', 'Santiago', 'Santos', 'Saul', 'Scott', 'Sean', 'Sergio', 
'Seth', 'Shane', 'Shannon', 'Shaun', 'Shawn', 'Sheldon', 'Sherman', 
'Sidney', 'Simon', 'Spencer', 'Stanley', 'Stephen', 'Steve', 'Steven', 
'Stewart', 'Stuart', 'Sylvester', 'Taylor', 'Ted', 'Terence', 'Terrance', 
'Terrell', 'Terrence', 'Terry', 'Theodore', 'Thomas', 'Tim', 'Timmy', 
'Timothy', 'Toby', 'Todd', 'Tom', 'Tomas', 'Tommie', 'Tommy', 
'Tony', 'Tracy', 'Travis', 'Trevor', 'Troy', 'Tyler', 'Tyrone', 
'Van', 'Vernon', 'Victor', 'Vincent', 'Virgil', 'Wade', 'Wallace', 
'Walter', 'Warren', 'Wayne', 'Wendell', 'Wesley', 'Wilbert', 'Wilbur', 
'Wilfred', 'Willard', 'William', 'Willie', 'Willis', 'Wilson', 'Winston', 
'Wm', 'Woodrow', 'Zachary',]

female = ['Ada', 'Adrienne', 'Agnes', 'Alberta', 'Alexandra', 'Alexis', 'Alice', 
'Alicia', 'Alison', 'Allison', 'Alma', 'Alyssa', 'Amanda', 'Amber', 
'Amelia', 'Amy', 'Ana', 'Andrea', 'Angel', 'Angela', 'Angelica', 
'Angelina', 'Angie', 'Anita', 'Ann', 'Anna', 'Anne', 'Annette', 
'Annie', 'Antoinette', 'Antonia', 'April', 'Arlene', 'Ashley', 'Audrey', 
'Barbara', 'Beatrice', 'Becky', 'Belinda', 'Bernadette', 'Bernice', 'Bertha', 
'Bessie', 'Beth', 'Bethany', 'Betsy', 'Betty', 'Beulah', 'Beverly', 
'Billie', 'Blanca', 'Blanche', 'Bobbie', 'Bonnie', 'Brandi', 'Brandy', 
'Brenda', 'Bridget', 'Brittany', 'Brooke', 'Camille', 'Candace', 'Candice', 
'Carla', 'Carmen', 'Carol', 'Carole', 'Caroline', 'Carolyn', 'Carrie', 
'Casey', 'Cassandra', 'Catherine', 'Cathy', 'Cecelia', 'Cecilia', 'Celia', 
'Charlene', 'Charlotte', 'Chelsea', 'Cheryl', 'Christie', 'Christina', 'Christine', 
'Christy', 'Cindy', 'Claire', 'Clara', 'Claudia', 'Colleen', 'Connie', 
'Constance', 'Cora', 'Courtney', 'Cristina', 'Crystal', 'Cynthia', 'Daisy', 
'Dana', 'Danielle', 'Darla', 'Darlene', 'Dawn', 'Deanna', 'Debbie', 
'Deborah', 'Debra', 'Delia', 'Della', 'Delores', 'Denise', 'Desiree', 
'Diana', 'Diane', 'Dianna', 'Dianne', 'Dixie', 'Dolores', 'Donna', 
'Dora', 'Doreen', 'Doris', 'Dorothy', 'Ebony', 'Edith', 'Edna', 
'Eileen', 'Elaine', 'Eleanor', 'Elena', 'Elisa', 'Elizabeth', 'Ella', 
'Ellen', 'Eloise', 'Elsa', 'Elsie', 'Elvira', 'Emily', 'Emma', 
'Erica', 'Erika', 'Erin', 'Erma', 'Ernestine', 'Essie', 'Estelle', 
'Esther', 'Ethel', 'Eula', 'Eunice', 'Eva', 'Evelyn', 'Faith', 
'Fannie', 'Faye', 'Felicia', 'Flora', 'Florence', 'Frances', 'Francis', 
'Freda', 'Gail', 'Gayle', 'Geneva', 'Genevieve', 'Georgia', 'Geraldine', 
'Gertrude', 'Gina', 'Ginger', 'Gladys', 'Glenda', 'Gloria', 'Grace', 
'Gretchen', 'Guadalupe', 'Gwen', 'Gwendolyn', 'Hannah', 'Harriet', 'Hattie', 
'Hazel', 'Heather', 'Heidi', 'Helen', 'Henrietta', 'Hilda', 'Holly', 
'Hope', 'Ida', 'Inez', 'Irene', 'Iris', 'Irma', 'Isabel', 
'Jackie', 'Jacqueline', 'Jacquelyn', 'Jaime', 'Jamie', 'Jan', 'Jana', 
'Jane', 'Janet', 'Janice', 'Janie', 'Janis', 'Jasmine', 'Jean', 
'Jeanette', 'Jeanne', 'Jeannette', 'Jeannie', 'Jenna', 'Jennie', 'Jennifer', 
'Jenny', 'Jessica', 'Jessie', 'Jill', 'Jo', 'Joan', 'Joann', 
'Joanna', 'Joanne', 'Jodi', 'Jody', 'Johanna', 'Johnnie', 'Josefina', 
'Josephine', 'Joy', 'Joyce', 'Juana', 'Juanita', 'Judith', 'Judy', 
'Julia', 'Julie', 'June', 'Kara', 'Karen', 'Kari', 'Karla', 
'Kate', 'Katherine', 'Kathleen', 'Kathryn', 'Kathy', 'Katie', 'Katrina', 
'Kay', 'Kayla', 'Kelley', 'Kelli', 'Kellie', 'Kelly', 'Kendra', 
'Kerry', 'Kim', 'Kimberly', 'Krista', 'Kristen', 'Kristi', 'Kristie', 
'Kristin', 'Kristina', 'Kristine', 'Kristy', 'Krystal', 'Lana', 'Latoya', 
'Laura', 'Lauren', 'Laurie', 'Laverne', 'Leah', 'Lee', 'Leigh', 
'Lela', 'Lena', 'Leona', 'Leslie', 'Leticia', 'Lila', 'Lillian', 
'Lillie', 'Linda', 'Lindsay', 'Lindsey', 'Lisa', 'Lois', 'Lola', 
'Lora', 'Lorena', 'Lorene', 'Loretta', 'Lori', 'Lorraine', 'Louise', 
'Lucia', 'Lucille', 'Lucy', 'Lula', 'Luz', 'Lydia', 'Lynda', 
'Lynette', 'Lynn', 'Lynne', 'Mabel', 'Mable', 'Madeline', 'Mae', 
'Maggie', 'Mamie', 'Mandy', 'Marcella', 'Marcia', 'Margaret', 'Margarita', 
'Margie', 'Marguerite', 'Maria', 'Marian', 'Marianne', 'Marie', 'Marilyn', 
'Marion', 'Marjorie', 'Marlene', 'Marsha', 'Marta', 'Martha', 'Mary', 
'Maryann', 'Mattie', 'Maureen', 'Maxine', 'May', 'Megan', 'Meghan', 
'Melanie', 'Melba', 'Melinda', 'Melissa', 'Melody', 'Mercedes', 'Meredith', 
'Michele', 'Michelle', 'Mildred', 'Mindy', 'Minnie', 'Miranda', 'Miriam', 
'Misty', 'Molly', 'Mona', 'Monica', 'Monique', 'Muriel', 'Myra', 
'Myrtle', 'Nadine', 'Nancy', 'Naomi', 'Natalie', 'Natasha', 'Nellie', 
'Nettie', 'Nichole', 'Nicole', 'Nina', 'Nora', 'Norma', 'Olga', 
'Olive', 'Olivia', 'Ollie', 'Opal', 'Ora', 'Pam', 'Pamela', 
'Pat', 'Patricia', 'Patsy', 'Patti', 'Patty', 'Paula', 'Paulette', 
'Pauline', 'Pearl', 'Peggy', 'Penny', 'Phyllis', 'Priscilla', 'Rachael', 
'Rachel', 'Ramona', 'Raquel', 'Rebecca', 'Regina', 'Renee', 'Rhonda', 
'Rita', 'Roberta', 'Robin', 'Robyn', 'Rochelle', 'Rosa', 'Rosalie', 
'Rose', 'Rosemarie', 'Rosemary', 'Rosie', 'Roxanne', 'Ruby', 'Ruth', 
'Sabrina', 'Sadie', 'Sally', 'Samantha', 'Sandra', 'Sandy', 'Sara', 
'Sarah', 'Shannon', 'Shari', 'Sharon', 'Shawna', 'Sheila', 'Shelia', 
'Shelley', 'Shelly', 'Sheri', 'Sherri', 'Sherry', 'Sheryl', 'Shirley', 
'Silvia', 'Sonia', 'Sonja', 'Sonya', 'Sophia', 'Sophie', 'Stacey', 
'Stacy', 'Stella', 'Stephanie', 'Sue', 'Susan', 'Susie', 'Suzanne', 
'Sylvia', 'Tabitha', 'Tamara', 'Tami', 'Tammy', 'Tanya', 'Tara', 
'Tasha', 'Teresa', 'Teri', 'Terri', 'Terry', 'Thelma', 'Theresa', 
'Tiffany', 'Tina', 'Toni', 'Tonya', 'Tracey', 'Traci', 'Tracy', 
'Tricia', 'Valerie', 'Vanessa', 'Velma', 'Vera', 'Verna', 'Veronica', 
'Vicki', 'Vickie', 'Vicky', 'Victoria', 'Viola', 'Violet', 'Virginia', 
'Vivian', 'Wanda', 'Wendy', 'Whitney', 'Willie', 'Wilma', 'Winifred', 
'Yolanda', 'Yvette', 'Yvonne',
]

middle = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]

pet = ['budgie','cat', 'dog', 'hampster']
pet_dict = {
'budgie' : ['green', 'yellow', 'blue'], 
'cat' : ['black', 'white', 'ginger', 'tabby'],
'dog' : ['black', 'white', 'brown', 'grey'], 
'hampster' : ['black', 'brown', 'white'],
}

def member_id_generator(total = 100):
    """
    random.sample produces a list of set length of unique integers.
    member_id's are a complete set but in random order
    """
    start_time = time.time()
    random_list = random.sample(range(1, total + 1), total)

    #print("Elapsed Time: {:.1f}".format(time.time() - start_time))
    #print("Length of random list",len(random_list))
    #print(random_list)
    #print(sorted(random_list))
    return random_list

    #Elapsed Time: 1.7
    #To create 1000000 random integer list

def date_of_birth_generator():
    """
    Generate a date of birth
    From 10 to 80 years ago
    """
    from datetime import datetime, timedelta

    year = datetime.today().year
    #print("Current year:", year)
    random_year = random.randint(year-80, year-10)

    #count = 10
    #while count != 0:
    random_year = random.randint(year-80, year-10)
    #print("Random birth year:", random_year)
    random_day_number = random.randint(1, 365)
    #print("Random day of the year:", random_day_number)
    dt = datetime(random_year, 1, 1) #, 0, 0)
    dtdelta = timedelta(days=random_day_number)
    dob = dt + dtdelta
    #print("DOB as datetime type:", dob)
    #print(type(dob)) # <class 'datetime.datetime'>
    dob_string = dob.strftime("%Y-%m-%d")
    #print("DOB as string:", dob_string)
    return dob_string

    #count -= 1

    """
    Current year: 2020
    Random birth year: 1974
    Random day of the year: 125
    DOB as datetime type: 1974-05-06 00:00:00
    DOB as string: 1974-05-06
    """
 
def quote_generator():  
    """
    Use Lawrence's coporate_ipsum program to randomly generate a quotation.
    """
    # import corporate_ipsum
    #print(dir(corporate_ipsum))
    #for i in range(4):
    return corporate_ipsum.create_ipsum(1)


def main(total = 100):
    """
    Generate an xml file that has random member information.
    """
    member_is_list = member_id_generator(total)
    start_time = time.time()
    with open(file_name + file_extension, 'w') as fout:
        s = '<?xml version="1.0" encoding="UTF-8"?>\n'
        s += '<pet_club>\n'
        for i in range(total):
            #member_id = str(i + 1)  # Used for sequencial member_id's
            member_id = str(member_is_list[i])
            random_surname = surname[random.randint(0, len(surname) - 1)]
            random_male = male[random.randint(0, len(male) - 1)]
            random_female = female[random.randint(0, len(female) - 1)]
            random_initial = middle[random.randint(0, len(middle) - 1)] + '.'
            random_pet = pet[random.randint(0, len(pet) - 1)]
            colour_list = pet_dict[random_pet] 
            random_colour = colour_list[random.randint(0, len(colour_list) - 1)] 
            random_sex = random.randint(0,1) 

            if random_sex == 0:
                random_gender = 'male'
                random_first = random_male
            else:
                random_gender = 'female'
                random_first = random_female

            random_dob = date_of_birth_generator()

            if is_quote:
                random_quote = quote_generator()

            s += '  <member>\n'
            s += '    <member_id>' + member_id + '</member_id>\n'    
            s += '    <surname>' + random_surname + '</surname>\n'
            s += '    <first>' + random_first + '</first>\n'
            s += '    <initial>' + random_initial + '</initial>\n'
            s += '    <gender>' + random_gender + '</gender>\n'
            s += '    <dob>' + random_dob + '</dob>\n'
            s += '    <pet>' + random_pet + '</pet>\n'
            s += '    <colour>' + random_colour + '</colour>\n'
            if is_quote:
                s += '    <quote>' + random_quote + '</quote>\n'
            s += '  </member>\n'

            #print(s)
            fout.write(s)
            s = ''

        s = '</pet_club>\n'
        #print(s)
        fout.write(s)

    # Append to the file a fixed length comment. E.g.
    # <!-- File Name:pet_club_8.xml Size:1827 Members:8 Duration:0.002      -->
    duration = time.time() - start_time
    # Add 100 bytes to the file size to allow for the comment to be added
    file_size = os.path.getsize(file_name + file_extension) + 100
    #print(file_size)
    # Comment is exactly 100 characters.
    comment = ("<!-- File Name:{: <25} Size:{: <10} Members:{: <10} "
               "Duration:{: <10.3f} -->\n".format(file_name + file_extension, 
                file_size, total_member, duration ))

    #print(comment)
    #print(len(comment)) # Should be 100

    with open(file_name + file_extension, 'a') as fout:
        fout.write(comment)

    print("Created:\n" + comment)

if __name__ == '__main__':
    # Allow command line input to set the number of members
    # $ python3 pet_club.py 4 <-- 4 x members in the pet club
    if len(sys.argv) > 1:
        #print(sys.argv[1])
        total_member = sys.argv[1]

        if total_member.isnumeric():
            total_member = int(total_member)
        else:
            print("Enter a numeric value for the number of members")
            sys.exit("Exiting.")

    # Append number of members to the filename
    file_name = file_name + '_' + str(total_member)

    main(total_member)

"""
Example of generating xml file with pet club having two members:

$ python3 pet_club.py 2
Created:
<!-- File Name:pet_club_2.xml            Size:751        Members:2          Duration:0.003      -->

$ cat pet_club_2.xml
<?xml version="1.0" encoding="UTF-8"?>
<pet_club>
  <member>
    <member_id>2</member_id>
    <surname>Butler</surname>
    <first>Elsa</first>
    <initial>V.</initial>
    <gender>female</gender>
    <dob>1964-03-11</dob>
    <pet>hampster</pet>
    <colour>brown</colour>
    <quote>Monotonically restore integrated materials.</quote>
  </member>
  <member>
    <member_id>1</member_id>
    <surname>Owens</surname>
    <first>Kelly</first>
    <initial>D.</initial>
    <gender>male</gender>
    <dob>1966-07-05</dob>
    <pet>cat</pet>
    <colour>tabby</colour>
    <quote>Energistically target pandemic systems.</quote>
  </member>
</pet_club>
<!-- File Name:pet_club_2.xml            Size:751        Members:2          Duration:0.003      -->
"""
