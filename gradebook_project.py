last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

# Create some lists:
subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [
  ["Physics", 98],
  ["Calculus", 97], 
  ["Poetry", 85],
  ["History", 88]
]
print(gradebook)

# Add more subjects:

gradebook.append(["Computer Science", 100])
print(gradebook)
gradebook.append(["Visual Arts", 93])
print(gradebook)

gradebook[5][1] = 98
print(gradebook)

gradebook[2].remove(85)
print(gradebook)
gradebook[2].append("Pass")
print(gradebook)

# One big gradebook
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
