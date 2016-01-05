# tutr  
##what is tut.r? you.r ultimate study buddy!
tut.r is a tinder-inspired web app that will match students wanting to find a study buddy || study group || tutor || tutee!
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
| leader | justin pacquing | @stinographer |
| frontend | jeanne locker | @jlox |
| backend | gregory redozubov | @gredoz |

##what we need to do:
- signup page
- finish up front front page
- dashboard (settings, find a tutor, become a tutor, etc.)
- settings page
- matching page
- register-as-tutor page
- database - names, subject, (for now input location), bio, matched/not matched, seen/not seen, picture, (number/skype???)
- ajax call for finding a match - goes through database
- chat (how it's done: blog style page, refreshed by ajax)
- connection to facebook (maybe)
