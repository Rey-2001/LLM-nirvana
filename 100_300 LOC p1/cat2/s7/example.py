import matplotlib.pyplot as plt
# import datetime
from datetime import datetime, timedelta

def getResourceProvider(resourceId_string):
    word_list = resourceId_string.split("/")
    prov_idx = word_list.index("providers")
    rp_idx = prov_idx + 1
    
    rname = word_list[rp_idx] # resource provider name, eg. "Microsoft.EventHub"
    lst = rname.split(".")
    rname = lst[1] # eg. "EventHub"
    return rname, word_list


def process_json(pipelineComponentsJsonDictionary):
    '''
    Function: Processes the JSON containing pipeline components, obtained after 
    running the Geneva action,
    To separate out the resourceIds of ASA, EH and SF components in lists. 

    comp - accronym for component
    '''
    # IDs of components
    asa_list = [] 
    eh_list = []
    sf_list = [] 
    
    eh_namespaces = [] 
    sf_apps = [] # application names 
    componentId_kind = {} 
    compId_health = {} 
    components_info_dictionary = {}

    for pipeline_list, pipeline_model in pipelineComponentsJsonDictionary.items():
        for pipeline_name, components_list in pipeline_model.items():
            for component in components_list:
                resourceId_string = component["resourceId"]
                rname, word_list = getResourceProvider(resourceId_string)

                componentId_kind[resourceId_string] = component["kind"]

                attribute_dictionary = {}
                attribute_dictionary['kind'] = component['kind']
                attribute_dictionary['name'] = component['name']
                attribute_dictionary['status'] = ''
                components_info_dictionary[resourceId_string] = attribute_dictionary

                kind = component['kind']
                kind = kind.lower()

                # separate lists of resourceIDs
                if rname == "ServiceFabric":
                    sf_list.append(resourceId_string) 
                    app_name = component["name"]
                    sf_apps.append(app_name)
                    attribute_dictionary['type'] = 'ServiceFabric'

                    if 'gls' in kind:
                        attribute_dictionary['position'] = 1

                elif rname == "EventHub":
                    eh_list.append(resourceId_string)
                    attribute_dictionary['type'] = 'EventHub'

                    namespaces_idx = word_list.index("namespaces")
                    ns_idx = namespaces_idx + 1
                    name_space =  word_list[ns_idx]
                    eh_namespaces.append(name_space) 

                    if ('ingestion' in kind) or ('ingestion' in name_space.lower()):
                        attribute_dictionary['position'] = 2
                    elif ('input' in kind) or ('sink' in name_space.lower()):
                        attribute_dictionary['position'] = 4
                    elif ('reducer' in kind) and ('output' in kind):
                        attribute_dictionary['position'] = 6
                    elif ('processor' in kind) and ('output' in kind):
                        attribute_dictionary['position'] = 8
                    elif 'pav2' in kind:
                        attribute_dictionary['position'] = 10
                    # else: its not a valid component and should not be shown

                elif rname == "StreamAnalytics":
                    asa_list.append(resourceId_string)
                    attribute_dictionary['type'] = 'StreamAnalytics'

                    if 'mdsprocessor' in kind:
                        attribute_dictionary['position'] = 3
                    elif 'reducer' in kind:
                        attribute_dictionary['position'] = 5
                    elif ('processor' in kind) and ('mds' not in kind) and ('emission' not in kind):
                        attribute_dictionary['position'] = 7
                    elif 'pav2' in kind:
                        attribute_dictionary['position'] = 9
                    elif 'latency' in kind:
                        attribute_dictionary['position'] = 11

                else:
                    print("ERROR: provider name not listed")

    sorted_comps = dict(sorted(components_info_dictionary.items(), key=lambda x: x[1]['position']))
    return eh_list, eh_namespaces, asa_list, sf_list, sf_apps, componentId_kind, compId_health, sorted_comps

def process_time(endTime, time_delta_minutes):
    '''
    Function: processes the endTime, to get the startTime at desired time difference. 
    '''
    adjusted_timestamp = endTime[:-3]
    datetime_obj = datetime.strptime(adjusted_timestamp, '%Y-%m-%dT%H:%M:%S.%f')
    formatted_timestamp = datetime_obj.strftime('%Y-%m-%d %H:%M:%S.%f')
    # Convert formatted timestamp to datetime object
    datetime_obj = datetime.strptime(formatted_timestamp, '%Y-%m-%d %H:%M:%S.%f')
    # Subtract 120 minutes from the datetime object
    new_datetime_obj = datetime_obj - timedelta(minutes=time_delta_minutes)
    # Convert the new datetime object back to a formatted timestamp
    new_formatted_timestamp = new_datetime_obj.strftime('%Y-%m-%d %H:%M:%S.%f')
    return new_formatted_timestamp