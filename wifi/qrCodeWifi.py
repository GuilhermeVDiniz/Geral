import qrcode

def create_qrcode(ssid: str, password: str) -> qrcode.image.pure.PyPNGImage:
    wifi_data = f"Wifi:T:WPA;S:{ssid};P{password};;"
    return qrcode.make(wifi_data)

if __name__ == "__main__":
    ssid = "_NOME_DO_WIFI_"
    password = "_SENHA_"
