# Hệ chuyên gia tư vấn lựa chọn tai nghe (Python + Streamlit)

## Chạy ứng dụng
1. Cài Python 3.10 trở lên.
2. Mở Terminal/CMD tại thư mục chứa `app.py`.
3. Cài thư viện:
   ```bash
   pip install -r requirements.txt
   ```
4. Chạy:
   ```bash
   streamlit run app.py
   ```
5. Trình duyệt sẽ mở giao diện web tự động (thường tại `http://localhost:8501`).

## Cách tư vấn
- Lựa chọn diễn ra lần lượt: loại tai nghe, mục đích, ngân sách, thương hiệu, thiết bị kết nối, pin, chống ồn và chống nước.
- Mỗi câu trả lời tự động giới hạn các lựa chọn ở bước sau theo những sản phẩm còn phù hợp; nếu đổi một câu trả lời trước đó, các lựa chọn phía sau được đặt lại để tránh tổ hợp không hợp lệ.
- Chọn “Không ưu tiên” ở loại tai nghe để không giới hạn theo loại. Mục đích và ngân sách thu hẹp danh sách; thương hiệu và thiết bị kết nối tiếp tục lọc sản phẩm.
- Pin, chống ồn và chống nước mặc định không lọc; chỉ lọc khi người dùng chọn yêu cầu cụ thể.
- Danh sách kết quả và số sản phẩm phù hợp được cập nhật tự động theo các lựa chọn.
- Ảnh sản phẩm tương ứng được lấy từ thư mục `images` theo mã sản phẩm (ví dụ `SP4.png`).

## Lưu ý về tập luật
Tài liệu Word hiện đọc được có mô tả 12 sản phẩm và tập sự kiện, nhưng mục 2.2 “Xây dựng tập luật” chưa có nội dung luật. Vì vậy nguyên mẫu dùng cơ chế suy diễn theo điều kiện và chấm điểm được mô tả trong mã nguồn. Nếu nhóm có danh sách luật đầy đủ riêng, có thể thay hàm `hard_requirements_match` và `score_product` bằng bộ luật IF–THEN đúng theo danh sách đó.
