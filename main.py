# main
#import csv
#import requests
#from datetime import datetime

# def variables
ifname = "./input.csv"
write_dir = "./snapshot/"

## def read_csv
def read_csv(ifname): 
    '''
    This method is supposed to read the csv
    
    The csv needs to follow the following standard: 
    
    Project Name; Form Name; URL dev
    '''
    import csv
    import requests

    with open (ifname, newline='') as f: 
        
        spamreader = csv.reader(f, delimiter=';', quotechar='|')
      
        data = []
        
        for line in spamreader: 
             data.append(line)
    return data

## def get json
def get_json(url):
    '''
    This method is supposed to get the JSON data 
    '''
    import requests
    r = requests.get(url)
    
    return r


## def write_json
def write_json(proj_name, form_name, write_dir, data = get_json_data.content):
    ''''
    This method is supposed to write the JSON data 
    in a file
    '''
    from datetime import datetime
    
    now = datetime.now() # current date and time
    ofname_date = now.strftime("%Y.%m.%d_%H%M") # e.g.: '2022.08.11_1229'

    open(write_dir+ofname_date+"_"+proj_name+" -"+form_name+".json", "wb").write(data)

    now_time = now.strftime("%Y.%m.%d %H:%M")
    print('[LOG] '+now_time+': Backup created sucessfully for: '+proj_name[0:15]+'...'+form_name[0:15])

    
# call read_csv
ifname_content = read_csv(ifname)


for i in range(1,len(ifname_content)):
    # call get_json
    get_json_data = get_json(ifname_content[i][2])
    #print(ifname_content[i][2])
    
    # call write_json
    proj_name = ifname_content[i][0]
    form_name = ifname_content[i][1]

    write_json(proj_name, form_name, write_dir, get_json_data.content)
