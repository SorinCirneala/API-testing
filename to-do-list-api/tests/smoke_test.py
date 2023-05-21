import sys, os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_path)

import actions
from locators import USER_ID

# check if the API is responding
def test_api_response():
    response = actions.check_root_endpoint()
    assert response.status_code == 200

# create a task, check if the task exists, has the correct content
def test_create_get():
    create_resp = actions.create_task("Buy 10 eggs", USER_ID)
    assert create_resp.status_code == 200
    added_task_id = create_resp.json()["task"]["task_id"]
    get_resp = actions.get_task(added_task_id)
    assert get_resp.status_code == 200
    retrieved_task_content = get_resp.json()["content"]
    assert retrieved_task_content == "Buy 10 eggs"


# create a task, delete the task, check if it still exists
def test_create_delete():
    create_resp = actions.create_task("Create to do list", USER_ID)
    assert create_resp.status_code == 200
    added_task_id = create_resp.json()["task"]["task_id"]
    delete_resp = actions.delete_task(added_task_id)
    assert delete_resp.status_code == 200
    get_resp = actions.get_task(added_task_id)
    assert "not found" in get_resp.json()["detail"]


# create a task, update content and status
def test_create_update():
    create_resp = actions.create_task("Some new task", USER_ID)
    assert create_resp.status_code == 200
    added_task_id = create_resp.json()["task"]["task_id"]
    update_resp = actions.update_task(added_task_id, content="Task text updated", is_done=True)
    assert update_resp.status_code == 200
    get_resp = actions.get_task(added_task_id)
    new_content = get_resp.json()["content"]
    new_done_state = get_resp.json()["is_done"]
    assert new_content == "Task text updated"
    assert new_done_state == True


# create a few tasks, list all the tasks
def test_list_user_tasks():
    ...