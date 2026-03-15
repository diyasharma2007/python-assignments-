student = {"name": "Diya", "age": 17, "city": "Pune"}
print("Original Dictionary:", student)
student["age"] = 18
student["city"] = "Pune"
print("After Update:", student)
student.pop("city")
print("After Removing city:", student)
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Is 'name' present?", "name" in student)
print("Length:", len(student))
