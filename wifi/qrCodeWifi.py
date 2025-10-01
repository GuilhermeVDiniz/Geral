import qrcode
from PIL import Image


def create_qrcode(ssid: str, password: str) -> Image.Image:
    if not ssid or not password:
        raise ValueError("SSID e senha não podem estar vazios.")

    wifi_data = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    qr_image = qrcode.make(wifi_data)
    return qr_image


if __name__ == "__main__":
    ssid = "_NOME_DO_WIFI_"
    password = "_SENHA_"

    try:
        qr_image = create_qrcode(ssid, password)
        qr_image.save("qrcode_wifi.png")
        print("QR Code gerado e salvo com sucesso.")
    except ValueError as e:
        print(f"Erro - : {e}")
