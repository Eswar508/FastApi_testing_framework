from utils.helper_fun import get_token
class StudentData:
    own_id=7
    invalid_id=1000
    student_expected_data={
        "user_id": 7,
        "name": "studentA",
        "age": 18,
        "gender": "male",
        "email": "student1@gmail.com",
        "cgpa": 8.0
    }
    @classmethod
    def student_id(cls):
        return [(cls.own_id,cls.student_expected_data)]
    student_id2=8
    update_id=9    
    patch_id=9
    delete_id1=10 
    deleted_id2=11  
    #deleted_id3=12   
    @classmethod
    def delete_token1(cls):
        data={
            "email":"student7@gmail.com",
            "password":"$Student7"
        }
        return get_token(data)
    @classmethod
    def delete_token2(cls):
        data={
            "email":"student8@gmail.com",
            "password":"$Student8"
        }
        return get_token(data)
    admin_patch_permission={"name":"admin patch","email":"adminpatchpermission@gmail.com"}
    self_update_permission={
          "name": "self update",
          "age": 18,
          "gender": "male",
          "email": "updatepermission@gmail.com",
          "cgpa": 8.0
         }
    other_update_permission={
          "name": "other update",
          "age": 18,
          "gender": "male",
          "email": "otherpermission@gmail.com",
          "cgpa": 8.0
         }
    admin_workflow_update={
          "name": "updated Student",
          "age": 18,
          "gender": "male",
          "email": "updatedstudent@gmail.com",
          "cgpa": 8.0
         }
    student_workflow_update={
          "name": "updated Student",
          "age": 18,
          "gender": "male",
          "email": "updatedstudent@gmail.com",
          "cgpa": 8.0
         }
    patched_schema={"name":"patched schema","email":"schemapatch@gmail.com"}
    updated_schema={
          "name": "updated Schema",
          "age": 18,
          "gender": "male",
          "email": "updatedschema@gmail.com",
          "cgpa": 8.0
         }
    schema_patch_me={"name":"schema patch me","email":"schemapatchme@gmail.com"}
    schema_update_me={
          "name": "schema update me",
          "age": 18,
          "gender": "male",
          "email": "schemaupdateme@gmail.com",
          "cgpa": 8.0
         }
    patch_email={"email":"patchme12@gmail.com"}
    patch_name={"name":"patch me"}
    path_multi={"name":"multi patchme","age":18}
    patch_invalid_name={"name":"patch_me1"}
    patch_invalid_email={"email":"patchme12gmail.com"}
    patch_duplicate_name={"name":"studentB"}
    update_me={
          "name": "studentEE",
          "age": 19,
          "gender": "female",
          "email": "student55@gmail.com",
          "cgpa": 7.5
     }
    update_invalid_name={
          "name": "$tudent",
          "age": 19,
          "gender": "female",
          "email": "student56@gmail.com",
          "cgpa": 7.5
     }
    update_invalid_email={
          "name": "studentEG",
          "age": 19,
          "gender": "female",
          "email": "student57@gmailcom",
          "cgpa": 7.5
     }
    update_duplicate_name={
          "name": "studentB",
          "age": 19,
          "gender": "female",
          "email": "student58@gmail.com",
          "cgpa": 7.5
     }
    id_patch_email={"email":"idpatch12@gmail.com"}
    id_patch_name={"name":"id patch"}
    id_pathc_multi={"name":"id multi patch","age":20}
    id_patch_invalid_name={"name":"id_patch1"}
    id_patch_invalid_email={"email":"id_patch12gmail.com"}
    id_patch_duplicate_name={"name":"studentB"}
    id_update={
          "name": "studentGE",
          "age": 19,
          "gender": "female",
          "email": "student75@gmail.com",
          "cgpa": 7.5
     }
    id_update_invalid_name={
          "name": "$tudenT",
          "age": 19,
          "gender": "female",
          "email": "student76@gmail.com",
          "cgpa": 7.5
     }
    id_update_invalid_email={
          "name": "studentGG",
          "age": 19,
          "gender": "female",
          "email": "student77@gmailcom",
          "cgpa": 7.5
     }
    id_update_duplicate_name={
          "name": "studentB",
          "age": 19,
          "gender": "female",
          "email": "student78@gmail.com",
          "cgpa": 7.5
     }