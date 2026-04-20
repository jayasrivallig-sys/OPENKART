page.get_by_role("button", name = "Submit").click()

page.get_by_role("checkbox", name = "maths").check()

page.get_by_role("heading", name = "welcome").to_be_visible()

page.get_by_label("Enter name :", ).fill("jayasri")

page.get_by_text("enter the number", exact = True)

page.get_by_alt_text("image").click()


//div[contains(@class , "header")]

//button[text() = "welcome"]

//input[starts-with(@id ,  "user")][1]

days = ["s", "m","t", "w"], "th", "f", "sat"]
checkbox = []

for days in days:
    checkbox = page.get_by_label(day)
    print("total days", len(checkbox))

for i in checkbox[2:]
    i.check()
    expect(i).to_be_checked()


indexes = [2,3,4]
    for i in indexes:
    checkbox[i].check()

days = ["s", "m","t", "w"], "th", "f", "sat"]
weekday = "f"
for i in days:
    if i = weekday:
    checkbox = page.get_by_label(i).check()

page.get_by_label(" verify").select_option(label = "Red")(index = 4)

product = page.locator("").inner_text()
print(product)
len(product)

product_names = [text.strip() for text in product.all_text_contents()

all_products = page.loctor(title, price, lg)
name_procts = all_products.all()
print(name_procts)

for prods in name_procts:
    prods(prods.inner_text())

selected_items = page.locator().select_option()
for i in selected_items:
    print("items" , i.count())

selected_items = page.locator().all_inner_texts()
print(len(selected_items))

selected_items.count()

next_button = page.locator("")
is_disabled = next_button.get_attribute("disabled")
if is_not_disabled is disables:
    next_button.click()
else:
    print("next button is disabled")
print(next_button)

all_rows = table.locator("tr").all()
rowcounr = not all_rows.count()


page.on("dialog" lambda : dialog , dialog.dismiss or accept)
page.locator().click()

x = lambda a,b,c : a*b*c
print(x(2,3,4))

frames = page.franes
pront(len(frames))

page.frame("name of prage")
page.frame.locator("")
page.frame(url = "")
input = frame.locator("")
input.fill("")

frame3 = page.frane(url = "")
frame3.locator("").fil()

child_frame = fram3.child_frame
print(len(child_frame))

inner_farne = child_frame[2]
radio = inner_farne.get_by_label("")
radio.check()


m1 = page.locator("").nth(1).hover
m2 = page.locator("").nth(2).click()
m3 = page.get_by_role("button" , name = "maths").dblclick()
m4 = page.get_by_role("button", name = "eng").click()
m5 = page.get_by_text("eng").click(button = "right")
m6 = page.get_by_text("eng").click(button = "middle")

sourse = page.locator("")
dest = page.locator("")
sourse.drag_to(dest)
pront(target.inner_text())

path_to_upload_file = page.locator("").set_input_files(path = "")
file_to_be_uploaded = page.get_by_role("button", name = "Upload").click

dowenload file with lambda
import os
page.on("download", lambda download : download.save_as("path"))
page.locator.click()
if os.path.exists("path"):
    print("path exists")
else:
    print("path does not exist")

page.on("popup", lambda popup : popup.wait_for_state_load())

browser = p.chromium.launch(headless = False)
context = browser.new_context(http_credentials={"user_name" : "admin" ,
                                                "password" : "password"})
page = context.new_page()
all_popups = context.pages()
print(len(all_popups))

for i in all_popups:
    print(i.url())
    print(i.title())
title = i.title()
all_popups[0].title()

page1 = context.new_page()
page2 = context.new_page()

page1.goto("url")
page2.goto("url")

page.screenshot(path ="")
page.screenshot(path ="", fullpage = True)
page.locator("").screenshot(path = "")


pytest.in

[pytest]
addopts = --screenshot-on
                        -only-on-failure
                        -on-first-failure
                        -off
        -- video-on
                -off
                -retain-on-failure
                -on-first-retry
        --tracing - on
                -off
                -retain-on-failure


video
context = browser.new_context(record_video_dir="path",
                              record_video_size ={"width" : 1024,
                                                  "height" : 768}

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

page.screenshot(path = f"screenshort/homepage_{timestanp}.png")

tracing
context.tracing.start(screenshot = True, snapshots = True)
context.tracing.stop(path = "trace.zip")
playwright show-trace trace.zip


flaky test - rerun/retries (rerun  - only failed test)
pip install pytest --reruns failures
pytest path --headed --reruns 3 --reruns-delay-2

--last-failed





import pytest

test_data = [("email1@abc.com", "password1", "valid"),
            "(email2@abc.com", "password2""invalid"),
                ("", "", "invalid")]

@pytest.mark.parametroize("email", "password", "validity", test_data)
test_parametrize_login(page, email, password, validity)
page.goto("")
page.locator("").fill(email)
page.fill("", password)


import json
file = open((path = "", "r"))
login_data = json.load(file)
import pytest

@pytest.mark,parametrize("email, password, validity"
                        [data["email"], data["password"], data["validity"]
                         for data in login_data)]
def test_login_param(page, email, password, validity):


import pytest
test_data = [("validmeail@gmi.com", 'p1, "valid')
             ("invalid@gm.com", "p2", "invalid")]
@pytest.mark.parametrize("email, password, validity", test_data)
def test_logindata_param(page, email, password, validity):
    page.goto("")
    page.locator.fill(email)
    page.fill("", password)
    page.locator("").click()

import pytest,json
file = open(path = "", 'r')
login_details = json.load(file)
@pyest.mark.parametroze("email, password, validity", [(data["email"],data["password"], data["validity"]) for data in login_details])
def test_json_login_param(page, login, email, validity):


import csv, pytest
data =[]
file = open("path of csv file")
reader = csv.DictReader(file)
for row in reader:
    data.append((row["email"],
                 row["password"],
                 row["validity"]))
@pytest.mark.parametrize("email, password, validity", data)
test_parm(page, email, password, validity):


imprt csv, pytest

login_data = []
file = open("path of csv")
reader = csv.DictReader(file)
for row in reader:
    login_data.append(row["email"],
               row["password"],
               row["validity"]))

import pytest, openpyxl
data = []
file = openpyxl.load_workbook("path")
sheet = workbook.active
for row in sheet.iter_row(min_row-val_value =2, values_only = True):
for row in sheet.iter_row(min_row = 2, values_only = True):
    email, password, validity = row
    data.append((str(email or "")),
    str(password or ""),)
    str(validity or ""))
    workbook.close


import pytest, openpyxl
data =[]
file = openpyxl.load_workbook("path")
sheet = workbook.active
for row in sheet.iter_rows(min_row = 2, values_only = True):
    email, password, validity = row
    row.append((str(email or ""), str(password or ""), str(validity or "")))
    worksheet.close()
@pytest.mark.parametrize("email, password, validity", data)
    def test_login_excal(page, email, password, validity)


HTML reports
pip install pytest-html
[pytest]
addopts == --html=myreport.html --self-contained-html(css and js into one file combined)
                                --capture=tee-sys(dispalys logs in console and report)

pip insatll allure-Pytest
https://github.com/allure-framework/allure2/release , dowmload latest zip fiule, swetup java bin evnv path
[pytest]
addopts ==--alluredir=reports/allure-results

runtime = allure serve reports/allure-results
permantent = allure generate reports/allure-reports -o reports/allure-reports\
open manually - allure open reports/allure-report