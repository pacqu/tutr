# tutr  
##what is tut.r? you.r ultimate study buddy!
tut.r is a tinder-inspired web app that will match students wanting to find a study buddy || study group || tutor || tutee!
hosted on: tutr.mooo.com
tut.r video: https://www.youtube.com/watch?v=cEXAUxgVSVE
##how it'll work:
* users indicate their availability just by opening the app and selecting how they want to study (one to one || group).
* users will then scroll through available potential study mates in their area and choose based on mutual study topics and interests that are displayed with the potential study mate's info.
* matched users will then be able to communicate with each other to indicate where they want to meet to study!
* if no local study mates are available, users can match with other users to setup remote, virtual study sessions!

##how we'll make it work: 
- sqlite databases to register users || keep track of available users
- jquery + ajax calls to allow users to interact with each other (scroll display of available users | send messages | etc)
- bootstrap + propreitary css + javascript to make it all pretty
- geolocation + google maps api to figure out user location, location relative to other users

##what extras we want to do:
- set up chat ||blog set up that's constantly updated via Ajax call

##who's making it all work:
| role | name | username |
-------|------|------
| leader & middleware| justin pacquing | @stinographer |
| frontend | jeanne locker | @jlox |
| backend | gregory redozubov | @gredoz |

##foundational stuff:
- [x] signup page
- [x] front page
- [x] dashboard (settings, find a tutor, become a tutor, etc.)
- [x] settings page
- [x] matching page
- [x] register-as-tutr page
- [x] database - unique email, name, subject, inputted location, bio, availablility, matched/not matched, user matched with
- [x] ajax calls for finding a match - goes through database

##extra stuff we want to get done eventually:
- [] database holds more contact info - phone number, skype, facebook, etc.
- [] chat (how it's done: inputted through forms, sent/refreshed by ajax)
- [] allow the option to pair with a fellow study buddy rather than create a tutr/tutee dynamic
- [] organize by location | use some sort of location api
- [] connection to facebook (longshot)

##timetable
- [x] 01/07 - database
- [x] 01/08 - template for signup
- [x] 01/08 - template for intro
- [x] 01/08 - main page logged
- [x] 01/15 - all templates (edit bio, find tutors)
- [x] 01/17 - middleware (up to that point) finished
- [x] 01/20 - ajax calls (tutr search)
- [x] 01/22 - polish results
- [x] 01/24 - video done
- [x] 01/25 - due date
