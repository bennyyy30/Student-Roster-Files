# Lab-09 - Student Roster Files
No more Mr. Nice Guy. This lab is intended to challenge you.  Yes you will be reading and writing to files, but that is the easy part. But think of it this way, this lab will have some "real world" applicability. So power though it and you'll come out the other side a much better Python programmer.

# Overview
Some applications are only useful if they can store data from one execution to the next. A student roster that tracks attendance and grades is a good example of that. A professor could use an application like this to take roll each day, then at the end of the semester all the historical data would be available for a report. This is called saving state. And it is done by using files. We will do a simplified version, but it will be complicated enough. Our application will use a command line interpreter to get user input and perform a few functions: show class list, show students' grades, show student attendances, submit a grade, or take attendance. Each time data is changed (or upon quitting) the input files get changed with the new data so that everything is there when the user runs the application again. 

# Background
I'll provide a few elements:
- a grades file. The header row for this file contains all the graded assignments/tests for the semester. The subsequent rows contain the student names and their grade for each assignment/test.  Initially the grades will all be blank, but you will notice commas to be used as delimiters between entries.
- an attendance file. The header row for this file contains all the class dates for the semester. The subsequent rows contain the student names and their attendance ("Present" or "Absent") for each class.  Initially the entries will all be blank, but you will notice commas to be used as delimiters between entries.

# Requirements
Your application **shall** read the contents of the two files and store the data such that the user can request to view it. The selection list shall be as follows  
>1 - List all students  
 2 - List all grades  
 3 - List attendance  
 4 - Submit a grade  
 5 - Take attendance  
 Q - Quit  
 
## Select 1
List the full names of all students
## Select 2
List the grade for each assignment/test for each student
## Select 3
First, let the user select from a list of students by number, then show the attendance ("Present" or "Absent") for each date for that student
## Select 4
First, let the user select from a list of assignments by number, then let them give a grade for each student one by one. For grades use percentages like 87.5. They can be strings
## Select 5
First, let the user select from a list of class dates by number, then let them give an attendance ("p" or "a") for each student one by one.

# Assignment Notes: 
Now that we are doing more complicated assignments, it is really important to plan out your logic before you start programming.  Write comments describing what needs to be done in the correct order (like pseudo code).  Then read over your comments and see if the logic makes sense.  Only when you are satisfied with your plan should you start actually coding.  Believe me, it will be quicker in the end this way.

See the example output to help you with the interface

