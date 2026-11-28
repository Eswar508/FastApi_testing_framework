import pytest
import shutil
from pathlib import Path
from api_client.auth_client import *
from api_client.student_client import delete_student_account
from api_client.auth_client import login_client
from utils.helper_fun import get_token

@pytest.fixture(autouse=True)
def reset_api_storage():
    project_root=Path(__file__).parent
    data_files=(
        (project_root/"Fast_Api"/"clean_up"/"registry.json",
         project_root/"Fast_Api"/"FastApi"/"storage"/"user_registry.json"),
        (project_root/"Fast_Api"/"clean_up"/"ids.json",
         project_root/"Fast_Api"/"FastApi"/"storage"/"user_ids.json"),
        (project_root/"Fast_Api"/"clean_up"/"password.json",
         project_root/"Fast_Api"/"FastApi"/"storage"/"user_passwords.json"),
    )
    for seed,storage in data_files:
        shutil.copyfile(seed,storage)
    yield
    for seed,storage in data_files:
        shutil.copyfile(seed,storage)

@pytest.fixture(scope="session")
def admin_update_token():
    data={"email":"admin2@gmail.com","password":"$AnAdmin2"}
    return get_token(data)
@pytest.fixture(scope="session")
def student_update_token():
    data={"email":"student4@gmail.com","password":"$Student4"}
    return get_token(data)
@pytest.fixture(scope="session")
def admin_token():
    data={"email":"admin1@gmail.com","password":"$AnAdmin1"}
    return get_token(data)
@pytest.fixture(scope="session")
def student_token():
    data={"email":"student1@gmail.com","password":"$Student1"}
    return get_token(data)
@pytest.fixture(scope="function")
def deleted_id(admin_token):
    id=12
    delete_student_account(admin_token,id)
    return id
@pytest.fixture(scope="function")   
def deleted_token():
    payload={
            "email":"student9@gmail.com",
            "password":"$Student9"
        }
    token=get_token(payload)
    delete_student_account(token)
    return token