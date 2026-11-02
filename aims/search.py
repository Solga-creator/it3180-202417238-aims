"""Tìm DVD trong danh sách theo tiêu đề."""


def search_by_title(items, keyword):
    """Trả về các DVD có `keyword` xuất hiện trong title (không phân biệt hoa thường)."""
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
