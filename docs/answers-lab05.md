# Câu hỏi thảo luận Lab 05

## Ưu, nhược điểm của upstream first so với release first?

**Upstream first** (sửa trên `master` rồi cherry-pick sang `release/*`): một lần sửa trên dòng đang phát triển, giảm lệch mã nguồn. Nhược: bản đã phát hành (`v1.0.0`) chưa được vá cho đến khi cherry-pick xong; dễ quên một dòng release.

**Release first** (học phần): hotfix tạo từ đúng bản khách đang dùng (`origin/release/lab04`), phát hành PATCH `v1.0.1` ngay, rồi cherry-pick `-x` sang `master` và `release/lab05`. Ưu: vá đúng phiên bản đang chạy. Nhược: commit bump phiên bản (1.0.1) không được merge nguyên nhánh vào master (xung đột 1.1.0), phải tách commit sửa lỗi.

## Nếu quên lan truyền sang `release/lab05`, lệnh nào ở Phần F phát hiện?

`git cherry -v origin/master origin/release/lab04` so sánh patch; chưa đủ nếu quên lab05.

Vòng kiểm tra hành vi:

```
for ref in v1.0.1 v1.1.0 master; do ... search_by_title(..., "lion") ...
```

Nếu quên lab05 thì `v1.1.0` (gắn trên `release/lab05`) in `0` thay vì `1`.

`git log --all --grep "cherry picked from commit <FIX_SHA>"` phải ra **2** commit (master + lab05). Thiếu một dòng là chưa lan truyền đủ.

Ghi chú số Issue: slide dùng `#20`; trên repo này Issue là **#21** vì Pull Request chiếm chung dãy số.
