#  Snake Game (Python / Tkinter)

Một trò chơi Rắn săn mồi cổ điển được xây dựng bằng Python 3 và Tkinter. Dự án áp dụng mô hình thiết kế phân tách MVC (Model-View-Controller) giúp quản lý mã nguồn bài bản, dễ bảo trì và nâng cấp.


##  Tính năng nổi bật

* Kiến trúc phân tách mô hình (Modular Design):** Tách bạch rõ ràng giữa Backend (Game Logic), Frontend (Tkinter UI) và Storage.
* Tự động tăng tốc độ:** Tốc độ di chuyển của rắn tăng dần sau mỗi 10 điểm đạt được.
* Lưu kỷ lục (High Score): Tự động đọc và ghi điểm cao nhất vào tệp `high_score.json`.
* Điều khiển linh hoạt: Hỗ trợ cả 4 phím mũi tên (`Arrow keys`) và cụm phím `WASD`.
* Giao diện trực quan: Tự động điều chỉnh khung chơi và nút chơi lại khi thua/thắng.



##  Cấu trúc thư mục

text
snake_game/
├── main.py          # Điểm khởi chạy ứng dụng
├── game_logic.py    # Backend: Thuật toán di chuyển, va chạm, điểm số
├── ui.py            # Frontend: Khung canvas, sự kiện bàn phím, giao diện
├── storage.py       # Quản lý đọc/ghi điểm cao nhất (high_score.json)
├── high_score.json  # File lưu trữ dữ liệu điểm số
└── README.md        # Tài liệu hướng dẫn dự án