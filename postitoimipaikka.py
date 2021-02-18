import json
with open('C:\Koulu\Ohjelmointi\Tehtävät\Kouluvuosi2\Koulu\Ohjelmointi\VUOSI2\Mobiiliohjelmointi\python\postinumerot-master\postcode_map_light.json') as f:
    sisalto = f.read()

postinumerot = json.loads(sisalto)


def etsi_toimipaikka(postinumero):
    
    if postinumero in postinumerot:
        return postinumerot[postinumero]
    else:
        return "Ei löytynyt"

def mainjuttu():

    numero = input("Kirjoita postinumero:")
    print(etsi_toimipaikka(numero))
    

if __name__ == '__main__':
    mainjuttu()