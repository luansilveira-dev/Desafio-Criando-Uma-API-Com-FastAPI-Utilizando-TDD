import os 

def run_api():
  return os.system("uvicorn store.main:app --reload")

#poetry run pre-commit install
def test():
  return os.system("poetry run pytest")


if __name__ == "__main__":
  test()
