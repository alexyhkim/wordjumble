import sys

jumbleme = sys.argv[1]

def wordjumble(word):
  if len(word) <= 1:
    return [word]
  else:
    newjumbled = []
    first = word[0]
    jumbled = wordjumble(word[1:])
    seen = {}
    for jumble in jumbled:
      i = 0
      while i <= len(jumble):
        newjumble = jumble[:i] + first + jumble[i:]
        if not newjumble in seen:
          newjumbled.append(newjumble)
          seen[newjumble] = 1
        i += 1
    newjumbled += jumbled
    newjumbled.append(first)
    return newjumbled

  
    
for word in wordjumble(jumbleme):
  print word

  