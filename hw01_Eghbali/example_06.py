initial_velocity = float(input("input the intial velocity km/h: "))
final_velocity = float(input("input the final velocity km/h: "))
time = float(input("input the time passed mins: "))
time /= 60
acceleration = (final_velocity - initial_velocity)/ time
print(acceleration)