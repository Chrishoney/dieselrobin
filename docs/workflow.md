# Workflow

## Registration

### Authentication 

* player places `robin` at the top of their current trunk rcfile indicating they
  want to play
* player registers as their account name, indicating which server they want to
  play on. this can be changed later, but this determines the rcfile to check.

### Registration

* when registering, a player chooses a character for the pool. a character model
  is created, but not assigned to a specific team.
* a player will also choose/create a team. choices: 
    * a new team
    * an existing team
    * team random
    * None

## Setup

### Pre tournament

* some number of days prior to the start, a player must confirm their presence.
  they have up until start date + N (probably 2) to confirm or they are removed.
* conduct character distribution in a transparent way
* after characters are distributed, allow players to start assigning characters
  bonus missions and starting players.

### Before Play

* teams must assign all bonus missions before playing
* teams must decide on a play order before playing

## Tournament Time

### Object Modification

* only the player completing a mission is assigned to is able to 'complete' the mission.
* substitutions are allowed, and must be approved by a 'staff' user.
* provide a few configurable attributes defined in an inline team template
  stylesheet.
* only 'staff' users are allowed to modify tournament details

### Missions

**Regular**

* once a player completes/fails a mission, they must mark whether it was
  completed/failed. only the player who played the mission can do this.   

**Bonus**

* they should also mark any bonus missions they completed/failed to complete. all
team members are allowed to edit bonus mission details.

## Wrapping up

* teams will receive a grace period of an hour or two post tournament to finish
  up their final scoring tasks.
* once this is over, scores will be frozen. only a 'staff' member can modify
  details after the grace period following the end of the tournament is
  finished.
* once the tournament is closed, 1st, 2nd and 3rd place 'awards' will be given
  out.
* current stats will move to an archival view, something like
  http://dieselrobin.org/old/jan/2013 or http://dieselrobin.org/old/4 
