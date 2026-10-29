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
    access_token = response_body["access_token"]
    print(access_token)

    course_response = api_context.get(
        "/oauthapi/getCourseDetails",
        params={
            "access_token": access_token
        }
    )
    course_response_body = course_response.json()
    print(course_response_body)
    assert course_response_body["instructor"] == "RahulShetty"