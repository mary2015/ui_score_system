from pages.score_page import ScorePage
import pytest
import allure


@pytest.mark.usefixtures('driver')
class TestScorePage:
    @allure.step("postive test case: valid input")
    @pytest.mark.parametrize("name,email,score", [("Mary", "mary@qq.com", 100)])
    @pytest.mark.parametrize("role", ["Teacher", "Student", "Helper"])
    def test_submit_valid_input(self, driver, name, email, score, role):
        page = ScorePage()
        page.submit_input(driver, name, email, score, role)
        # assert

    @allure.step("Negative test case: invalid score")
    @pytest.mark.parametrize("name,email,role", [("Mary", "mary@qq.com", "Helper")])
    @pytest.mark.parametrize("score", ["", -1, 101])
    def test_submit_invalid_score(self, driver, name, email, score, role):
        page = ScorePage()
        page.submit_input(driver, name, email, score, role)
        # assert

    @allure.step("Negative test case: invalid email")
    @pytest.mark.parametrize("name,score,role", [("Mary", 100, "Helper")])
    @pytest.mark.parametrize("email", ["@123.com", "12@", ""])
    def test_submit_invalid_email(self, driver, name, score, role, email):
        page = ScorePage()
        page.submit_input(driver, name, email, score, role)
        # assert

    @allure.step("Negative test case: invalid name")
    @pytest.mark.parametrize("name,score,email,role", [("", 100, "mary@qq.com", "Helper")])
    def test_submit_invalid_name(self, driver, name, email, score, role):
        page = ScorePage()
        page.submit_input(driver, name, email, score, role)
        # assert

    def test_submit_without_input(self, driver):
        page = ScorePage()
        page.submit_without_input(driver)
        # assert
