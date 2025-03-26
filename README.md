# EtkiyeTepki

**EtkiyeTepki**, Türkiye'deki protestoların görüntülerini bir araya getiren, açık kaynaklı arşiv amaçlı bir fotoğraf galerisi projesidir.

## Özellikler
- **Anlık Yükleme**: Görseller, yalnızca göründükleri anda yüklenir, böylece sayfa hızlı açılır.
- **Sonsuz Kaydırma**: Kullanıcı aşağı kaydırdıkça yeni görseller otomatik olarak yüklenir.
- **Basit ve Açık Kaynak**: Herkes katkıda bulunabilir veya projeyi özelleştirebilir.

## Kurulum
1. **Repoyu Klonlayın veya İndirin**:
   ```bash
   git clone https://github.com/yurttasgirisimi/EtkiyeTepki.git
   ```
2. **Görselleri Yükleyin**:
   - Protesto fotoğraflarınızı `arsiv/` klasörüne ekleyin.
   - Dosya adlarını anlamlı tutun (ör. `2023_ankara_protest.jpg`).
3. **Görsel Listesini Güncelleyin**:
   - `index.html` dosyasındaki `imageList` dizisini, kendi görsel dosya adlarınızla doldurun:
     ```javascript
     const imageList = [
         'arsiv/2023_ankara_protest.jpg',
         'arsiv/2023_istanbul_protest.jpg',
         // Daha fazla görsel ekleyin
     ];
     ```
4. **GitHub'a Yükleyin**:
   ```bash
   git add .
   git commit -m "Görseller ve galeri eklendi"
   git push origin main
   ```

## Kullanım
- Tarayıcınızda siteyi açtığınızda, görseller otomatik olarak yüklenir.
- Aşağı kaydırdıkça yeni görseller görünür.
- Mobil cihazlarda tek sütunlu bir düzenle uyumlu çalışır.

## Katkıda Bulunma
- Görseller eklemek, tasarımı geliştirmek veya kodu optimize etmek isterseniz, bir pull request gönderebilirsiniz.
- Önerileriniz için "Issues" sekmesini kullanabilirsiniz.

## Notlar
- Görsel sayınız çoksa, dosya boyutlarını optimize edin (ör. JPEG sıkıştırma).
- Dinamik görsel listesi için bir JSON dosyası kullanılabilir, ancak bu statik bir hosting olduğu için şu an manuel güncelleme gerektirir.

## Lisans
Bu proje açık kaynaktır ve [MIT Lisansı](#) altında dağıtılmaktadır (isteğe bağlı olarak lisans ekleyebilirsiniz).
