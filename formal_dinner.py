#family_dinner.py
#Jan_21_2020
#Charlie Heyman

# Done with the help of Will Deardorff

import random


#declare list vars
kitchen = []
waiter = []
waiter_option = []
to_be_seated_option = []
kitchen_option = []
to_be_seated = []


try:
    with open('Dinner Seating - Student List 2018-19 4.csv') as student_file:
        for line in student_file:
            alist = line.split(',')
            #print(alist)
            x = slice(3)
            a = alist[x]
            #print(a)
            if a[2][:1] == 'W':
                kitchen_option.append(a)
                to_be_seated_option.append(a)              
            elif a[2] == 'Kitchen':
                waiter_option.append(a)
                to_be_seated_option.append(a)
            else:
                waiter_option.append(a)
                kitchen_option.append(a)
                to_be_seated_option.append(a)

#waiterOption contains all seated students from previous week
   
    num_student = len(to_be_seated_option)
    print ('number of students = '+ str(num_student))
    #print(student)
    #print('waiter option')
    #print(waiter_option)
    #print('kitchen option..')
    #print(kitchen_option)
   
    #randomly pick 7 kitchen students and 31 waiter students
    waiter = random.sample(waiter_option,31)
    print('number of waiters = ' + str(len(waiter)))
    print(waiter)

   
    for each in waiter:
        if each in kitchen_option:
            kitchen_option.remove(each)


    #create new staff of kicthen w/o repeats
    kitchen = random.sample(kitchen_option,7)
    print(kitchen)

    #de-insect-ing
    print('to be seated count= '+str(len(to_be_seated_option)))



    for each in waiter:
        to_be_seated_option.remove(each)
       
    for each in kitchen:
        to_be_seated_option.remove(each)

    #de-insect-ing
    print('to be seated count= '+str(len(to_be_seated_option)))

    
    #lambda defines the function that we are sorting by, third element in the array

    sort_to_be_seated  = sorted(to_be_seated_option,key=lambda x: x[2])
    #quit()    
#open csv file
    try:
        with open('FormalSeatAssignment.csv','w') as output_file:
            counter = 1
            max_table = 31
            for each_student in kitchen:
                #print(each_student + ',Kitchen',file=output_file)
                print(each_student[0] + ',' + each_student[1] + ',Kitchen',file=output_file)
            for each_student in waiter:
                scounter = str(counter)
                #print(each_student + ',' + 'W' + scounter.zfill(2),file=output_file)
                print(each_student[0] + ',' + each_student[1] + ',W' + scounter.zfill(2),file=output_file)
                counter = counter + 1
                if counter > max_table:
                    counter = 1
            for each_student in sort_to_be_seated:
                #print(each_student + ',' + str(counter),file=output_file)
                print(each_student[0] + ',' + each_student[1] + ',' + str(counter),file=output_file)
                counter = counter + 1
                if counter > max_table:
                    counter = 1
    except IOError as err:
        print('IO Error writing seat assignment file')
    finally:
        output_file.close()
       
except IOError as err:
    print('IO Error reading student file: '+str(err))
finally:
    student_file.close()
