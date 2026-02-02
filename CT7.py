roomnum = {
    'CSC101' : '3004',
    'CSC102' : '4501',
    'CSC103' : '6755',
    'NET110' : '1244',
    'COM241' : '1411'
}
instructors = {
    'CSC101' : 'Haynes',
    'CSC102' : 'Alvarado',
    'CSC103' : 'Rich',
    'NET110' : 'Burke',
    'COM241' : 'Lee',
}
meettime = {
    'CSC101' : '8:00 a.m.',
    'CSC102' : '9:00 a.m.',
    'CSC103' : '10:00 a.m.',
    'NET110' : '11:00 a.m.',
    'COM241' : '1:00 p.m.',
}
coursenum = input('Please enter your course code and number: ')
if coursenum in roomnum:
    print(f'\nCourse: {coursenum}')
    print(f'\nRoom: {roomnum[coursenum]}')
    print(f'\nInstructor: {instructors[coursenum]}')
    print(f'\nMeeting Time: {meettime[coursenum]}')
else:
    print(f'Course not found!')
