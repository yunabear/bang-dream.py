import requests as rq
#simpan_data = []
alldata = {
    'data1':{
        # Kasumi Toyama : 0
        # Tae Hanazono : 1
        # Rimi Ushigome : 2
        # Saaya Yamabuki : 3
        # Arisa Ichigaya : 4
        # Ran Mitake : 5
        # Moca Aoba : 6
        # Himari Uehara : 7
        # Tomoe Udagawa : 8
        # Tsugumi Hazawa : 9
    },
    'data2':{
        # Kokoro Tsurumaki : 0
        # Kaoru Seta : 1
        # Hagumi Kitazawa : 2
        # Kanon Matsubara : 3
        # Misaki Okusawa : 4
        # Aya Maruyama : 5
        # Hina Hikawa : 6
        # Chisato Shirasagi : 7
        # Maya Yamato : 8
        # Eve Wakamiya : 9
    },
    'data3':{
        # Yukina Minato : 0
        # Sayo Hikawa : 1
        # Lisa Imai : 2
        # Ako Udagawa : 3
        # Rinko Shirokane : 4
        # Mashiro Kurata : 5
        # Touko Kirigaya : 6
        # Nanami Hiromachi : 7
        # Tsukushi Futaba : 8
        # Rui Yashio : 9
    },
    'data4':{
        # Layer : 0
        # Lock : 1
        # Masking : 2
        # Pareo : 3
        # chu2 : 4
    }
}

class kumpulan_api():
    def api1():
        api = rq.get('http://bandori.party/api/members/')
        apijson = api.json()
        for i in range(len(apijson['results'])):
            alldata['data1'] = apijson['results']

    def api2():
        api = rq.get('https://bandori.party/api/members/?page=2')
        apijson = api.json()
        for i in range(len(apijson['results'])):
            alldata['data2'] = apijson['results']

    def api3():
        api = rq.get('https://bandori.party/api/members/?page=3')
        apijson = api.json()
        for i in range(len(apijson['results'])):
            alldata['data3'] = apijson['results']

    def api4():
        api = rq.get('https://bandori.party/api/members/?page=4')
        apijson = api.json()
        for i in range(len(apijson['results'])):
            alldata['data4'] = apijson['results']
    api1()
    api2()
    api3()
    api4()

