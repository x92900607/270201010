GPA=float(input('your GPA:'))
num_lectures=int(input('lecture number:'))
if num_lectures < 47 and GPA < 2.0:
  print('not enough lectures and GPA!')
elif num_lectures < 47 and GPA >= 2.0:
  print('not enough lectures!')
elif num_lectures >= 47 and GPA < 2.0:
  print('not enough GPA!')
else:
  print('GRADUATED!')
