## Register Downloadable metadata to Datacite 

### Register_DOI_Datacite.py
### Metadata Info.csv file with following information

* ID
* UUID
* Title
* Date
* Author
* Abstract
* Purpose
* Link

Change Prefix and Login Info as require.

It creates the log file with date and time inside log folder with doi generation information.
 

*Required modules*

* datacite==1.0.1
* pandas==0.25.3
* requests==2.22.0

for more information :
https://datacite.readthedocs.io/en/latest/index.html#

### CheckRDSLink.py - Check metadata link RDS
#### DownloadListRDS.csv with following information
* ID
* UUID

create **Metadata_ERRORLIST.csv** file with error metadata link

### Stats_DOI.py List all the registered DOI from Datacite
### Generate DataciteDOI.csv file with following information
* DOI
* URL
* Identifier
* Title