import os 

def run_api():
  return os.system("uvicorn store.main:app --reload")

# poetry run pre-commit install
def test():
    return os.system("poetry run pytest")


def test_matching(func_test):
    return os.system(f"poetry run pytest -s -rx {func_test} --pdb store ./tests/")


if __name__ == "__main__":
    # test_matching(func_test="test_usecases_query_should_return_success")
    test()