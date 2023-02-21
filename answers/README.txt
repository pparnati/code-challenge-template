1)codeproject is the main Django project which has application called codeapp
2)insidde codeapp file dataloadsqlite4.py is the data loading scripts which reads from folder ../wx_data and reads every file and inserts into sqlite db.
3)models.py has WeatherData model which corresponds to  codeapp_weatherdata table.
4)views.py and urls.py inside codeapp have been modified to take care of the service api 
 have used sqllite database 
pagination
http://localhost:8000/weather/?page=5

stats
pagination
http://localhost:8000/weather/stats/?page=5

CREATE TABLE codeapp_weatherdata (
    id             INTEGER      NOT NULL
                                PRIMARY KEY AUTOINCREMENT,
    weatherdate    VARCHAR (8),
    maxtempofday   INTEGER,
    mintempofday   INTEGER,
    precipofday    INTEGER,
    weatherstation VARCHAR (16),
    theyear        INTEGER      NOT NULL
);


CREATE TABLE codeapp_yielddata (
    id             INTEGER     NOT NULL
                               PRIMARY KEY AUTOINCREMENT,
    theyear        INTEGER (4) NOT NULL,
    yieldoftheyear INTEGER
);

CodePipeline with S3 , codedBuild  and codeDeploy
Each pipeline stage can create aritifacts
Artifacts are passwd stored in Amazon s3 and passed on to the next stage
