
# This is a school project in DD1334 HT23 Database Technology (dbtech23)

By:
- Oskar Wallberg
- Alexander Karolin

Scope:
Webapplication for Housing Cooperatives implementing database technologies
Focus om security, hashing, salting, session ids etc.
User login system storing account information 
- Members (guests, can view and change account related information)
- Admins (full access to whole system, can change settings and account information)
Booking system
- Scheduled times , displayed as time cards

Database in the form of SQLite
Frontend with React
Security with Firebase
Backend with Flask and python (maybe Express.js)

other...





## REDIS
> brew services start reids
> brew services stop redis
> redis-server  (ctrl-c to escape)
> redis-cli  (ctrl-c to escape)
    > lpush key element (...element)
    > lrange key start stop
    > rpop key
    > set key value
    > get key
    > del key
