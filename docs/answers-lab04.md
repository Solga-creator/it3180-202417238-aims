# Câu hỏi thảo luận Lab 04

## Vì sao `release/*` không merge vào `master`? So sánh với GitFlow.

`release/*` là dòng bảo trì của một baseline đã đóng băng. Merge ngược vào `master` sẽ kéo theo bump phiên bản PATCH (ví dụ 1.0.1) và có thể đụng MINOR đang phát triển trên `master` (1.1.0). Thay đổi từ release đưa về `master` bằng cherry-pick từng commit sửa lỗi.

GitFlow có `develop` + `main`/`master`: nhánh `release/*` merge vào cả hai khi phát hành. Release Flow của học phần không có `develop`; `master` là nơi tích hợp, `release/labXX` là bản nộp/bảo trì theo tuần, nên không merge release trở lại master.

## Vì sao lên 1.0.0 mà không phải 0.4.0?

SemVer `0.y.z` là giai đoạn đầu, API chưa ổn định. Tag `v0.1.0`–`v0.3.0` đánh dấu Lab 01–03. Lab 04 đóng gói sản phẩm đủ dùng (giỏ hàng, tìm kiếm, giảm giá, test, CHANGELOG) nên đánh `1.0.0`: từ đây PATCH = hotfix, MINOR = thêm tính năng tương thích.
