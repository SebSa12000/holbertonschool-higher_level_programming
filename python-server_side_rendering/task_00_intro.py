import json
import os
def generate_invitations(template, array_list):
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