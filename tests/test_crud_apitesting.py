from playwright.sync_api import Playwright
import pytest
import json

baseurl = "https://restful-booker.herokuapp.com"

def read_json(file_path):
    file = open(file_path,'r')
    return json.load(file)

@pytest.fixture
def request_context(playwright:Playwright):
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()

def test_post_create_booking(request_context):
    data = read_json("D:/PLAYWRIGHT/OPENKART/tests/jsondata.json")
    response = request_context.post(f"{baseurl}/booking", data = data)

    assert response.ok , "Post request failed"
    assert response.status==200

    response_body = response.json()
    print(response_body)

    assert "bookingid" in response_body
    assert "booking" in response_body

    booking = response_body["booking"]
    assert booking["firstname"] == data["firstname"]
    assert booking["lastname"] == data["lastname"]
    assert booking["totalprice"] == data["totalprice"]
    assert booking["depositpaid"] == data["depositpaid"]
    assert booking["bookingdates"] ["checkin"]== data["bookingdates"]["checkin"]
    assert booking["bookingdates"] ["checkout"]== data["bookingdates"]["checkout"]

    global bookingid
    bookindid = response_body["bookingid"]

def test_get_bookingdetails(request_context):
    response=request_context.get(f"{baseurl}/booking/{bookingid}")
    assert response.ok
    assert response.status == 200

    response_body = response.json()
    print(f"Booking details of bookingid {bookingid}" , response_body)
    assert "firstname" in response_body
    assert "lastname" in response_body

