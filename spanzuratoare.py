import hangmanClient, json
id_student = "puscasemanuel7@gmail.com"
password = "FBNVWZ"
litere =['I', 'E', 'R', 'A', 'L', 'O', 'T', 'N', 'U', 'C', 'S', 'Ä', 'Ă', 'M', 'P', 'D', 'Ț', 'G', 'B', 'Z', 'F', 'Ș', 'V', 'H', 'Â', 'Î', 'J', 'X', 'K', 'Y', 'W', 'Q']
jocuri = []

def adauga_litere(litera, cuvant, pozitii_litere):
    cuvantnou = list(cuvant)
    for pozitii in pozitii_litere:
        cuvantnou[pozitii] = litera
    cuvantnou = "".join(cuvantnou)
    cuvant = cuvantnou
    return cuvant

def rezolva(joc):
    i=0
    id = joc["id"]
    cuvantc = joc["cuvant"]
    while "*" in cuvantc:
        if i < len(litere):
            pozitiilitere = unde_se_potriveste_litera(id_student,id,litere[i])
            cuvantc = adauga_litere(litere[i], cuvantc,pozitiilitere)
            i += 1
        else:
            break
    verifica_cuvantul(id_student,id,cuvantc)

def unde_se_potriveste_litera(id_student, id_joc, litera):
    """
    pozitiilitere = []
    for joc in jocuri:
        if joc["id"] == id_joc:
            cuvantcorect = joc["cuvantcorect"]
            joc["incercari"] +=1
    for i in range(0, len(cuvantcorect)):
        if cuvantcorect[i] == litera:
            pozitiilitere.append(i)
    return pozitiilitere
    """
    for joc in jocuri:
        if joc["id"] == id_joc:
            joc["incercari"] += 1
    return hangmanClient.check_letter(id_joc, litera)

def verifica_cuvantul(id_student, id_joc, cuvant_format):
    """"
    for joc in jocuri:
        if joc["id"] == id_joc:
            cuvantcorect = joc["cuvantcorect"]
    if cuvant_format == cuvantcorect:
        return 1
    else:
        return 0
    """
    return hangmanClient.check_word(id_joc, cuvant_format)


def main():
    hangmanClient.login(id_student, password)
    numarJocuri = 0
    numarTotalIncercari = 0

    while True:
        game = hangmanClient.new_game()
        game = {"id": game["game_id"], "cuvant": game["word_to_guess"], "cuvantcorect": "", "incercari": 0}
        numarJocuri += 1
        if game["id"] == 100:
            break
        jocuri.append(game)

    for joc in jocuri:
        rezolva(joc)
    print("nr_jocuri", numarJocuri)

    for joc in jocuri:
        numarTotalIncercari += joc["incercari"]

    print("incercari", numarTotalIncercari)
    with open("date_iesire_timestamp.txt", "w") as g:
        for joc in jocuri:
            print(joc["id"], ";", joc["incercari"], sep="")
            g.write(str(str(joc["id"])+";"+str(joc["incercari"])+"\n"))


if __name__ == '__main__':
    main()
