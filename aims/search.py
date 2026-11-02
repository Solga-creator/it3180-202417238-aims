"""Tìm DVD trong danh sách."""


def search_by_category(items, keyword):
    """Trả về các DVD có `keyword` trong category (không phân biệt hoa thường)."""
    key = keyword.lower()
    return [dvd for dvd in items if key in dvd.category.lower()]


def search_by_title(items, keyword):
    """Trả về các DVD có `keyword` xuất hiện trong title (không phân biệt hoa thường)."""
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
