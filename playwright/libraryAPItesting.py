from playwright.sync_api import Playwright

data = {


"name":"Learn Appium Automation with Java",
"isbn":"bcdzz",
"aisle":"22777",
"author":"John foe"
}






def test_add_a_book(playwright:Playwright):
    api_context = playwright.request.new_context(base_url= "http://216.10.245.166")
    response = api_context.post("Library/Addbook.php", data = data)
    assert response.ok
    response_body = response.json()
    print(response_body)
    book_id = response_body["ID"]
    return book_id







def test_delete_a_book(playwright:Playwright):
    id_for_book = test_add_a_book(playwright)
    api_request_context = playwright.request.new_context(base_url= "http://216.10.245.166")
    response = api_request_context.post("/Library/DeleteBook.php", data = {"ID" : id_for_book})
    assert response.ok
    print(response.status)
    response_body = response.json()
    print(response_body["msg"])