
# This is a school project in DD1334 HT23 Database Technology (dbtech23)

Grupp:
- Alexander Karolin
- Oskar Edén Wallberg

Hej, vårt projekt består av två servrar (en för frontend och webbsidan och en för backend med routing och sqlite3 databas). 

techstack:
- React med jsx
- Python, Flask
- Sqlite3 för databas

För att starta projektet:
Kopiera projektet till en mapp och kör följande:
> cd backend
> pip install -r requirements.txt
> cd ..
> cd frontend
> npm install
> npm run dev
(kör app.py filen i en terminal och starta med npm run dev i en annan separat)

Om detta inte fungerar visar vi gärna vad vi har gjort vid nästa tillfälle. Iom att appen fortfarande är i demo fasen finns inte ett snabbkommando for att starta den men kommer att implementeras. 







______________________________________________________________
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



# Backend Structure:
Resource - https://github.com/mtnbarreto/flask-base-api/tree/master/flask-api/project

- flask-server/
    - db/
        - create_databases.sql
    - project/
        - api/
            - utils/
                - __init__.py
                - decorators.py
                - exceptions.py
                - error_handlers.py
            - routes/
                - __init__.py
                - ...all my blueprints...
            - __init__.py
        - models/
            - __init__.py
            - ...all my models...
        - __init__.py               # imports blueprints and registers them
        - config.py                 # config classes 
        - extensions.py             # init flask extensions used
    - tests/
        - ...tests for models and blueprint routes...
    - set_env_vars.sh