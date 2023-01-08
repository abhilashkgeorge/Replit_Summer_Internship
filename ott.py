import json

def isValid(stale, latest, otjson):
  # this is the part you will write!
  cursorPosition = 0 

  #convertion of stringified list of dictionaries
  jsonValue = json.loads(otjson)
  
  if jsonValue == []:
    return True

  for operations in jsonValue:    
    if operations['op'] == 'insert':
      stale = operations['chars'] + stale
      cursorPosition += len(operations['chars'])
      
    elif operations['op'] == 'delete':
      if operations['count'] + cursorPosition > len(stale):
        return False #delete past end
      stale = stale[:cursorPosition] + stale[cursorPosition + operations['count']:]
      
    elif operations['op'] == 'skip':
      if operations['count'] + cursorPosition > len(stale):
        return False #skip past end
      cursorPosition += operations['count']

  return stale == latest

 

print(isValid(
  'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
  'Repl.it uses operational transformations.',
  '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]'
)) # true

print(isValid(
  'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
  'Repl.it uses operational transformations.',
  '[{"op": "skip", "count": 45}, {"op": "delete", "count": 47}]'
)) 
#expected answer - # false, delete past end

print(isValid(
  'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
  'Repl.it uses operational transformations.',
  '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}, {"op": "skip", "count": 2}]'
))# false, skip past end

print(isValid(
  'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
  'We use operational transformations to keep everyone in a multiplayer repl in sync.',
  '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]'
))#true
  
print(isValid(
  'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
  'We can use operational transformations to keep everyone in a multiplayer repl in sync.',
  '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]'
))# false

print(isValid(
  'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
  'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
  '[]'
))# true