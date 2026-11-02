# Câu hỏi thảo luận Lab 02

## Vì sao phải đồng bộ `master` trước khi gửi PR?

Nhánh tính năng thường tạo từ `master` cũ. Trong lúc đó `master` đã nhận PR khác (ví dụ `print_cart`). Nếu gửi PR khi chưa đồng bộ, reviewer xem diff thiếu ngữ cảnh, CI chạy trên mã lệch, và GitHub có thể báo conflict. `git fetch` rồi `git merge origin/master` (hoặc rebase) trên nhánh của mình, chạy lại chương trình, rồi mới push — đó là tích hợp sớm, đúng kiểm soát thay đổi.

## Khi nào không được rebase?

Không rebase commit **đã chia sẻ** (đã push, người khác dựa vào). Rebase đổi SHA; người khác phải `--force` theo, dễ mất commit. Trên `master` / `release/*` tuyệt đối không rebase. Rebase chỉ dùng cho commit chưa push, hoặc nhánh riêng của mình trước khi người khác dựa vào (và khi bắt buộc cập nhật nhánh đã push thì `--force-with-lease`, không `--force`).

## `feature/*` khác `topic/*` ra sao?

- `feature/*`: thay đổi **hành vi sản phẩm** (mã nguồn, test). Ví dụ `feature/cart-print`, `feature/search-by-title`.
- `topic/*`: thay đổi **không phải tính năng chạy** — tài liệu, template, cấu hình quy trình. Ví dụ `topic/pr-template`, `topic/use-case-diagram`.

Cả hai đều đi PR vào `master`, không commit thẳng.
