from playwright.sync_api import sync_playwright,Playwright, expect

def test_practise_automation(playwright :Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    # page1.goto("https://www.pavantestingtools.com/")
    expect(page).to_have_url("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page).to_have_title("Automation Testing Practice: PlaywrightPractice")


    # page.get_by_role("button", name="Primary Action").click()
    # page.get_by_role("button", name="Toggle Button").click()
    # page.locator("//input[@id= 'username']").fill("Jayasri", timeout=1500)
    # accpet_terms = page.get_by_label("Accept terms", exact=True).click(timeout=15000)
    # expect.soft(accpet_terms).to_be_checked(timeout=15000)
    # page.locator("li", has_text='Home').first.click()
    # page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    # page.get_by_role("alert", name='                     This is an important alert message!                 ',
    #                  exact=True)
    # page.get_by_label("Standard").click()
    # page.get_by_placeholder("Enter your full name").fill("Jayasri")
    # page.get_by_role("button", name="Search").click()
    # logo = page.get_by_alt_text("logo image")
    # expect(logo).to_be_visible(timeout=2000)

    # path = page.locator("#singleFileInput").set_input_files('D:\PLAYWRIGHT\OPENKART\python\samplefile.txt',timeout=3000)
    # upload = page.get_by_role("button", name="Upload Single File").click()
    # expect(page.locator("#singleFileStatus")).to_be_visible()
    # # expect(file_upload_confirm).to_be_visible(timeout=4000)
    # expect(page.locator("#singleFileStatus")).to_contain_text("Single file selected:")

    # path2= page.locator("#multipleFilesInput").set_input_files(['D:/PLAYWRIGHT/OPENKART/python/dummy.txt', 'D:/PLAYWRIGHT/OPENKART/python/samplefile.txt', 'D:/PLAYWRIGHT/OPENKART/python/test.txt'])
    # upload_mutli = page.get_by_role("button", name="Upload Multiple Files").click()
    # expect(page.locator("//p[@id='multipleFilesStatus']")).to_be_visible()

    # table =page.locator("//table[@name='BookTable']")
    # row = table.locator("tr")
    # expect(row).to_have_count(7)
    # row_count = row.count()
    # print("row are :", row_count)
    # row_all = table.locator("tr").all()

    # row_elements = row.all_inner_texts()
    # print(row_elements)
    # for i in row_elements:
    #     print(i)

    # row_elements_count = row.nth(5).locator("td")
    # row_elements_name = row_elements_count.all_inner_texts()
    # print(row_elements_name)

    # table_heading = page.locator("//table[@name='BookTable']//tr//th")
    # print(table_heading.all_inner_texts())

    # next_button = page.locator("//li//a[text() = '2']")
    # next_button.click(timeout=19000)

    # page.on("dialog", lambda dialog :dialog.accept())
    # simple_alert = page.get_by_role("button", name="Simple Alert").click(timeout=5000)
    #
    # page.on("dialog", lambda dialog: dialog.dismiss())
    # confirm_alert = page.get_by_role("button", name="Confirmation Alert").click(timeout=5000)

    # page.on("dialog", lambda dialog: dialog.accept("times of india"))
    # prompt_alert = page.get_by_role("button", name="Prompt Alert").click(timeout=4000)
    # msg_locator = page.locator("#demo")
    # expect(msg_locator).to_contain_text("Hello")

    # new_tab = page.get_by_role("button", name="New Tab")
    # new_tab.click(timeout=4000)
    # page1 = context.new_page()
    # expect(page1).to_have_url("https://www.pavantestingtools.com/")

    # mouse_hover = page.get_by_role("button", name="Point Me").hover()
    #
    # mouse_click = page.get_by_role("link", name="Mobiles").click()
    # # mouse_rightclick = page.get_by_role("link", name="Mobiles").click(button="right")
    # # mouse_middleclick = page.get_by_role("link", name="Mobiles").click(button="middle")
    # # double_click= page.get_by_role("link", name="Mobiles").dblclick()
    #
    # sourse = page.get_by_text("Drag me to my target", exact=True)
    # dest = page.get_by_text("Drag me to my target", exact=True)
    # sourse.drag_to(dest)

    list_textbox = page.get_by_role("textbox", name="Select an item").click(timeout=10000)
    item_to_select= page.get_by_text("Item 5", exact=True).click()



