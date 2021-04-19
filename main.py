# -*- coding: utf-8 -*-

"""
Benson Lee
CPSC 223P-01
Apr. 14, 2021
blee71@csu.fullerton.edu
"""

import csv

def listNames():
  """Lists the names of all the students"""
  studentNameFile = open("attendance.txt", "r")
  studentNames = studentNameFile.readline()
  studentNames = [r.strip() for r in studentNames.split(',')]
  names = studentNameFile.read().splitlines()
  names = [r.replace(',', '') for r in names]

  for name in names:
    print(name)
  
  studentNameFile.close()

def listGrades():
  """Lists the grades for each assignment/test for each student"""
  studentGradesFile = open("grades.txt", "r")
  studentGrades = list(csv.reader(studentGradesFile))
  assignments = studentGrades.pop(0)[1:]
  names = studentGradesFile.read().splitlines()
  names = [r.replace(',', '') for r in names]

  for name in studentGrades:
    print(name[0])
    for i, item in enumerate(assignments, start = 1):
      print(item.strip() + ': ' + name[i])
    print()
  
  studentGradesFile.close()

def listAttendance():
  """Lists the attendance with "Present" or "Absent" keyword for each student"""
  studentAttendanceFile = open("attendance.txt", "r")
  studentNames = list(csv.reader(studentAttendanceFile))
  dates = studentNames.pop(0)[1:]

  print("Which student?\n")
  for i, name in enumerate(studentNames, start = 1):
    print(f"{i} - {name[0]}")

  print()

  studentChoice = int(input("> "))
  if studentChoice in range(len(studentNames) + 1):
    s = studentNames[studentChoice - 1]
    print(s[0])
    s = zip(dates, s[1:])
    for date, grades in s:
      print(f"{date.strip()}: {grades}")
    print()
  else:
    print("Invalid entry! Try again...\n")
    menu()
  
  studentAttendanceFile.close()

def submitGrades():
  """Records the grades submitted via user input and assignment selection"""
  with open("grades.txt", "r") as f:
    studentGrades = list(csv.reader(f))
  assignments = studentGrades[0][1:]
  names = [r[0] for r in studentGrades[1:]]

  print("Which assignment/test?")
  for i, file in enumerate(assignments, start = 1):
    print(f"{i} - {file.strip()}")

  print()

  fileChoice = int(input("> "))
  if fileChoice in range(len(assignments) + 1):
    for i, name in enumerate(names, start = 1):
      grades = str(input(f"Grade for {name} for {assignments[fileChoice - 1].strip()} > "))
      studentGrades[i][fileChoice] = grades
    
    with open("grades.txt", 'w', newline = '') as f:
      csv.writer(f).writerows(studentGrades)
  else: 
    print("Invalid entry! Try again...\n")
    menu()

def takeAttendance():
  """Records attendance for each student by the date selected"""
  with open("attendance.txt", "r") as f:
    studentAttendance = list(csv.reader(f))
  attendance = studentAttendance[0][1:]
  names = [r[0] for r in studentAttendance[1:]]

  print("Which date?")
  for i, dates in enumerate(attendance, start = 1):
    print(f"{i} - {dates.strip()}")

  print()
  dateChoice = int(input("> "))
  print()

  if dateChoice in range(len(attendance) + 1):
    for i, name in enumerate(names, start = 1):
      presentAbsent = str(input(f"Student {name} (p/a) > "))
      if (presentAbsent == 'a') or (presentAbsent == 'A'):
          presentAbsent = 'Absent'
      elif (presentAbsent == 'p') or (presentAbsent == 'P'):
          presentAbsent = 'Present'
      else:
          presentAbsent()
      studentAttendance[i][dateChoice] = presentAbsent
    
    with open("attendance.txt", 'w', newline = '') as f:
      csv.writer(f).writerows(studentAttendance)
  else: 
    print("Invalid entry! Try again...\n")
    menu()

def menu():
  """Main driver for the student roster program"""
  presentChoice = False

  while not presentChoice:
    print()
    print("What do you want to do?\n")
    print("1 - List all students")
    print("2 - List all grades")
    print("3 - List attendance")
    print("4 - Submit a grade")
    print("5 - Take attendance")
    print("Q - Quit")
    print()

    choice = str(input("> "))
    print()

    while not (choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == 'Q' or choice == 'q'):
      print("Invalid entry. Try again")
      choice = str(input("> "))

    if (choice == '1'):
      listNames()
    elif (choice == '2'):
      listGrades()
    elif (choice == '3'):
      listAttendance()
    elif (choice == '4'):
      submitGrades()
    elif (choice == '5'):
      takeAttendance()
    else:
      break
menu()