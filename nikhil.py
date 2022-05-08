print("****************************************")

total_room = int(input("Enter total Room : "))
total_seat_in_one_room = int(input("Enter total seat in one room : "))
total_column_in_one_room = int(input("Enter total column in one room : "))
total_seat_in_one_column = int(input("Enter total seat in one column : "))
total_student = int(input("Enter total student : "))
student_in_one_seat = int(input("Enter total student in one seat : "))
first_rollno = int(input("Enter first rollno of godavari : "))
first_rollno2 = int(input("Enter first rollno chandan singh: "))
print()


for room in range(total_room):
    
    if(total_student<1):
        break
    
    if(total_student<=(total_seat_in_one_room*student_in_one_seat)):
    
        print("****************************************")
        print("Total Students in Room Number ",room+1," = ",total_seat_in_one_room*student_in_one_seat)
        print("Roll Number ",first_rollno," To Roll Number ",first_rollno2+((total_student)-1)//2)
        print()
        for col in range(total_column_in_one_room):
            print("**************************")
            print("Student in column Number",col+1)
            print("**************************")
            for i in range(total_seat_in_one_column):
                for k in range(1,student_in_one_seat+1):
                    if(i%2!=0):
                        print(first_rollno,end=("     "))
                        first_rollno+=1
                    else:
                        print(first_rollno2,end=("     "))
                        first_rollno2+=1
                print()
            print()
        
        print("****************************************")
        break
    
    else:
        print("****************************************")
        print("Total Students in Room Number ",room+1," = ",total_seat_in_one_room*student_in_one_seat)
        print("Roll Number ",first_rollno," To Roll Number ",first_rollno2+((total_seat_in_one_room*student_in_one_seat)-1)//2)
        print("****************************************")
        print()
        print()
        for col in range(total_column_in_one_room):
            print("**************************")
            print("Student in column Number",col+1)
            print("**************************")
            for i in range(1,total_seat_in_one_column+1):
                for k in range(1,student_in_one_seat+1):
                    if(i%2!=0):
                        print(first_rollno,end=("     "))
                        first_rollno+=1
                    else:
                        print(first_rollno2,end=("     "))
                        first_rollno2+=1
                print()
            print()
            
        first_rollno-=total_seat_in_one_room*student_in_one_seat//student_in_one_seat
        first_rollno2-=total_seat_in_one_room*student_in_one_seat//student_in_one_seat
                
        
        total_student=total_student-(total_seat_in_one_room*student_in_one_seat)
        first_rollno+=(total_seat_in_one_room*student_in_one_seat)//student_in_one_seat
        first_rollno2+=(total_seat_in_one_room*student_in_one_seat)//student_in_one_seat
       
      
    



