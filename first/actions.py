import requests
from locators import ROOT_URL, CREATE_URL, GET_TASK_URL, LIST_TASK_URL, DELETE_TASK_URL, UPDATE_URL

# endpoint actions
def check_root_endpoint():
    """ returns response object """
    return requests.get(ROOT_URL)


def create_task(content: str, user_id: str, task_id: str ="", is_done: bool =False) -> requests.Response:
    payload = {
        "content": content,
        "user_id": user_id,
        "task_id": task_id,
        "is_done": is_done
    }
    return requests.put(CREATE_URL, json=payload)


def get_task(task_id: str) -> requests.Response:
    return requests.get(f"{GET_TASK_URL}{task_id}")


def list_user_tasks(user_id: str) -> requests.Response:
    return requests.get(f"{LIST_TASK_URL}{user_id}")


def delete_task(task_id: str) -> requests.Response:
    return requests.delete(f"{DELETE_TASK_URL}{task_id}")

# TODO refactor to use type hints for all parameters
def update_task(task_id: str, content=None, is_done=None) -> requests.Response:
    current_data = get_task(task_id).json()
    new_data = {
        "content": content if content else current_data["content"],
        "user_id": current_data["user_id"],
        "task_id": task_id,
        "is_done": current_data["is_done"] if is_done == None else is_done
    }
    return requests.put(UPDATE_URL, json=new_data)