def searchMember(name):
    save = name
    
    # data1
    kasumi = ("kasumi","kasumi toyama","toyama kasumi")
    tae = ("otae","tae","tae hanazono","hanazono tae")
    rimirin = ("rimirin","rimi","rimi ushigome","ushigome rimi")
    saaya = ("saaya","saya","saaya yamabuki","yamabuki saaya","saya yamabuki","yamabuki saya")
    arisa = ("arisa","ichigaya arisa","arisa ichigaya")
    ran = ("ran","ran mitake","mitake ran")
    moca = ("moca","moca aoba","aoba moca")
    himari = ("himari uehara","uehara himari","himari")
    tomoe = ("tomoe","tomoe udagawa","udagawa tomoe")
    tsugumi = ("tsugumi","hazawa","tsugumi hazawa","hazawa tsugumi")

    # data2
    kokoro = ("kokoro","kokoro tsurumaki","tsurumaki kokoro")
    kaoru = ("kaoru","kaoru seta","seta kaoru")
    hagumi = ("hagumi","hagumi kitazawa","kitazawa hagumi")
    kanon = ("kanon","kanon matsubara","matsubara kanon")
    misaki = ("misaki","misaki okusawa","okusawa misaki")
    aya = ("aya maruyama","aya","maruyama aya")
    hina = ("hina","hina hikawa","hikawa hina")
    chisato = ("chisato","chisato shirasagi","shirasagi chisato")
    maya = ("maya yamato","maya","yamato maya")
    eve = ("eve","eve wakamiya","wakamiya eve")
    
    # data3
    yukina = ("yukina","yukina minato","minato yukina")
    sayo = ("sayo","sayo hikawa","hikawa sayo")
    lisa = ("lisa","lisa imai","imai lisa")
    ako = ("ako","ako udagawa","udagawa ako")
    rinko = ("rinrin","rinko","rinko shirokane","shirokane rinko")
    mashiro = ("mashiro","mashiro kurata","kurata mashiro")
    touko = ("touko","touko kirigaya","kirigaya touko")
    nanami = ("nanami","nanami hiromachi","hiromachi nanami")
    tsukushi = ("tsukushi","futaba","tsukushi futaba","futaba tsukushi")
    rui = ("rui","rui yashio","yashio rui")
    
    # data4
    layer = ("layer")
    lock = ("lock")
    masking = ("masking")
    pareo = ("pareo")
    chu = ("chu2","chuchu","chu chu","chu-chu")

    if save.lower() in kasumi:
        nama = alldata['data1'][0]['name']
        japan = alldata['data1'][0]['japanese_name']
        birthday = alldata['data1'][0]['birthday']
        school = alldata['data1'][0]['school']
        band = alldata['data1'][0]["i_band"]
        cv = alldata['data1'][0]['romaji_CV']
        image = alldata['data1'][0]['image']
        sq_image = alldata['data1'][0]['square_image']
    elif save.lower() in tae:
        nama = alldata['data1'][1]['name']
        japan = alldata['data1'][1]['japanese_name']
        birthday = alldata['data1'][1]['birthday']
        school = alldata['data1'][1]['school']
        band = alldata['data1'][1]["i_band"]
        cv = alldata['data1'][1]['romaji_CV']
        image = alldata['data1'][1]['image']
        sq_image = alldata['data1'][1]['square_image']
        return sq_image
    elif save.lower() in rimirin:
        nama = alldata['data1'][2]['name']
        japan = alldata['data1'][2]['japanese_name']
        birthday = alldata['data1'][2]['birthday']
        school = alldata['data1'][2]['school']
        band = alldata['data1'][2]["i_band"]
        cv = alldata['data1'][2]['romaji_CV']
        image = alldata['data1'][2]['image']
        sq_image = alldata['data1'][2]['square_image']
    elif save.lower() in saaya:
        nama = alldata['data1'][3]['name']
        japan = alldata['data1'][3]['japanese_name']
        birthday = alldata['data1'][3]['birthday']
        school = alldata['data1'][3]['school']
        band = alldata['data1'][3]["i_band"]
        cv = alldata['data1'][3]['romaji_CV']
        image = alldata['data1'][3]['image']
        sq_image = alldata['data1'][3]['square_image']      
    elif save.lower() in arisa:
        nama = alldata['data1'][4]['name']
        japan = alldata['data1'][4]['japanese_name']
        birthday = alldata['data1'][4]['birthday']
        school = alldata['data1'][4]['school']
        band = alldata['data1'][4]["i_band"]
        cv = alldata['data1'][4]['romaji_CV']
        image = alldata['data1'][4]['image']
        sq_image = alldata['data1'][4]['square_image']
    elif save.lower() in ran:
        nama = alldata['data1'][5]['name']
        japan = alldata['data1'][5]['japanese_name']
        birthday = alldata['data1'][5]['birthday']
        school = alldata['data1'][5]['school']
        band = alldata['data1'][5]["i_band"]
        cv = alldata['data1'][5]['romaji_CV']
        image = alldata['data1'][5]['image']
        sq_image = alldata['data1'][5]['square_image']
    elif save.lower() in moca:
        nama = alldata['data1'][6]['name']
        japan = alldata['data1'][6]['japanese_name']
        birthday = alldata['data1'][6]['birthday']
        school = alldata['data1'][6]['school']
        band = alldata['data1'][6]["i_band"]
        cv = alldata['data1'][6]['romaji_CV']
        image = alldata['data1'][6]['image']
        sq_image = alldata['data1'][6]['square_image']
    elif save.lower() in himari:
        nama = alldata['data1'][7]['name']
        japan = alldata['data1'][7]['japanese_name']
        birthday = alldata['data1'][7]['birthday']
        school = alldata['data1'][7]['school']
        band = alldata['data1'][7]["i_band"]
        cv = alldata['data1'][7]['romaji_CV']
        image = alldata['data1'][7]['image']
        sq_image = alldata['data1'][7]['square_image']
    elif save.lower() in tomoe:
        nama = alldata['data1'][8]['name']
        japan = alldata['data1'][8]['japanese_name']
        birthday = alldata['data1'][8]['birthday']
        school = alldata['data1'][8]['school']
        band = alldata['data1'][8]["i_band"]
        cv = alldata['data1'][8]['romaji_CV']
        image = alldata['data1'][8]['image']
        sq_image = alldata['data1'][8]['square_image']
    elif save.lower() in tsugumi:
        nama = alldata['data1'][9]['name']
        japan = alldata['data1'][9]['japanese_name']
        birthday = alldata['data1'][9]['birthday']
        school = alldata['data1'][9]['school']
        band = alldata['data1'][9]["i_band"]
        cv = alldata['data1'][9]['romaji_CV']
        image = alldata['data1'][9]['image']
        sq_image = alldata['data1'][9]['square_image']
    elif save.lower() in kokoro:
        nama = alldata['data2'][0]['name']
        japan = alldata['data2'][0]['japanese_name']
        birthday = alldata['data2'][0]['birthday']
        school = alldata['data2'][0]['school']
        band = alldata['data2'][0]["i_band"]
        cv = alldata['data2'][0]['romaji_CV']
        image = alldata['data2'][0]['image']
        sq_image = alldata['data2'][0]['square_image']
    elif save.lower() in kaoru:
        nama = alldata['data2'][1]['name']
        japan = alldata['data2'][1]['japanese_name']
        birthday = alldata['data2'][1]['birthday']
        school = alldata['data2'][1]['school']
        band = alldata['data2'][1]["i_band"]
        cv = alldata['data2'][1]['romaji_CV']
        image = alldata['data2'][1]['image']
        sq_image = alldata['data2'][1]['square_image']
    elif save.lower() in hagumi:
        nama = alldata['data2'][2]['name']
        japan = alldata['data2'][2]['japanese_name']
        birthday = alldata['data2'][2]['birthday']
        school = alldata['data2'][2]['school']
        band = alldata['data2'][2]["i_band"]
        cv = alldata['data2'][2]['romaji_CV']
        image = alldata['data2'][2]['image']
        sq_image = alldata['data2'][2]['square_image']
    elif save.lower() in kanon:
        nama = alldata['data2'][3]['name']
        japan = alldata['data2'][3]['japanese_name']
        birthday = alldata['data2'][3]['birthday']
        school = alldata['data2'][3]['school']
        band = alldata['data2'][3]["i_band"]
        cv = alldata['data2'][3]['romaji_CV']
        image = alldata['data2'][3]['image']
        sq_image = alldata['data2'][3]['square_image']
    elif save.lower() in misaki:
        nama = alldata['data2'][4]['name']
        japan = alldata['data2'][4]['japanese_name']
        birthday = alldata['data2'][4]['birthday']
        school = alldata['data2'][4]['school']
        band = alldata['data2'][4]["i_band"]
        cv = alldata['data2'][4]['romaji_CV']
        image = alldata['data2'][4]['image']
        sq_image = alldata['data2'][4]['square_image']
    elif save.lower() in aya:
        nama = alldata['data2'][5]['name']
        japan = alldata['data2'][5]['japanese_name']
        birthday = alldata['data2'][5]['birthday']
        school = alldata['data2'][5]['school']
        band = alldata['data2'][5]["i_band"]
        cv = alldata['data2'][5]['romaji_CV']
        image = alldata['data2'][5]['image']
        sq_image = alldata['data2'][5]['square_image']    
    elif save.lower() in hina:
        nama = alldata['data2'][6]['name']
        japan = alldata['data2'][6]['japanese_name']
        birthday = alldata['data2'][6]['birthday']
        school = alldata['data2'][6]['school']
        band = alldata['data2'][6]["i_band"]
        cv = alldata['data2'][6]['romaji_CV']
        image = alldata['data2'][6]['image']
        sq_image = alldata['data2'][6]['square_image']
    elif save.lower() in chisato:
        nama = alldata['data2'][7]['name']
        japan = alldata['data2'][7]['japanese_name']
        birthday = alldata['data2'][7]['birthday']
        school = alldata['data2'][7]['school']
        band = alldata['data2'][7]["i_band"]
        cv = alldata['data2'][7]['romaji_CV']
        image = alldata['data2'][7]['image']
        sq_image = alldata['data2'][7]['square_image']
    elif save.lower() in maya:
        nama = alldata['data2'][8]['name']
        japan = alldata['data2'][8]['japanese_name']
        birthday = alldata['data2'][8]['birthday']
        school = alldata['data2'][8]['school']
        band = alldata['data2'][8]["i_band"]
        cv = alldata['data2'][8]['romaji_CV']
        image = alldata['data2'][8]['image']
        sq_image = alldata['data2'][8]['square_image']
    elif save.lower() in eve:
        nama = alldata['data2'][9]['name']
        japan = alldata['data2'][9]['japanese_name']
        birthday = alldata['data2'][9]['birthday']
        school = alldata['data2'][9]['school']
        band = alldata['data2'][9]["i_band"]
        cv = alldata['data2'][9]['romaji_CV']
        image = alldata['data2'][9]['image']
        sq_image = alldata['data2'][9]['square_image']
    elif save.lower() in yukina:
        nama = alldata['data3'][0]['name']
        japan = alldata['data3'][0]['japanese_name']
        birthday = alldata['data3'][0]['birthday']
        school = alldata['data3'][0]['school']
        band = alldata['data3'][0]["i_band"]
        cv = alldata['data3'][0]['romaji_CV']
        image = alldata['data3'][0]['image']
        sq_image = alldata['data3'][0]['square_image']
    elif save.lower() in sayo:
        nama = alldata['data3'][1]['name']
        japan = alldata['data3'][1]['japanese_name']
        birthday = alldata['data3'][1]['birthday']
        school = alldata['data3'][1]['school']
        band = alldata['data3'][1]["i_band"]
        cv = alldata['data3'][1]['romaji_CV']
        image = alldata['data3'][1]['image']
        sq_image = alldata['data3'][1]['square_image']
    elif save.lower() in lisa:
        nama = alldata['data3'][2]['name']
        japan = alldata['data3'][2]['japanese_name']
        birthday = alldata['data3'][2]['birthday']
        school = alldata['data3'][2]['school']
        band = alldata['data3'][2]["i_band"]
        cv = alldata['data3'][2]['romaji_CV']
        image = alldata['data3'][2]['image']
        sq_image = alldata['data3'][2]['square_image']
    elif save.lower() in ako:
        nama = alldata['data3'][3]['name']
        japan = alldata['data3'][3]['japanese_name']
        birthday = alldata['data3'][3]['birthday']
        school = alldata['data3'][3]['school']
        band = alldata['data3'][3]["i_band"]
        cv = alldata['data3'][3]['romaji_CV']
        image = alldata['data3'][3]['image']
        sq_image = alldata['data3'][3]['square_image']
    elif save.lower() in rinko:
        nama = alldata['data3'][4]['name']
        japan = alldata['data3'][4]['japanese_name']
        birthday = alldata['data3'][4]['birthday']
        school = alldata['data3'][4]['school']
        band = alldata['data3'][4]["i_band"]
        cv = alldata['data3'][4]['romaji_CV']
        image = alldata['data3'][4]['image']
        sq_image = alldata['data3'][4]['square_image']
    elif save.lower() in mashiro:
        nama = alldata['data3'][5]['name']
        japan = alldata['data3'][5]['japanese_name']
        birthday = alldata['data3'][5]['birthday']
        school = alldata['data3'][5]['school']
        band = alldata['data3'][5]["i_band"]
        cv = alldata['data3'][5]['romaji_CV']
        image = alldata['data3'][5]['image']
        sq_image = alldata['data3'][5]['square_image']
    elif save.lower() in touko:
        nama = alldata['data3'][6]['name']
        japan = alldata['data3'][6]['japanese_name']
        birthday = alldata['data3'][6]['birthday']
        school = alldata['data3'][6]['school']
        band = alldata['data3'][6]["i_band"]
        cv = alldata['data3'][6]['romaji_CV']
        image = alldata['data3'][6]['image']
        sq_image = alldata['data3'][6]['square_image']
    elif save.lower() in nanami:
        nama = alldata['data3'][7]['name']
        japan = alldata['data3'][7]['japanese_name']
        birthday = alldata['data3'][7]['birthday']
        school = alldata['data3'][7]['school']
        band = alldata['data3'][7]["i_band"]
        cv = alldata['data3'][7]['romaji_CV']
        image = alldata['data3'][7]['image']
        sq_image = alldata['data3'][7]['square_image']
    elif save.lower() in tsukushi:
        nama = alldata['data3'][8]['name']
        japan = alldata['data3'][8]['japanese_name']
        birthday = alldata['data3'][8]['birthday']
        school = alldata['data3'][8]['school']
        band = alldata['data3'][8]["i_band"]
        cv = alldata['data3'][8]['romaji_CV']
        image = alldata['data3'][8]['image']
        sq_image = alldata['data3'][8]['square_image']
    elif save.lower() in rui:
        nama = alldata['data3'][9]['name']
        japan = alldata['data3'][9]['japanese_name']
        birthday = alldata['data3'][9]['birthday']
        school = alldata['data3'][9]['school']
        band = alldata['data3'][9]["i_band"]
        cv = alldata['data3'][9]['romaji_CV']
        image = alldata['data3'][9]['image']
        sq_image = alldata['data3'][9]['square_image']
    elif save.lower() in layer:
        nama = alldata['data4'][0]['name']
        japan = alldata['data4'][0]['japanese_name']
        birthday = alldata['data4'][0]['birthday']
        school = alldata['data4'][0]['school']
        band = alldata['data4'][0]["i_band"]
        cv = alldata['data4'][0]['romaji_CV']
        image = alldata['data4'][0]['image']
        sq_image = alldata['data4'][0]['square_image']
    elif save.lower() in lock:
        nama = alldata['data4'][1]['name']
        japan = alldata['data4'][1]['japanese_name']
        birthday = alldata['data4'][1]['birthday']
        school = alldata['data4'][1]['school']
        band = alldata['data4'][1]["i_band"]
        cv = alldata['data4'][1]['romaji_CV']
        image = alldata['data4'][1]['image']
        sq_image = alldata['data4'][1]['square_image']
    elif save.lower() in masking:
        nama = alldata['data4'][2]['name']
        japan = alldata['data4'][2]['japanese_name']
        birthday = alldata['data4'][2]['birthday']
        school = alldata['data4'][2]['school']
        band = alldata['data4'][2]["i_band"]
        cv = alldata['data4'][2]['romaji_CV']
        image = alldata['data4'][2]['image']
        sq_image = alldata['data4'][2]['square_image']
    elif save.lower() in pareo:
        nama = alldata['data4'][3]['name']
        japan = alldata['data4'][3]['japanese_name']
        birthday = alldata['data4'][3]['birthday']
        school = alldata['data4'][3]['school']
        band = alldata['data4'][3]["i_band"]
        cv = alldata['data4'][3]['romaji_CV']
        image = alldata['data4'][3]['image']
        sq_image = alldata['data4'][3]['square_image']
    elif save.lower() in chu:
        nama = alldata['data4'][4]['name']
        japan = alldata['data4'][4]['japanese_name']
        birthday = alldata['data4'][4]['birthday']
        school = alldata['data4'][4]['school']
        band = alldata['data4'][4]["i_band"]
        cv = alldata['data4'][4]['romaji_CV']
        image = alldata['data4'][4]['image']
        sq_image = alldata['data4'][4]['square_image']
    else:
        nama = ""
        japan = ""
        birthday = ""
        school = ""
        band = ""
        cv = ""
        image = ""
        sq_image = ""
        print("Not Found!")
    text = f"Name : {nama} \nJapanese name : {japan} \nBirthday : {birthday} \nSchool : {school} \nBand : {band} \nCV : {cv} \n{image} \n{sq_image}"
    return text
