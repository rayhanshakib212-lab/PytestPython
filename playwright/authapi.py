from playwright.sync_api import Playwright

def test_get_token(playwright:Playwright):

    api_context = playwright.request.new_context(base_url = "https://rahulshettyacademy.com")

    response = api_context.post("/oauthapi/oauth2/resourceOwner/token",
                                form={
                                    "client_id": "692183103107-p0m7ent2hk7suguv4vq22hjcfhcr43pj.apps.googleusercontent.com",
                                    "client_secret": "erZOWM9g3UtwNRj340YYaK_W",
                                    "grant_type": "client_credentials",
                                    "scope": "trust"
                                  }
                                  )
    assert response.ok
    response_body = response.json()
    print(response_body)