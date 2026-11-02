# Use case — AIMS-mini

Người dùng (khách hàng) thao tác trên giỏ hàng DVD.

```text
                    AIMS-mini
  (Khách hàng) ---- add DVD to cart
               ---- remove DVD from cart
               ---- print cart
               ---- search DVD by title
               ---- view total cost
```

## Tác nhân
- Khách hàng: thêm/xóa đĩa, xem giỏ, tìm theo tiêu đề.

## Use case chính
1. **Thêm DVD vào giỏ** — hệ thống kiểm tra giới hạn 20 đĩa.
2. **Xóa DVD khỏi giỏ** — nếu đĩa không có, báo lỗi.
3. **In giỏ hàng** — giỏ trống in `The cart is empty`.
4. **Tìm theo tiêu đề** — `search_by_title(items, keyword)`.
5. **Xem tổng tiền** — `total_cost()`.
