set PGPASSWORD=postgres

pg_dump -U postgres -F c -v db_geonetwork > d:\\backup\\gn_db_%date:~10,4%%date:~4,2%%date:~7,2%.backup"