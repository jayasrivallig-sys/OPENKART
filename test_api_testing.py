from datetime import datetime, timedelta

from faker import Faker
from playwright.sync_api import Playwright
import faker

import json

def test_apitesting(playwright:Playwright):
    baseurl = "https://restful-booker.herokuapp.com"
    request_context = playwright.request.new_context()

    #hard coded data
#     request_body ={
#     "firstname" : "Jim",
#     "lastname" : "Brown",
#     "totalprice" : 111,
#     "depositpaid" : True,
#     "bookingdates" : {
#         "checkin" : "2018-01-01",
#         "checkout" : "2019-01-01"
#     },
#     "additionalneeds" : "Breakfast"
# }

    #json
    # file = open("D:/PLAYWRIGHT/OPENKART/tests/jsondata.json",'r')
    # request_body = json.load(file)

    #FAKER
    faker = Faker()
    first_name = faker.first_name()
    last_name = faker.last_name()
    total_price = faker.random_int(min=100, max=500)
    deposit_paid = faker.boolean()
    checkin = datetime.now().strftime("%Y-%m-%d")
    checkout = (datetime.now() +timedelta(days=5)).strftime("%Y-%m-%d")
    additional_needs = faker.word()

    request_body = {
            "firstname" : first_name,
            "lastname" : last_name,
            "totalprice" : total_price,
            "depositpaid" : deposit_paid,
            "bookingdates" : {
                "checkin" : checkin,
                "checkout" : checkout
            },
            "additionalneeds" : additional_needs
        }

    response = request_context.post(f"{baseurl}/booking", data = request_body)
    assert response.ok
    assert response.status==200

    response_body = response.json()
    print(response_body)

    assert "bookingid" in response_body
    assert "booking" in response_body

    booking = response_body["booking"]
    assert booking["firstname"] == first_name
    assert booking["lastname"] ==last_name
    assert booking["totalprice"] ==total_price
    assert booking["depositpaid"] is deposit_paid
    assert booking["bookingdates"]["checkin"] == checkin
    assert booking["bookingdates"]["checkout"] == checkout
    assert booking["additionalneeds"] == additional_needs

    request_context.dispose()

