## Electric Gaadi Dashboard (EGD)

This repository hosts code for extracting, cleaning and transforming dataset of import of transport vehicles in Nepal.
The **Department of Customs** under **Ministry of Finance** publishes monthly statistics of import and export of goods for each fiscal year. We are using this data to build a dashboard to showcase trend of import of **Electric Vehicles** in Nepal.

This repository contains scripts for purpose of downloading the _xlsx_ files from DoC website, cleaning and extracting data from those files, transforming the data as per requirement and generating processed _csv_ file for ease of use.

### The purpose of scripts in this repo are as below:

### [1. download.ipynb](download.ipynb)

This script has code to download files from DoE website. Beautiful Soup library is used to acquire urls for various fiscal years page and files for the specific year. The excel and pdf files are downloaded and saved locally in `data` directory in a managed manner.

### [2. extract.ipynb](extract.ipynb)

This script does lump of work in cleaning and transforming the data. The data before fiscal year 2074/75 is discarded due to non-uniformity. The monthly data has values cumulated to that month from start of fiscal year. So data had to be transformed accordingly, only then it could be merged. So, this script handles tasks including:

- Reading excel files for each fiscal year, month wise
- Cleaining and structuring the data into a structured format: `hscode | description | unit | quantity | value | revenue`
- Subtracting values from previous month to get actual values for the month.
- Merging the data of all months in fiscal year.
- Tagging fiscal year and month in data.
- Merging the data for every fiscal year to produce unified csv of format: `fy | month | hscode | description | unit | quantity | value | revenue`

### [3. hscode/extract-2079-80.ipynb](hscode/extract-2079-80.ipynb)

This script extracts HS Codes and descriptions from Customs Tariff manual published by DoC. We found that HS Codes for most fiscal years' datasets matched with Custom Tariff lookup for fiscal year 2079/80. Since generating excel file from pdf published by DoC was a one off job, we did that manually using AI tools. We wrote this script to parse the generated excel file to generate strucutred lookup.

### [3. match.ipynb](match.ipynb)

This script checks if all HS Codes match with [lookup](hscode/lookup.csv), so that all data is accounted for. Any exceptions such as non-existing HS Codes are handled here by manual mapping. Certain HS Codes are tagged according to type of fuel used and type of vehicle, this is also handled here.

This script also contains function to lookup any HS Code upto 8 digits, which also returns descriptions for all umbrella HS Codes. E.g:
```py
> hscode_lookup(87022041)
    {
        'descriptions': [
            'Unassembled',
            'Jeep, Car and Van :',
            'With both compression-ignition internal combustion piston engine (diesel or semi-diesel) and electric motor as motors for propulsion:',
            'Motor vehicles for the transport of ten or more persons, including the driver.'],
        'duties': {'import_duty_saarc': '80', 'import_duty_general': '80'}
    }
```

## Usage

1. First download all files from DoC website running the `download.ipynb` notebook.

   This should download all files in `data` dir, inside corresponding fiscal year directories.

2. Extract data from excel files using the `extract.ipynb` notebook.

   This should generate `extracted.csv` in root dir.

3. Generate lookup for HS Codes using `hscode/extract-2078-80.ipynb` notebook.

   This should generate `hscode/data/fy-2079-80.csv`, copy it to `hscode/lookup.csv`.
   
    Although few exceptions are handled while matching data, some codes did not exist in this year's manual, those codes were added manually, and due to lack of time, we didn't have time to properly document this. You are encouraged to use the [lookup.csv](hscode/lookup.csv) for lookup.

4. Finally match the data and tags by running `match.ipynb` notebook.

   This should generate `final.csv` in root dir. This is the final data we can use.

---

### Team Members:

1. Jivan Parajuli
2. Rahul Adhikari
3. Sandesh Humagain
4. Saurav Pachhai
5. Utsab Singh
