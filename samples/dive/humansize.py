# -*- coding: utf-8 -*-
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'], 
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB','EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024=True):
  if size < 0:
    raise ValueError('number must be non-negative')
  mutiple = 1024 if a_kilobyte_is_1024 else 1000

  for suffix in SUFFIXES[mutiple]:
    size /= mutiple
    if size < mutiple:
      return '{0:.1f} {1}'.format(size, suffix)
  raise ValueError('number is large')

if __name__ == '__main__':
  print(approximate_size(1000000000000, False))
  print(approximate_size(1000000000000))
