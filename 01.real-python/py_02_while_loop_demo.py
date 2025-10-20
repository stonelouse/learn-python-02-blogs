def do_while_loop(iterable):
  count = 1
  while count <= len(iterable):
    upper = iterable[count - 1].upper()
    count += 1
    if upper == 'STOP':
      break
    if upper == 'CONT':
      continue
    print(upper)
  else:
    print('no break occured')
