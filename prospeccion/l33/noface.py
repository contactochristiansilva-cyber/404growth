# Tapa las caras de las referencias (Flow rechaza fotos con personas reconocibles).
# python3 -I noface.py <modelo yunet.onnx> <dir_in> <dir_out> archivos...
import sys, os, cv2
mdl, src, out = sys.argv[1:4]; os.makedirs(out, exist_ok=True)
for f in sys.argv[4:]:
    im = cv2.imread(os.path.join(src, f)); h, w = im.shape[:2]
    d = cv2.FaceDetectorYN.create(mdl, '', (w, h), 0.55, 0.3, 50)
    _, faces = d.detect(im)
    n = 0
    for fc in (faces if faces is not None else []):
        x, y, bw, bh = map(int, fc[:4]); cx, cy = x + bw // 2, y + bh // 2
        cv2.ellipse(im, (cx, cy - bh // 8), (int(bw * .9), int(bh * 1.1)), 0, 0, 360, (185, 185, 185), -1); n += 1
    cv2.imwrite(os.path.join(out, f), im, [cv2.IMWRITE_JPEG_QUALITY, 90])
    print(f, n)
