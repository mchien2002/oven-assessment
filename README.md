
## PRODUCT API

```markdown
# 🛠️ Backend Technical Assessment - Product API

## 1. Giới thiệu
Đây là dự án **Backend Technical Assessment** cho vị trí Backend Engineer.  
Ứng dụng được xây dựng bằng **Django + Django REST Framework**, tuân thủ chuẩn **RESTful API** để quản lý **sản phẩm (Products)** và xử lý **file upload** với một **cấu trúc Hashmap tự cài đặt**.

Điểm nổi bật:
- API hỗ trợ **CRUD** cho sản phẩm.
- API hỗ trợ **upload file** (hình ảnh/tài liệu) vào hệ thống file cục bộ.
- File/folder upload được lưu trữ và hiển thị lại theo dạng **cây JSON** với thư mục lồng nhau.
- Business logic được **tách biệt rõ ràng** trong **Service Layer**, giúp code dễ bảo trì, mở rộng, kiểm thử.

---

## 2. Công nghệ sử dụng
- **Python 3.11**
- **Django 5.x**
- **Django REST Framework (DRF)**
- **PostgreSQL** (chạy qua Docker)
- **Swagger (drf-yasg)** – tài liệu API
- **Pytest** – unit testing
- **Custom Hashmap** – cấu trúc dữ liệu cho upload

---

## 3. Cấu trúc thư mục
Dự án áp dụng mô hình **Service Layer**:


```

.  
├── applications  
│ ├── products  
│ │ ├── models/ # Models  
│ │ ├── serializers/ # DRF serializers  
│ │ ├── services/ # Business logic (Service Layer)  
│ │ ├── views/ # View xử lý request/response  
│ │ └── urls.py  
├── libs/ # Common libs: responses, logger, decorators , hashmap
├── djangoapp/ # Core settings, urls, wsgi  
├── docker/ # Docker configs  
└── manage.py

```

### 🔹 Service Layer
- **View**: chỉ tiếp nhận request và trả response.
- **Service**: chứa toàn bộ business logic (query DB, xử lý nghiệp vụ, thao tác dữ liệu).
- Lợi ích:
  - **SoC (Separation of Concerns)** – tách biệt rõ ràng.
  - **Dễ bảo trì, mở rộng**.
  - **Dễ viết unit test**.

Ví dụ (rút gọn):
```python
# services/product_service.py
class ProductService:
    @staticmethod
    @pretty_function()
    def create(data, logger):
        logger.debug("Creating product")
        product = Product.objects.create(**data)
        return ProductSerializer(product).data

```

----------

## 4. Chức năng đã triển khai

### ✅ Product API (CRUD)

-   `POST /products/v1/create` → Tạo sản phẩm
    
-   `GET /products/v1/products` → Danh sách sản phẩm
    
-   `GET /products/v1/product/{id}/` → Chi tiết sản phẩm
    
-   `PUT /products/v1/update/{id}/` → Cập nhật sản phẩm
    
-   `DELETE /products/v1/delete/{id}/` → Xoá sản phẩm

-   `POST /products/v1/uploads/{id}/` → Upload attachments cho sản phẩm

    

Schema sản phẩm ví dụ:

```json
{
  "id": "uuid",
  "name": "Laptop Gaming",
  "price": 25000000,
  "description": "Laptop cấu hình cao",
  "image_url": "/images/xxx.jpg",
  "created_at": "2025-10-01T12:00:00Z",
  "updated_at": "2025-10-01T12:00:00Z"
}

```

### ✅ Upload + Tree API

-   `POST /api/attachments/upload/` → Upload file/folder
    
-   `GET /api/attachments/tree/` → Trả về cây JSON
    

Ví dụ output:

```json
"attachments": {
      "product_id": {
        "images": {
          "img_1.jpg": {
            "size": 1829268,
            "type": "image/jpeg"
          }
        },
        "pdf": {
          "pdf_1.pdf": {
            "size": 110629,
            "type": "application/pdf"
          },
          "pdf_2.pdf": {
            "size": 110629,
            "type": "application/pdf"
          }
        },
        "media": {
          "video.mp4": {
            "size": 41879884,
            "type": "video/mp4"
          }
        }
      }
    }
  }
```

```

### ✅ Hashmap Custom

-   Tự cài đặt Hashmap (chaining để xử lý collision).
    
-   Hashmap dùng lưu metadata của file trước khi trả JSON.
    

### ✅ Database

-   PostgreSQL trong Docker.
    
-   Không sử dụng Migration.
    

### ✅ Swagger

-   Tài liệu API: `http://127.0.0.1:3000/api-docs/`
    

### ✅ Unit Test

-   Test CRUD products.
    
-   Test Hashmap (insert, get, delete).
    
-   Test API upload + tree.
    

----------

## 5. Hướng dẫn cài đặt

### 1. Clone repo

```bash
git clone https://github.com/mchien2002/oven-assessment.git
cd oven-assessment

```

### 2. Tạo virtual env & cài package

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

### 3. Chạy với Docker (Khuyên dùng)

```bash
docker-compose up -d

```

### 5. Chạy server

> ⚠️ **Note**: Nếu muốn chạy trên local phải chỉnh sửa thuộc tính `HOST` trong file `config.json` từ `db -> localhost.`

```bash
uvicorn djangoapp.asgi:application --workers 1 --host 0.0.0.0 --port 3000

```

### 6. Truy cập

-   API root: `http://127.0.0.1:3000/`
    
-   Swagger: `http://127.0.0.1:3000/api-docs/`
    

----------

## 6. Chạy Unit Test

```bash
pytest

```
    
----------

## 7. Giới hạn hiện tại

-   Upload hiện tại chỉ lưu file vào **local filesystem** (chưa tích hợp AWS S3).
    
-   Hashmap metadata mới chỉ lưu trong bộ nhớ (chưa persist vào DB).
    
-   Authentication chưa triển khai (ngoài phạm vi yêu cầu).
    

----------

## 8. Tác giả

👨‍💻 Developed by **[Your Name]**  
📧 Email: [minhchien77777@gmail.com](mailto:minhchien77777@gmail.com)  
📂 Github: [My Github](https://github.com/mchien2002)

