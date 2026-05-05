import cv2
import numpy as np


def contador_medicamentos_final(caminho_imagem):
    img = cv2.imread(caminho_imagem)
    if img is None:
        print("Erro ao carregar imagem.")
        return

    img = cv2.resize(img, (800, 600))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray_clahe = clahe.apply(gray)

    blurred = cv2.GaussianBlur(gray_clahe, (7, 7), 0)

    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    kernel_erosao = np.ones((5, 5), np.uint8)
    thresh = cv2.erode(thresh, kernel_erosao, iterations=2)

    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    output = img.copy()

    contador = 0
    for c in cnts:
        area = cv2.contourArea(c)

        if area > 200:
            contador += 1

            rect = cv2.minAreaRect(c)
            center, size, angle = rect

            expanded_size = (size[0] + 12, size[1] + 12)
            expanded_rect = (center, expanded_size, angle)

            box = cv2.boxPoints(expanded_rect)
            box = np.int32(box)

            cv2.drawContours(output, [box], 0, (255, 200, 50), 2, cv2.LINE_AA)

            cX, cY = int(center[0]), int(center[1])
            cv2.circle(output, (cX, cY), 3, (255, 255, 255), -1, cv2.LINE_AA)
            cv2.circle(output, (cX, cY), 4, (255, 200, 50), 1, cv2.LINE_AA)

            texto = f"{contador}"
            font = cv2.FONT_HERSHEY_DUPLEX
            escala = 0.6
            espessura = 1

            (tw, th), _ = cv2.getTextSize(texto, font, escala, espessura)
            tx = cX - (tw // 2)
            ty = cY - int(max(expanded_size) // 2) - 15

            pad = 5
            cv2.rectangle(output, (tx - pad, ty - th - pad), (tx + tw + pad, ty + pad), (30, 30, 30), -1)

            cv2.putText(output, texto, (tx, ty), font, escala, (255, 255, 255), espessura, cv2.LINE_AA)

    altura_banner = 80
    output_com_banner = cv2.copyMakeBorder(output, altura_banner, 0, 0, 0, cv2.BORDER_CONSTANT, value=[15, 15, 15])

    cv2.line(output_com_banner, (0, altura_banner), (800, altura_banner), (255, 200, 50), 2, cv2.LINE_AA)

    cv2.putText(output_com_banner, "SCANNER OTICO DE MEDICAMENTOS", (20, 35),
                cv2.FONT_HERSHEY_DUPLEX, 0.6, (180, 180, 180), 1, cv2.LINE_AA)

    cv2.putText(output_com_banner, f"Total Detectado: {contador}", (20, 65),
                cv2.FONT_HERSHEY_DUPLEX, 0.9, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("Mascara (Com CLAHE)", thresh)
    cv2.imshow("Scanner de Medicamentos", output_com_banner)
    print(f"Sucesso! {contador} objetos detectados.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

contador_medicamentos_final('assets/remedio.png')
