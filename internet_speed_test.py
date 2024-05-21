import speedtest

def test_internet_speed():
    dl_speed = 0
    up_speed = 0
    try:
        sptest = speedtest.Speedtest()
        dl_speed = sptest.download() / 1000000
        up_speed = sptest.upload() / 1000000
    except speedtest.SpeedtestException as e:
        print("Ha ocurrido un error:", str(e))

    return {'download': dl_speed, 'upload': up_speed}
