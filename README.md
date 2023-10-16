Steps for installation of prerequisites
1. Install the requirements using `pip install -r requirements.txt`
2. Install postgresql and create a database named `postgres` with username `postgres` and password `mypostgres` and port `5432`
3. Change the directory to `h1bdata` using command `cd h1bdata`
4. Run the command `python manage.py makemigrations` and `python manage.py migrate` to create the database tables
5. Move the csv files to `data` folder inside the current directory
6. Run the command `python ingest.py` to add the data from the csv files to the database
7. Run the command `python manage.py runserver` to start the server

## API Endpoints
1. `/api/count/`: Returns the no. of applicants 
2. `/api/mean/`: Returns the mean of the annual salary in $
3. `/api/median/`: Returns the median of the annual salary in $
4. `/api/percentile/?val=0.25`: Returns the 25th percentile of the annual salary in $, replace 0.25 with the desired percentile to find other percentile values.

