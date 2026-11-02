# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-11-02

### Added
- `Cart.sort_by_title()` and `Cart.sort_by_cost()`
- `search_by_category()` in `aims/search.py`


## [1.0.1] - 2026-11-02

### Fixed
- `search_by_title` is case-insensitive (`lion` finds The Lion King)

## [1.0.0] - 2026-11-02

### Added
- Package layout `aims/` (DVD, Cart) and demo `main.py`
- `Cart.print_cart()` (empty cart prints `The cart is empty`)
- `search_by_title()` in `aims/search.py`
- `Cart.total_cost_with_discount(percent)` with validation
- Pull request template, use case notes, and lab discussion answers
- Unit tests for cart limit and discount

### Fixed
- Cart accepted the 21st DVD although the limit is 20 (#8)
- Discount used `total * percent / 100` instead of remaining amount after percent off
- Add-to-cart message conflict: keep Vietnamese wording and DVD title

### Changed
- Add-to-cart message: `Đã thêm đĩa '{title}' vào giỏ hàng`
