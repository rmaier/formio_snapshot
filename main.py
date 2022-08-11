# main
#import csv
#import requests
#from datetime import datetime

# def inputfile name
ifname = "./input.csv"

## def read_csv
def read_csv(ifname): 
    '''
    This method is supposed to read the csv
    
    The csv needs to follow the following standard: 
    
    Project Name; Form Name; URL dev
    '''
    import csv
    import requests

    with open (ifname, newline='') as csvfile: 
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader: 
             print(', '.join(row))
    return row
 
    #proj_name = row[0]
    #form_name = row[1]
    #url = row[2]

# call read_csv
ifname_content = read_csv(ifname)

## def get json
def get_json(url = ifname_content[2]):
    '''
    This method is supposed to get the JSON data 
    '''
    import requests
    r = requests.get(url)
    
    return r

# call get_json
get_json_data = get_json(ifname_content[2])

# call write_json

## def write_json
def write_json(proj_name, form_name, data = get_json_data.content):
    ''''
    This method is supposed to write the JSON data 
    in a file
    '''
    from datetime import datetime
    
    now = datetime.now() # current date and time
    ofname_date = now.strftime("%Y.%m.%d_%H%M") # e.g.: '2022.08.11_1229'

    open(ofname_date+"_"+proj_name+" -"+form_name+".json", "wb").write(data)

    now_time = now.strftime("%Y.%m.%d %H:%M")
    print('[LOG] '+now_time+': Backup created suceccfully')
    
# call write_json
proj_name = ifname_content[0]
form_name = ifname_content[1]

write_json(proj_name, form_name, get_json_data.content)

