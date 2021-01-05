### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# probably a bad idea to look at an ace as 1, it could be high or low, but is commonly worth "more points".
  def check_for_ace(self, card): 
    if card.value = 1: #this should have a comparator not be assigning 1
      return True
    else # missing a colon here 
      return False
   

  dif highest_card(self, card1 card2): #incorrect spelling of def, missing a comma between params
  if card1.value > card2.value:
    return card
  else:
    return card2
  


def cards_total(self, cards): # indentation is wrong
  total # ideally set this to 0 to begin with
  for card in cards:
    total += card.value
    return "You have a total of" + total #this line should be broken out of the for loop, otherwise the loop will only ever run on the first item
  
```
