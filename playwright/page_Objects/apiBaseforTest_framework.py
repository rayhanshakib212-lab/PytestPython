from urllib import response
from playwright.sync_api import Playwright, Request


payload =  {"orders": [ { "country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}

class APIUtils:
    def getTokenframworktest(self,playwright:Playwright, user_credentials):
       user_email = user_credentials['userEmail']
       user_password = user_credentials['userPassword']
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response_new = api_request_context.post("https://rahulshettyacademy.com/api/ecom/auth/login",
            data = {"userEmail": user_email, "userPassword": user_password})
        assert response_new.ok
        print(response_new.json())
        responseBody = response_new.json()
        return responseBody["token"]







    def createOrderframworktest(self, playwright:Playwright, user_credentials):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client/")
        response_new= api_request_context.post("/api/ecom/order/create-order",
                                data= payload,
                                headers={"Authorization": token,
                                         "Content-Type": "application/json"
                                         })

        print(response_new.json())
        response_body = response_new.json()
        orderId = response_body["orders"][0]
        return orderId