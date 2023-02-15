1)codeproject is the main Django project which has application called codeapp
2)insidde codeapp file dataloadsqlite4.py is the data loading scripts which reads from folder ../wx_data and reads every file and inserts into sqlite db.
3)models.py has WeatherData model which corresponds to  codeapp_weatherdata table.

pagination
http://localhost:8000/weather/?page=5

stats
pagination
http://localhost:8000/weather/stats/?page=5


CodePipeline with S3 , codedBuild  and codeDeploy
Each pipeline stage can create aritifacts
Artifacts are passwd stored in Amazon s3 and passed on to the next stage