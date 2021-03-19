#<----- FUNCTION REVIEW---->

def repeat_stuff(stuff, num_repeats=10):
      return stuff * num_repeats

# create a variable that repeats row, three times and adds your boat
lyrics = repeat_stuff("Row ", 3) + "Your Boat. "

# create song variable that repeats lyrics 10 times because no second arguement is give and the number of repeats defaults to 10
song = repeat_stuff(lyrics)

print(song)



#<----- CALCULATE AGES ---->

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


my_age = calculate_age(2021, 1986)
dads_age = calculate_age(2021, 1948)
moms_age = calculate_age(2021, 1954)

print(
    f"My mom's age is {moms_age}, my dads_age is {dads_age} and my age is {my_age}")


#<----- PHYSICS PROBLEMS ---->


train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

# TEMPERATURE

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)


# USE THE FORCE

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force.")

def get_energy(mass, c=3*10**8):
  return mass*c

bomb_energy = get_energy(bomb_mass)
print(f"A 1 kg bomb supplies {bomb_energy} Joules.")


# DO THE WORK

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  work = force * distance
  return work

train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance} ,meters.")