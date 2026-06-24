# Dictionary
Phone_book = {}
Phone_book2 = dict()

# สร้างค่าใน Dictionary

Student = {
     "Name" : "Tianphop",
     "Gender" : "Male",
     "Age" : "20",
     "Tel" : "098-980-6232"
}
#print(Student)
#print(Student["Name"])
#print(Student["Gender"])
#print(Student["Age"])
#print(Student["Tel"])

#Name_Student = Student.get("Name","Not Found")
#print(Name_Student)
#print(Student["Name"])

#Room_Number = Capacity , Equipment , Teacher
Class_Room = {
        "Room_Number" : "R205",
        "Capacity" : "30",
        "Equipment" : ["Projector", "Microphone", "Computer"],
        "Teacher" : {
            "Name" : "Sgt. Pornsupat",
            "Specialization" : "Programming",
            "Tel" : "080-808-8080"
        }
}
#print(Class_Room["Room_Number"])

Class_Room_Check = Class_Room.get("Room_Number","Not Found")
print(Class_Room_Check)
#Student["Age"] = "30"
#Student["Name"] = "Methanon"
#print(Student["Age"])
#print(Student["Name"])

# ลบค่าใน Dictionary
#del Student["Tel"]
#Remove_Value = Student.pop("Tel","Not Found")
#print(Student)
#print(Remove_Value)

Pop_Data = Student.pop("Tel","Not Found")
print(Pop_Data)