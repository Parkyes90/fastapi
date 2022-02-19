from typing import Optional, List

from fastapi import APIRouter, status, Header, Cookie
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router = APIRouter(prefix="/products", tags=["products"])
products = ["watch", "camera", "phone"]


@router.get("")
def list_products():
    response = Response(content=" ".join(products), media_type="text/plain")
    response.set_cookie(key="session_id", value="session")
    return response


@router.get("/header")
def products_with_header(
    response: Response,
    header: Optional[List[str]] = Header(None),
    session_id: Optional[str] = Cookie(None),
):
    if header:
        response.headers["custom-response-header"] = ", ".join(header)
    return {"data": products, "header": header, "session_id": session_id}


@router.get(
    "/{product_id}",
    responses={
        status.HTTP_200_OK: {
            "content": {"text/html": {"example": "<div>Product</div>"}},
            "description": "Returns the HTML for the object",
        },
        status.HTTP_404_NOT_FOUND: {
            "content": {
                "text/plain": {"example": "Product not available"},
            },
            "description": "A cleartext error message",
        },
    },
)
def retrieve_product(product_id: int):
    if product_id > len(products):
        return PlainTextResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content="Product not available",
            media_type="text/plain",
        )

    product = products[product_id]
    output = f"""
    <head>
    <style>
    .product {{
        width: 500px;
        height: 30px;
        border: 2px inset green;
        background-color: lightblue;
        text-align: center;
    }}
    </style>
    </head>
    <div class="product">{product}</div>
    """
    return HTMLResponse(content=output, media_type="text/html")
