
import postitoimipaikka

POSTINUMEROT = {
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}

ERIKOISTAPAUKSET = {
    "43800": "KIVIJÄRVI",
    "91150": "YLI-OLHAVA",
    "65374": "SMART POST",
    "28204": "SMARTPOST"
}

def test_helsigin_postinumero():
    tulos = postitoimipaikka.etsi_toimipaikka('00500')

    assert tulos == "HELSINKI"

# def test_postinumerot_omalla_datalla(mocker):
#     oma_data = ERIKOISTAPAUKSET
#     mocker.patch('json.loads(sisalto)', return_value=oma_data)

#     tulos = postitoimipaikka.etsi_toimipaikka('90210')

#     assert tulos == 'BEVERLY HILLS'