
mkdir templates 
python3 scaffold.py user username country_id:references email password phone job_id:references
python3 scaffold.py commit_dating user_id:references description
python3 scaffold.py country name
python3 scaffold.py programminglanguage name
python3 scaffold.py job name
python3 scaffold.py commit_coding programminglanguage_id:references user_id:references title content
python3 scaffold.py migration_trip destination user_id:references
python3 scaffold.py migration_database user_id:references content migration_trip_id:references
python3 scaffold.py artist name
python3 scaffold.py musicvideo artist_composer title
python3 scaffold.py artisthasmusicvideo musicvideo_id:references artist_id:references
python3 scaffold.py gossip content user_id:references
python3 scaffold.py artisthasgossip gossip_id:references artist_id:references
