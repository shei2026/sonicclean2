# 🔊 SonicClean2 (PWA instalable)

## 1) GitHub
```
git init
git add .
git commit -m "SonicClean2"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/sonicclean.git
git push -u origin main
```
## 2) Vercel
vercel.com → Add New → Project → importa `sonicclean` → Framework: **Other** → Deploy.
Enlace: `https://sonicclean.vercel.app`

## 3) QR
Abre tu enlace: la página ya muestra su QR. (Opcional: `python generar_qr.py` crea el PNG.)
Al escanearlo → abre la app → "Instalar app" (Android) o Compartir → Añadir a pantalla de inicio (iPhone).

## Opcional: APK con Flutter
`flutter create sonicclean && cd sonicclean && flutter pub add audioplayers`
Reemplaza lib/main.dart por flutter/lib/main.dart → `flutter build apk --release`
