# data-warehouse-project
Udacity data engineer nanodegree data warehouse project
## Context:

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. Raw data is stored in the AWS S3 bucket. A cloud data warehouse is going to be implemented for analytical use cases. 

## Analytical goals:

The analytics team is particularly interested in understanding what songs users are listening to.

## Database schema design:

### Fact Table

1. **songplays** - records in log data associated with song plays i.e. records with page `NextSong`.

	* songplay\_id, start\_time, user\_id, level, song\_id, artist\_id, session\_id, location, user\_agent

### Dimension Tables

2. **users** - users in the app

	* user\_id, first\_name, last\_name, gender, level
	
3. **songs** - songs in music database
	* song\_id, title, artist\_id, year, duration

4. **artists** - artists in music database
	* artist_id, name, location, latitude, longitude
5. **time** - timestamps of records in songplays broken down into specific units
	* start\_time, hour, day, week, month, year, weekday

## ETL pipeline

**Step 0:** 
Launch redshift cluster and create IAM role for accessing S3 from redshift.

**Step 1:** 

run: `python create_tables.py` under the main directory

The script will create staging tables(storing the raw data from S3), fact table and dimension tables.

**Step 2:** 

run: `python etl.py` under the main directory.

The script will first transfer json files from S3 into the staging tables in Redshift. Events data will be copied into table `staging_events`; Song meta data will be copied into table `staging_songs`  

After all the data in S3 copied into staging tables, fact table `songplays` will be updated with data from staging tables. Then dimension tables `users, songs, artistists and time` will be updated with data from staging tables. 