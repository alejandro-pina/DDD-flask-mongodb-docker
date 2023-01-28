QUERY_NAME = 'page'
END_POINT = '/api/user'


def get_total_pages(per_page: int, total: int) -> int:
    pages = int(total / per_page)
    nex_page = 1 if (total % per_page) >= 1 else 0
    total_pages = pages + nex_page
    return total_pages


def back_to(page: int, per_page: int, total: int, sort_field: str, order_by: str) -> dict:
    query_back = "/"
    pages = get_total_pages(per_page, total)
    if (page - 1) == (pages + 1):
        query_back = "/?page="+str(page - 1)
        query_back += "&order_by="+order_by
        query_back += "&sort_field="+sort_field

    return query_back


def pagination(page: int, per_page: int, count_item: int, total: int) -> dict:
    pages = get_total_pages(per_page, total)
    prev_page = (page - 1) if page > 1 else ""
    next_page = page + 1 if page <= pages else ''

    return {
        "endpoint"   : END_POINT,
        "query"      : QUERY_NAME,
        "page_number": page,
        "p_prev"     : prev_page,
        "p_next"     : next_page,
        "per_page"   : per_page,
        "pages"      : (pages + 1),
        "total"      : total,
        "count_item" : count_item
    }
