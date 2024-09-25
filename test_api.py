import os
import requests
import json
from dotenv import load_dotenv

#Создание репозитория
def create_repo(name_repos):
  load_dotenv()

  token = os.getenv('GITHUB_TOKEN')
  name = os.getenv('GITHUB_USERNAME')

  if not token or not name:
      print("Error")

  repo_test = name_repos

  url = f'https://api.github.com/user/repos'

  headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
  }

  data = {
    'name': repo_test,
    'private': False
  }

  response = requests.post(url, headers=headers, data=json.dumps(data))

  if response.status_code == 201:
      print(f"Репозиторий {repo_test} успешно создан")
  else:
      print(f'Ошибка при создании репозитория: {response.status_code}')
      print(response.json())


#Удаление репозитория
def del_repo(name_repo):
  load_dotenv()

  token = os.getenv('GITHUB_TOKEN')
  name = os.getenv('GITHUB_USERNAME')

  repo_del = name_repo

  url = f'https://api.github.com/repos/{name}/{repo_del}'

  headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
  }

  response = requests.delete(url, headers= headers)

  if response.status_code == 204:
     print(f"Репозиторий {repo_del} успешно удален")
  else:
     print("Репозиторий не найден")


#Просмотр репозитория
def list_repo():
   load_dotenv()

   token = os.getenv('GITHUB_TOKEN')
   name = os.getenv('GITHUB_USERNAME')
   
   url = f'https://api.github.com/users/{name}/repos'

   headers = {
      'Authorization': f'token {token}'
   }

   response = requests.get(url, headers=headers)

   if response.status_code == 200:
      repos = response.json()
      print("Список репозиториев:")
      for repo in repos:
          print(f'- {repo["name"]}')
   else:
      print("Репозитории отсутствуют")


if __name__ == "__main__":
    print("1. Создание репозитория")
    print("2. Удаление репозитория")
    print("3. Просмотр списка репозиториев")
    choose = int(input("Введите номер меню: "))

    if choose == 1:
      name = str(input("Введите имя репозитория: "))
      create_repo(name)
    elif choose == 2:
       name = str(input("Введите имя репозитория: "))
       del_repo(name)
    elif choose == 3:
       list_repo()
    