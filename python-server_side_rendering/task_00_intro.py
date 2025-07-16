import json
import os
def generate_invitations(template, array_list):

    '''Generate invitations'''
    if not isinstance(template, str):
        print(f'template must be a string, got {type(template).__name__}')
        return
    if not template:
        print('Template is empty, no output files generated.')
        return

    if not isinstance(array_list, list) or \
        not all(isinstance(dict_attendee, dict)
                for dict_attendee in array_list):
        print(
            'attendees must be a list and '
            'with only dictionaries got {}'.format(type(array_list).__name__)
            )
        return
    if not array_list:
        print(f'No data provided, no output files generated.')
        return

    i = 1
    for item in array_list:
        dictionary = item
        serialized = json.dumps(dictionary)
        unpacked   = json.loads(serialized)

        txt1 = template.format(name = unpacked['name'],  event_title = unpacked['event_title'], 
                               event_date = unpacked['event_date'],event_location = unpacked['event_location'])
        
        name_file = "output_" + str(i) + ".txt"
        if os.path.exists(name_file):
            print("Le fichier "+ name_file+ " existe deja")
        else:
            try:
                with open(name_file, "w") as f:
                    f.write(txt1)
            except:
                print("erreur d'ecriture")
        i = i + 1