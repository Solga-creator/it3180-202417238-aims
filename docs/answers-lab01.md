# Câu hỏi thảo luận Lab 01

## Vì sao dùng `git mv`?

`git mv` vừa đổi tên tệp trên đĩa vừa ghi nhận rename trong index. Git vẫn có thể lần lịch sử qua đổi tên (`git log --follow`). Trên Pull Request, tab Files changed hiện *renamed* chứ không phải xóa một tệp và thêm tệp khác, nên reviewer thấy đây là tái cấu trúc, không phải viết lại mã.

## `release/lab01` có phải baseline không?

Có. Baseline là phiên bản đã thống nhất, chỉ đổi qua quy trình. Nhánh `release/lab01` cắt từ `master` sau khi PR #1 đã merge; đó là bản nộp Lab 01. Các sửa sau phải đi nhánh mới / hotfix, không sửa tùy tiện trên baseline.

## Vì sao không commit thẳng `master` dù làm một mình?

Release Flow cấm commit trực tiếp lên `master` và `release/*`. Mọi thay đổi đi qua Pull Request để còn mô tả, kiểm thử và lịch sử review. Làm một mình vẫn tạo PR (có thể tắt yêu cầu approval) để giữ đúng quy trình SCM: thay đổi được kiểm soát trước khi vào baseline.
