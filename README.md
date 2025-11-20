<p align="center">
 <h1 align="center">QuickDraw</h1>

## Giới thiệu

Dưới đây là mã nguồn Python cho **QuickDraw** – một trò chơi trực tuyến do Google phát triển. Với mã nguồn này, bạn có thể:

* **Chạy ứng dụng cho phép bạn vẽ trực tiếp trước camera (nếu dùng laptop thì webcam sẽ được sử dụng mặc định)**
* **Chạy ứng dụng cho phép bạn vẽ trên canvas**

## Ứng dụng vẽ

Mã nguồn và bản demo sẽ được phát hành sớm.

## Dataset

Bộ dữ liệu dùng để huấn luyện mô hình có thể tìm thấy tại [Quick Draw dataset] trên Google Cloud Storage. Ở đây tôi chỉ chọn 20 tệp tương ứng với 20 loại đối tượng.

## Các lớp (Categories)

Bảng dưới đây mô tả 20 lớp mà mô hình sử dụng:

|            |        |           |          |
| ---------- | :----: | :-------: | :------: |
| apple      |  book  |   bowtie  |  candle  |
| cloud      |   cup  |    door   | envelope |
| eyeglasses | guitar |   hammer  |    hat   |
| ice cream  |  leaf  |  scissors |   star   |
| t-shirt    |  pants | lightning |   tree   |

## Mô hình đã huấn luyện

Bạn có thể tìm mô hình đã được huấn luyện tại **trained_models/whole_model_quickdraw**

## Huấn luyện

Bạn cần tải các tệp `.npz` tương ứng với 20 lớp và lưu vào thư mục **data**.
Nếu muốn huấn luyện mô hình với danh sách lớp khác, bạn chỉ cần thay đổi hằng số **CLASSES** trong file **src/config.py** và tải thêm các tệp `.npz` cần thiết.

Sau đó, bạn chỉ cần chạy:

```
python3 train.py
```

---

Nếu bạn muốn, mình có thể dịch file README này sang dạng chuyên nghiệp hơn, hoặc giúp bạn viết README chuẩn GitHub.
