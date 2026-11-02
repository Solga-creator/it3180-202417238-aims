# Câu hỏi thảo luận Lab 03

## Merge base là gì?

Merge base là commit tổ tiên chung mới nhất của hai đầu nhánh (`git merge-base A B`). Git so sánh từng nhánh với merge base để tính diff khi merge. Hai nhánh cùng sửa một dòng so với merge base thì xung đột. Ở Lab 03, merge base của `feature/vietnamese-messages` và `master` (sau PR #13) là commit trước khi hai bên đổi `print` trong `add_dvd`.

## Vì sao `master` / `release/*` phải dùng revert?

`reset` dời con trỏ nhánh và viết lại lịch sử. Trên nhánh đã chia sẻ, reset (kèm force-push) xóa commit người khác đã kéo về. `revert` tạo commit mới đảo ngược thay đổi, lịch sử vẫn tuyến tính/còn đủ, có thể review qua PR. Baseline (`master`, `release/*`) chỉ nhận thay đổi có kiểm soát, nên hoàn tác cũng phải là commit mới — không được `reset --hard` rồi đẩy đè.

Ghi chú đánh số Issue: slide dùng `#6`, nhưng GitHub dùng chung dãy số cho Issue và Pull Request. Issue giỏ hàng 21 đĩa trên repo này là **#8**; PR sửa là **#9** với `Fixes #8`.
