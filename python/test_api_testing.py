from urllib import request
from playwright.sync_api import sync_playwright, expect


def test_api_get(playwright):
    request_context = playwright.request.new_context(
                         extra_http_headers ={
                             "Accept" : "application/json",
                              "Authorization" : "Bearer ",
                                "X-Api-Key" : "reqres-free-v1"})


    response = request_context.get("https://reqres.in/api/users?page=2'")
    assert response.status ==401
    json_data = response.json()
    print(json_data)
    assert json_data["id"] ==3
    request_context.dispose()