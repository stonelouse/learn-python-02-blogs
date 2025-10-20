def do_for_loop(iterable):
  for loop_var in iterable:
    upper = loop_var.upper()
    if upper == 'STOP':
      break
    if upper == 'CONT':
      continue
    print(upper)
  else:
    print('no break occured')
