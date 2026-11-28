from api_client.student_client import get_student_account
from test_cases.student_data import StudentData
def test_get_student_me(student_token):
    expected_data=StudentData.student_expected_data
    get_response=get_student_account(student_token)
    assert get_response.status_code==200
    json_response=get_response.json()
    assert json_response["name"]==expected_data["name"]
    assert json_response["email"]==expected_data["email"]
    assert json_response["user_id"]==expected_data["user_id"]